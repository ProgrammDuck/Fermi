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



class main(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_command_error(self, error, ctx: commands.Context):
        if isinstance(error, commands.errors.CommandOnCooldown):
            msg = eremb.copy()
            msg.description = error
            await ctx.reply(embed=msg)
async def setup(bot):
    await bot.add_cog(main(bot))
