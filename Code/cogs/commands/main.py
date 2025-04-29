import discord
from discord.ext import commands

scemb = discord.Embed(
    title='✅ Success ✅',
    colour=discord.Colour.green()
)
eremb = discord.Embed(
    title='❌ Error ❌',
    colour=discord.Colour.red()
)

class main(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    
    @commands.hybrid_command('clear', help='Clearing messages', aliases=['purge'])
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, value = 10):
        value += 1
        await ctx.channel.purge(limit=value)
        msg = scemb.copy()
        msg.description = f'{value - 1} messages cleared'
        await ctx.send(embed=msg, delete_after=5)
        
        
    @commands.hybrid_command('echo', help='Repeat your message')
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def echo(self, ctx, *, message):
        await ctx.reply(message)
        
    
    @commands.hybrid_command('info', help='Information of the bot.')
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def info(self, ctx):
        msg = discord.Embed(
            title='Information',
            description='This is a open-source bot\n - [Github](https://github.com/ProgrammDuck/Ppoker)\n   - created by <@916019025945976842>. He is my Dad). I have only 1 developer. You can change this bot for your hope, This all.',
            colour=discord.Colour.blue()
        )

        await ctx.reply(embed=msg)

    @commands.hybrid_command('ping', help='Check if the bot is online')
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def ping(self, ctx):
        await ctx.reply('Pong!')

    @commands.hybrid_command('help', help='List all available commands')
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def help(self, ctx, command_name: str = None):
        if command_name:
            command = self.bot.get_command(command_name)
            if command and not command.hidden:
                msg = discord.Embed(
                    description=f'Argument:\n`[]` - optional\n`<>` - required',
                    colour=discord.Colour.blue()
                )
                msg.add_field(name=command.name.capitalize(), value=f'{command.help}\nUsage: `{self.bot.command_prefix}{command.name} {command.signature}`', inline=False)
                await ctx.reply(embed=msg)
            else:
                msg = eremb.copy()
                msg.description = f'Command `{command_name}` not found.'
                await ctx.reply(embed=msg)
        else:
            msg = discord.Embed(
                title='Available Commands',
                description=f'Use `{self.bot.command_prefix}` as the prefix for all commands.',
                colour=discord.Colour.blue()
            )
            for command in self.bot.commands:
                msg.add_field(name=command.name.capitalize(), value=f'{command.help}\nUsage: `{self.bot.command_prefix}{command.name} {command.signature}`', inline=False)

            await ctx.reply(embed=msg)
            
    
async def setup(bot):
    await bot.add_cog(main(bot))
