from discord.ext import commands
from utilities.SmallWeeb import Paths
from utilities.SmallWeeb import Request
from utilities.WeebyMessage import WeebyMessages
import discord
import datetime


class Weebsh(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.req = Request(Paths())

    @commands.hybrid_command(pass_context=True, description="Awe ;(. Here lemme hug you!")
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def cry(self, ctx):
        u = self.req.cry()
        embed = discord.Embed(color=0xf3f3f3)
        embed.set_author(name=WeebyMessages('sEmote', 'cry', ctx.message.author, None, True).__message__(), url=u[0],
                         icon_url=ctx.message.author.display_avatar if not ctx.message.author.guild_avatar else ctx.message.author.guild_avatar)
        embed.set_image(url=u[0])
        if self.bot.debugMode:
            embed.set_footer(text=f"DEBUG: Fetch Time: {'{:.2f}'.format(u[1]/1000)} seconds")
        await ctx.send(embed=embed)

    @commands.hybrid_command(pass_context=True, description="Hug somebody!")
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def hug(self, ctx, member: discord.Member = None):
        if not member or member == ctx.message.author:
            mes = WeebyMessages('uEmote', 'hug', ctx.message.author, None, True).__message__()
            return await ctx.send(mes)
        u = self.req.hug()
        embed = discord.Embed(color=0xf3f3f3)
        embed.set_author(name=WeebyMessages('uEmote', 'hug', ctx.message.author, member, False).__message__(), url=u[0],
                         icon_url=ctx.message.author.display_avatar if not ctx.message.author.guild_avatar else ctx.message.author.guild_avatar)
        embed.set_image(url=u[0])
        if self.bot.debugMode:
            embed.set_footer(text=f"DEBUG: Fetch Time: {'{:.2f}'.format(u[1]/1000)} seconds")
        await ctx.send(embed=embed)

    @commands.hybrid_command(pass_context=True, description="Mwah!")
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def kiss(self, ctx, member: discord.Member = None):
        if not member or member == ctx.message.author:
            mes = WeebyMessages('uEmote', 'kiss', ctx.message.author, None, True).__message__()
            return await ctx.send(mes)
        u = self.req.kiss()
        embed = discord.Embed(color=0xf3f3f3)
        embed.set_author(name=WeebyMessages('uEmote', 'kiss', ctx.message.author, member, False).__message__(), url=u[0],
                         icon_url=ctx.message.author.display_avatar if not ctx.message.author.guild_avatar else ctx.message.author.guild_avatar)
        embed.set_image(url=u[0])
        if self.bot.debugMode:
            embed.set_footer(text=f"DEBUG: Fetch Time: {'{:.2f}'.format(u[1]/1000)} seconds")
        await ctx.send(embed=embed)

    @commands.hybrid_command(pass_context=True, description="Cuddle someone!")
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def cuddle(self, ctx, member: discord.Member = None):
        if not member or member == ctx.message.author:
            mes = WeebyMessages('uEmote', 'cuddle', ctx.message.author, None, True).__message__()
            return await ctx.send(mes)
        u = self.req.cuddle()
        embed = discord.Embed(color=0xf3f3f3)
        embed.set_author(name=WeebyMessages('uEmote', 'cuddle', ctx.message.author, member, False).__message__(), url=u[0],
                         icon_url=ctx.message.author.display_avatar if not ctx.message.author.guild_avatar else ctx.message.author.guild_avatar)
        embed.set_image(url=u[0])
        if self.bot.debugMode:
            embed.set_footer(text=f"DEBUG: Fetch Time: {'{:.2f}'.format(u[1]/1000)} seconds")
        await ctx.send(embed=embed)

    @commands.hybrid_command(pass_context=True, description="Slap someone! (How dareth thou!?)")
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def slap(self, ctx, member: discord.Member = None):
        if not member or member == ctx.message.author:
            mes = WeebyMessages('uEmote', 'slap', ctx.message.author, None, True).__message__()
            return await ctx.send(mes)
        u = self.req.slap()
        embed = discord.Embed(color=0xf3f3f3)
        embed.set_author(name=WeebyMessages('uEmote', 'slap', ctx.message.author, member, False).__message__(),
                         url=u[0],
                         icon_url=ctx.message.author.display_avatar if not ctx.message.author.guild_avatar else ctx.message.author.guild_avatar)
        embed.set_image(url=u[0])
        if self.bot.debugMode:
            embed.set_footer(text=f"DEBUG: Fetch Time: {'{:.2f}'.format(u[1]/1000)} seconds")
        await ctx.send(embed=embed)

    @commands.hybrid_command(pass_context=True, description="Kermit the frog!")
    @commands.cooldown(1, 60, commands.BucketType.user)
    async def kermit(self, ctx):
        u = self.req.kermit()
        embed = discord.Embed(color=0xf3f3f3).set_image(url=u[0])
        if self.bot.debugMode:
            embed.set_footer(text=f"DEBUG: Fetch Time: {'{:.2f}'.format(u[1]/1000)} seconds")
        await ctx.send(embed=embed)

    @commands.hybrid_command(pass_context=True, description="Pet someone :)")
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def pat(self, ctx, member: discord.Member = None):
        if not member or member == ctx.message.author:
            mes = WeebyMessages('uEmote', 'pat', ctx.message.author, None, True).__message__()
            return await ctx.send(mes)
        u = self.req.pat()
        embed = discord.Embed(color=0xf3f3f3)
        embed.set_author(name=WeebyMessages('uEmote', 'pat', ctx.message.author, member, False).__message__(), url=u[0],
                         icon_url=ctx.message.author.display_avatar if not ctx.message.author.guild_avatar else ctx.message.author.guild_avatar)
        embed.set_image(url=u[0])
        if self.bot.debugMode:
            embed.set_footer(text=f"DEBUG: Fetch Time: {'{:.2f}'.format(u[1]/1000)} seconds")
        await ctx.send(embed=embed)

    @commands.hybrid_command(pass_context=True, description=":< | Why Are You Pouting")
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def pout(self, ctx):
        u = self.req.pout()
        embed = discord.Embed(color=0xf3f3f3)
        embed.set_author(name=WeebyMessages('sEmote', 'pout', ctx.message.author, None, True).__message__(), url=u[0],
                         icon_url=ctx.message.author.display_avatar if not ctx.message.author.guild_avatar else ctx.message.author.guild_avatar)
        embed.set_image(url=u[0])
        if self.bot.debugMode:
            embed.set_footer(text=f"DEBUG: Fetch Time: {'{:.2f}'.format(u[1]/1000)} seconds")
        await ctx.send(embed=embed)

    @commands.hybrid_command(pass_context=True, description="Tickle somebody!")
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def tickle(self, ctx, member: discord.Member = None):
        if not member or member == ctx.message.author:
            mes = WeebyMessages('uEmote', 'tickle', ctx.message.author, None, True).__message__()
            return await ctx.send(mes)
        u = self.req.tickle()
        embed = discord.Embed(color=0xf3f3f3)
        embed.set_author(name=WeebyMessages('uEmote', 'tickle', ctx.message.author, member, False).__message__(), url=u[0],
                         icon_url=ctx.message.author.display_avatar if not ctx.message.author.guild_avatar else ctx.message.author.guild_avatar)
        embed.set_image(url=u[0])
        if self.bot.debugMode:
            embed.set_footer(text=f"DEBUG: Fetch Time: {'{:.2f}'.format(u[1]/1000)} seconds")
        await ctx.send(embed=embed)

    @commands.hybrid_command(pass_context=True, description="Stare at someone O_O")
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def stare(self, ctx, member: discord.Member = None):
        if not member or member == ctx.message.author:
            mes = WeebyMessages('uEmote', 'stare', ctx.message.author, None, True).__message__()
            return await ctx.send(mes)
        u = self.req.stare()
        embed = discord.Embed(color=0xf3f3f3)
        embed.set_author(name=WeebyMessages('uEmote', 'stare', ctx.message.author, member, False).__message__(), url=u[0],
                         icon_url=ctx.message.author.display_avatar if not ctx.message.author.guild_avatar else ctx.message.author.guild_avatar)
        embed.set_image(url=u[0])
        if self.bot.debugMode:
            embed.set_footer(text=f"DEBUG: Fetch Time: {'{:.2f}'.format(u[1]/1000)} seconds")
        await ctx.send(embed=embed)


class EmbedConstructor:
    def __init__(self, message: str = None, author: discord.Member = None, url: str = None):
        self.message = message
        self.author = author
        self.url = url
        self.construct()

    def construct(self):
        self.embed = discord.Embed(color=0xf3f3f3)
        self.embed.set_author(name=self.message, url=self.url[0], icon_url=self.author.avatar_url)
        self.embed.set_image(url=self.url[0])


async def setup(bot):
    await bot.add_cog(Weebsh(bot))
