import datetime as dt
import time
import discord
from discord.ext import commands
from discord import app_commands
from discord.utils import get

import main
from utilities.Constants import *


class Help(commands.Cog):
    """Help Commands"""
    __slots__ = ("bot", "_id")

    def __init__(self, bot):
        self.bot = bot
        self._id = bot.bot_id

    @commands.command(name="help", aliases=["h"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def help(self, ctx: discord.ext.commands.Context, help_type: str = ""):
        return await ctx.send("Nothing to see yet! (Gets deleted after 5 seconds)", delete_after=5)

    @commands.hybrid_command(name="info", aliases=["botinfo", "binfo"], description="Displays the bot info!")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def info(self, ctx: discord.ext.commands.Context):
        embed = discord.Embed(title=f"Galactic Hub Bot", color=COLOR, timestamp=discord_timestamp())
        embed.set_thumbnail(url=ME_AVATAR)
        embed.add_field(name="Version ", value=f"`{self.bot.version}`", inline=True)
        embed.add_field(name="Author", value="<@!292016137926082560>\n<@!927207732002586674>", inline=True)
        embed.add_field(name="Prefix", value=f"`{self.bot.command_prefix}`", inline=True)
        #thanks_string = ""
        #for tAr in self.bot.thanks:
        #    thanks_string += f"<@!{tAr[0]}> - {tAr[1]}\n"
        #embed.add_field(name="Special Thanks",value=thanks_string,inline=False)
        embed.set_footer(text="Made By RedstonedLife#9229 & LydiaLovelace#4444 With ❤ From Israel & U.S.A",
                         icon_url=ME_AVATAR)
        await ctx.send(embed=embed, ephemeral=True)


async def setup(bot):
    await bot.add_cog(Help(bot))