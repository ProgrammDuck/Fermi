import discord
from discord.ext import commands


import logging

from Bot.embeds import scemb, eremb


class test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.logger = logging.getLogger(__name__)

    @commands.command('test_scemb', hidden=True)
    @commands.is_owner()
    async def test_scemb(self, ctx: commands.Context):
        msg = scemb.copy()
        await ctx.reply(embed=msg)
        
    @commands.command('test_eremb', hidden=True)
    @commands.is_owner()
    async def test_eremb(self, ctx):
        msg = eremb.copy()
        await ctx.reply(embed=msg)
        
async def setup(bot):
    await bot.add_cog(test(bot))
