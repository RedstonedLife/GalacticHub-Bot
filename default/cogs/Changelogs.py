import json

import discord
from discord import app_commands
from discord.ext import commands

from utilities.Constants import *


class Changelogs(commands.Cog):
    __slots__ = ("bot", "_id", "clgData")

    def __init__(self, bot):
        self.bot = bot
        self._id = bot.bot_id
        with open("cfgs/changelogs.json") as f:
            self.clgData = json.load(f)
            f.close()

    """
    Utilities Section
    """

    def latest(self) -> str:
        return list(self.clgData['changelogs'].keys())[len(list(self.clgData['changelogs'].keys())) - 1]

    def versions(self) -> list[str]:
        return list(self.clgData['changelogs'].keys())

    def create_embed(self, version) -> discord.Embed:
        embed = discord.Embed(title=self.clgData['changelogs'][version]['title'],
                              description=self.clgData['changelogs'][version]['description'],
                              color=COLOR,
                              timestamp=discord_timestamp()
                              )
        for field_dict in self.clgData['changelogs'][version]['fields']:
            tmpDict = dict(field_dict)
            embed.add_field(name=tmpDict['name'], value=tmpDict['value'], inline=tmpDict['inline'])
        embed.set_footer(text="Made By RedstonedLife#9229 & LydiaLovelace#4444 With ❤ From Israel & U.S.A", icon_url=RED_AVATAR)
        return embed

    """
    Slash Commands
    """

    @app_commands.command(name="changelog", description="Displays the changelog of a given version or the latest")
    @app_commands.describe(version="What version are you interested in?")
    async def changelog(self, interaction: discord.Interaction, version: str = None) -> None:
        if not version:  # Proceed with latest
            return await interaction.response.send_message(embed=self.create_embed(self.latest()), ephemeral=True)
        if version not in self.versions():
            return await interaction.response.send_message(f"{interaction.user.mention}, Oops!. I couldn't find the "
                                                           f"version you were looking "
                                  f"for (`{version}`)\nAvailable versions: {','.join(self.versions())}", ephemeral=True)
        await interaction.response.send_message(embed=self.create_embed(version), ephemeral=True)

    """
    Regular Commands
    """

    @commands.command(name="changelog", aliases=["updates", "chlog", "clg"], pass_context=True)
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def changelog_command(self, ctx: discord.ext.commands.Context, version: str = None):
        if not version:  # Proceed with latest
            return await ctx.send(embed=self.create_embed(self.latest()))
        if version not in self.versions():
            return await ctx.send(f"{ctx.message.author.mention}, Oops!. I couldn't find the version you were looking "
                                  f"for (`{version}`)\nAvailable versions: {','.join(self.versions())}", delete_after=5)
        await ctx.send(embed=self.create_embed(version))


async def setup(bot):
    await bot.add_cog(Changelogs(bot))