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
        elif isinstance(error, commands.MissingRequiredArgument):
            msg = eremb.copy()
            msg.description = 'Missing required argument. !help <command>'
            await ctx.reply(embed=msg)
        elif isinstance(error, commands.MissingPermissions):
            msg = eremb.copy()
            msg.description = 'You dont have permissions to eexecute this command.'
            await ctx.reply(embed=msg)
        elif isinstance(error, commands.BotMissingPermissions):
            msg = eremb.copy()
            msg.description = 'Bot doesnt have permissions.'
            await ctx.reply(embed=msg)
        elif isinstance(error, commands.CommandNotFound):
            msg = eremb.copy()
            msg.description = 'Command not found'
            await ctx.reply(embed=msg)
        elif isinstance(error, commands.MemberNotFound):
            msg = eremb.copy()
            msg.description = 'Member not found'
            await ctx.reply(embed=msg)
        
            
            
            
async def setup(bot):
    await bot.add_cog(main(bot))
