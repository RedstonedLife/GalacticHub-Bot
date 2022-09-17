import discord
from discord.ext import commands

from main import Bot


class Debug(commands.Cog):
    __slots__ = ("bot", "_id")

    def __init__(self, bot: Bot):
        self.bot = bot
        self._id = bot.bot_id

    @commands.hybrid_command(
        name="debug",
        aliases=["dbgm", "dbm"],
        description="Puts bot into debug mode (Bot Owner Only)",
        pass_context=True
    )
    async def debug_cmd(self, ctx: discord.ext.commands.Context):
        if ctx.message.author.id in self.bot.authors_id:
            if self.bot.debugMode:
                self.bot.debugMode = False
                await ctx.send(mention_author=True,
                               content="Debug mode was set to `false`",
                               ephemeral=True)
            else:
                self.bot.debug()
                await ctx.send(mention_author=True,
                               content="Debug mode was set to `true`",
                               ephemeral=True)
        else:
            await ctx.send(mention_author=True,
                           content="Whoops!, this command is for the bot developers only!",
                           ephemeral=True)


async def setup(bot):
    await bot.add_cog(Debug(bot))
