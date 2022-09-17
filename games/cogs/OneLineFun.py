import datetime as dt
import time, random
import discord
from discord.ext import commands
from discord import app_commands
from discord.utils import get

import main
from utilities.Constants import *


class OneLineFun(commands.Cog):
    """Help Commands"""
    __slots__ = ("bot", "_id", "responses")

    def __init__(self, bot: main.Bot):
        self.bot = bot
        self._id = bot.bot_id
        self.responses = ["Not so sure", "42", "Most likely", "Absolutely not", "Outlook is good",
                          "I see good things happening", "Never",
                          "Negative", "Could be", "Unclear, ask again", "Yes", "No", "Possible, but not probable"]

    """
    Slash Command
    """

    @app_commands.command(name="cookie",description="You want a cookie? Maybe give one to a fellow friend! :)")
    @app_commands.describe(member="Gives your fellow friend a cookie! :)")
    async def cookie(self, interaction: discord.Interaction, member: discord.Member = None) -> None:
        if not member:
            return await interaction.response.send_message(f"{interaction.user.mention} Here have a 🍪 or 🍪🍪",
                                                           ephemeral=True)
        if member.id is interaction.user.id:
            return await interaction.response.send_message(
                f"{interaction.user.mention} awww. You can't give yourself "
                f"a cookie, here take this one from me 🍪", ephemeral=True)
        return await interaction.response.send_message(f"{member.mention}, {interaction.user.mention} gave you a 🍪",
                                                       ephemeral=False)

    @app_commands.command(name="8ball", description="Ask the mysterious 8ball a question!")
    @app_commands.describe(question="Ask the mysterious 8ball any question your heart desires!")
    async def ball(self, interaction: discord.Interaction, question: str = None):
        if not question:
            return await interaction.response.send_message("What question shall you ask the magic 8ball?",
                                                           ephemeral=True)
        #
        blank = get(interaction.message.channel.guild.emojis, name="blank")
        return await interaction.response.send_message(
            f':8ball:** | {interaction.message.author.display_name} asked:** {question}\n{blank}** | Answer:** {random.choice(self.responses)}', ephemeral=False)

    """
    Regular prefix commands
    """

    @commands.command(name="cookie", pass_context=True)
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def cookie_command(self, ctx, member: discord.Member = None):
        if member is ctx.message.author:
            return await ctx.send(f"{ctx.message.author.mention} awww. You can't give yourself "
                                  f"a cookie, here take this one from me 🍪")
        if not member:
            return await ctx.send(ctx.message.author.mention + " Here have a 🍪 or 🍪🍪")
        return await ctx.send(member.mention + ", " + ctx.message.author.mention + " gave you a 🍪")

    @commands.command(pass_context=True, name="8ball")
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def ball_command(self, ctx):
        question = str(ctx.message.content).split(f"{self.bot.command_prefix}8ball ")
        if len(question) == 1:
            return await ctx.send("What question shall you ask the magic 8ball?", delete_after=5)
        #
        blank = get(ctx.message.channel.guild.emojis, name="blank")
        return await ctx.send(
            f':8ball:** | {ctx.message.author.display_name} asked:** {question[1]}\n{blank}** | Answer:** {random.choice(self.responses)}')

    @commands.command(pass_context=True)
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def cake(self, ctx):
        return await ctx.send(embed=discord.Embed().set_image(
            url="https://wompampsupport.azureedge.net/fetchimage?siteId=7575&v=2&jpgQuality=100&width=700&url=https"
                "%3A%2F%2Fi.kym-cdn.com%2Fentries%2Ficons%2Ffacebook%2F000%2F001%2F707%2Fthecakeisalie.jpg"))


async def setup(bot):
    await bot.add_cog(OneLineFun(bot))
