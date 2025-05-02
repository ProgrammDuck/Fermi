import discord
from discord.ext import commands
import random
import logging

scemb = discord.Embed(
    title='✅ Success ✅',
    colour=discord.Colour.green()
)
eremb = discord.Embed(
    title='❌ Error ❌',
    colour=discord.Colour.red()
)

class fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.logger = logging.getLogger(__name__)
        
    
    @commands.hybrid_command('random', help='Gets random number of your arguments.')
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def random(self, ctx, number_1, number_2):
        if number_1 >= number_2:
            msg = eremb.copy()
            msg.description = 'Number 1 must be less than number 2'
            await ctx.reply(embed=msg)
            return
        
        try:
            number_1 = int(number_1)
            number_2 = int(number_2)
        except ValueError:
            msg = eremb.copy()
            msg.description = 'You need input number!'
            await ctx.reply(embed=msg)
            return

        value = random.randint(number_1, number_2)
        msg = scemb.copy()
        msg.description = f'Your number is **{value}**'
        await ctx.reply(embed=msg)
        
    @commands.hybrid_command('magicball', help='Return random answer to your quesion.')
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def magicball(self, ctx, question):
        yes = discord.Embed(
            title='I think...',
            description='Yes! Without reservations.',
            colour=discord.Colour.blurple()
        )
        
        yes1 = discord.Embed(
            title='I think...',
            description='Yes, partially.',
            colour=discord.Colour.blurple()
        )
        
        idk = discord.Embed(
            title='I dont know.',
            description='Ask at another time.',
            colour=discord.Colour.blurple()
        )
        
        no = discord.Embed(
            title='I think...',
            description='No! This is 100% the true answer.',
            colour=discord.Colour.blurple()
        )
        
        no1 = discord.Embed(
            title='I think...',
            description='No, partially.',
            colour=discord.Colour.blurple()
        )
        
        table = [yes, yes1, idk, no, no1]
        answer = table[random.randint(0, len(table) - 1)]
        
        self.logger.info(f'[MAGICBALL] {question} - {answer}')
        await ctx.reply(embed=answer)
    
async def setup(bot):
    await bot.add_cog(fun(bot))
