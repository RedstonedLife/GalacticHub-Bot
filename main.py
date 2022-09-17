import discord
import json
import logging
import os
import datetime
import sqlite3
import asyncio
from discord.ext import commands
from discord.utils import get, find
import random

from utilities.Constants import *


def initLogger() -> logging.Logger:
    if os.path.exists("logs/"):
        pass
    else:
        os.mkdir("logs/")
    lg = logging.getLogger("GLHUB_LOG")
    lg.setLevel(logging.DEBUG)
    handler = logging.FileHandler(
        filename=f"logs/bot-{datetime.datetime.now().strftime('%d-%m-%Y')}.log",
        encoding="utf-8",
        mode="a"
    )
    handler.setFormatter(
        logging.Formatter(
            "%(asctime)s:%(levelname)s:%(name)s: %(message)s"
        )
    )
    lg.addHandler(handler)
    return lg


def initTokens() -> json:
    try:
        with open("cfgs/tokens.json", "r") as f:
            data = json.loads(f.read())
            f.close()
            return data
    except Exception as e:
        print(e)
        exit(-1)


def initConfig() -> json:
    try:
        with open("cfgs/bot.json", "r") as f:
            data = json.loads(f.read())
            f.close()
            return data
    except Exception as e:
        print(e)
        exit(-1)


def initdbConfig() -> json:
    try:
        with open("cfgs/database.json", "r") as f:
            data = json.loads(f.read())
            f.close()
            return data
    except Exception as e:
        print(e)
        exit(-1)


logger = initLogger()
botData = initConfig()
tokens = initTokens()
databaseData = initdbConfig()


class Bot(commands.Bot):
    __slots__ = ("modules", "bot_id", "script_start_dt", "authors_id", "version", "elist")

    def __init__(self, *args, loop=None, **kwargs):
        super().__init__(
            command_prefix=botData['prefix'],
            activity=discord.Game(name=f"{botData['prefix']} | Loading..."),
            status=discord.Status.dnd,
            intents=discord.Intents.all()
        )
        self.remove_command("help")
        self.modules = botData['modules']
        self._setup_databases()
        self.script_start_dt = datetime.datetime.now()
        self.bot_id = botData['bot-id']
        self.authors_id = botData['authors-id']
        self.version = botData['version']
        self.elist = None
        self.synced = False

    async def _load_emojis(self, guild: discord.Guild):
        for file in os.listdir("data/emojis/"):
            try:
                emoji_id = get(guild.emojis, name=file[:-4])
                if not emoji_id:
                    with open(f"data/emojis/{file}", "rb") as img:
                        await guild.create_custom_emoji(name=file[:-4], image=img.read())
                        img.close()
                        print(f"Added Emoji {file[:-4]}")
                else:
                    print(f"Did not add Emoji :{file[:-4]}: because it already exists")
            except Exception:
                logger.exception(f"Failed to add emoji {file}")

    def _setup_databases(self):
        if os.path.exists(f"data/databases/"):
            pass
        else:
            os.mkdir("data/databases")
        for database in databaseData['databases']:
            if os.path.exists(f"data/databases/{database}{databaseData['file_extension']}"):
                pass
            else:
                try:
                    sqlite3.connect(f"data/databases/{database}{databaseData['file_extension']}").close()
                    print(f"Created data/databases/{database}{databaseData['file_extension']}")
                    logger.info(f"Created data/databases/{database}{databaseData['file_extension']}")
                except sqlite3.Error:
                    print("Failed")

    async def on_guild_join(self, guild: discord.Guild):
        await self.wait_until_ready()
        await self._load_emojis(guild)

    async def on_command_error(self, context: commands.Context, exception: commands.CommandError) -> None:
        if isinstance(exception, commands.CommandNotFound):
            await context.send(
                "That command does not exist :confused:\nPlease use `{}help` for a list of commands".format(
                    self.command_prefix
                ),
                delete_after=5
            )
            # Handling command not found errors
        if isinstance(exception, commands.CommandOnCooldown):
            await context.send(
                '{}'.format(context.author.mention),
                embed=discord.Embed(
                    title=":alarm_clock: Cooldown Error",
                    description=f"Please cooldown a little, try again in `{exception.retry_after:.2}s`",
                    color=COOLDOWN_COLOR
                ),
                delete_after=5
            )
            # A little artistic touch
        else:
            # raise error
            await context.send(
                embed=discord.Embed(
                    title="Error",
                    description=f"{exception} Invalid command see `{self.command_prefix}help`.\nIf you think this is a bot error, report this to the author",
                    color=ERROR_COLOR,
                    timestamp=datetime.datetime.utcnow()
                ),
                delete_after=5
            )

    def run(self, token, *args, **kwargs):
        try:
            super().run(token, *args, **kwargs)
        except KeyboardInterrupt:
            try:
                self.loop.run_until_complete(self._close())
                logger.info("Shutting down")
                print("Shutting down")
                exit(130)
            except Exception as e:
                logger.exception(e, exc_info=True)
                exit(1)

    async def on_command(self, ctx):
        self.commands_used += 1

    async def on_ready(self):
        self.elist = {e.name: str(e) for e in self.emojis}
        for guild in self.guilds:
            await self._load_emojis(guild=guild)
        print("Bot is ready to engage!")
        if not self.synced:
            await self.tree.sync()
            self.synced = True
        print("Bot synced slash commands!")
        await self.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.listening,
                name=f"{self.command_prefix}help"
            )
        )


async def load_extensions(client: Bot):
    for module in client.modules:
        if len(os.listdir(f"{module}/cogs/")) == 0:
            print(f"{module}.cogs is empty")
        else:
            for file in os.listdir(f"{module}/cogs/"):
                try:
                    if file.endswith(".py") and not file[:-3] == "__init__":
                        await client.load_extension(f'{module}.cogs.{file[:-3]}')
                        logger.info(f"Loaded {module}.cogs.{file[:-3]}")
                        print(f"Loaded {module}.cogs.{file[:-3]}")
                except Exception as e:
                    print(f"Failed to load {module}.cogs.{file[:-3]}")
                    print(e)
                    logger.exception(f"Failed to load {module}.cogs.{file[:-3]}")


async def unload_extensions(client: Bot):
    for module in client.modules:
        if len(os.listdir(f"{module}/cogs/")) == 0:
            print(f"{module}.cogs is empty")
        else:
            for file in os.listdir(f"{module}/cogs/"):
                try:
                    if file.endswith(".py") and not file[:-3] == "__init__":
                        await client.unload_extension(f'{module}.cogs.{file[:-3]}')
                        logger.info(f"Unloaded {module}.cogs.{file[:-3]}")
                        print(f"Unloaded {module}.cogs.{file[:-3]}")
                except Exception:
                    print(f"Failed to unload {module}.cogs.{file[:-3]}")
                    logger.exception(f"Failed to unload {module}.cogs.{file[:-3]}")


async def main():
    async with bot:
        await load_extensions(bot)
        await bot.start(tokens['discord'], reconnect=True)

if __name__ == "__main__":
    bot = Bot()
    asyncio.run(main())
