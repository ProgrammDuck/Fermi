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
        
    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, error):
        command = self.bot.get_command(ctx.command.name)
        if isinstance(error, commands.errors.CommandOnCooldown):
            msg = eremb.copy()
            msg.description = error
            await ctx.reply(embed=msg)
        elif isinstance(error, commands.MissingRequiredArgument):
            msg = eremb.copy()
            msg.description = f'Missing required argument.\nUsage: `{self.bot.command_prefix}{command.name} {command.signature}`'
            await ctx.reply(embed=msg)
        elif isinstance(error, commands.MissingPermissions):
            msg = eremb.copy()
            msg.description = 'You dont have permissions to execute this command.'
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
    await bot.add_cog(errors(bot))
