import discord
from discord.ext import commands

scemb = discord.Embed(
    title='✅ Success ✅',
    colour=discord.Colour.green()
)
eremb = discord.Embed(
    title='❌ Error❌',
    colour=discord.Colour.red()
)



class errors(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.hybrid_command('clear', help='Clearing messages', aliases=['purge'])
    async def clear(self, ctx, value = 10):
        value += 1
        await ctx.channel.purge(limit=value)
        msg = scemb.copy()
        msg.description = f'{value - 1} messages cleared'
        await ctx.send(embed=msg, delete_after=5)
        
        
    @commands.hybrid_command('echo', help='Repeat your message')
    async def echo(self, ctx, *, message):
        await ctx.reply(message)
        
    
    @commands.hybrid_command('info', help='Information of the bot.')
    async def info(self, ctx):
        msg = discord.Embed(
            title='Information',
            description='This is a open-source bot\n - [Github](https://github.com/ProgrammDuck/Ppoker)\n   - created by <@916019025945976842>. He is my Dad). I have only 1 developer. You can change this bot for your hope, This all.',
            colour=discord.Colour.blue()
        )
        
        await ctx.reply(embed=msg)
        
    

async def setup(bot):
    await bot.add_cog(errors(bot))
