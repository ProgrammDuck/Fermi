# ⁡⁢⁣⁡⁢⁣⁡⁢⁡⁢⁣⁣𝗶𝗺𝗽𝗼𝗿𝘁 𝗹𝗶𝗯𝘀⁡
import discord
from discord.ext import commands
import os

load_cogs = [
    'cogs.commands.roblox',
    'cogs.commands.main',
    'cogs.events.errors',
    'cogs.commands.moderation'
]

def main():
    intents = discord.Intents.all()
    intents.message_content = True
    bot = commands.Bot('!', help_command=None, intents=intents, case_insensitive=True)
    
    @bot.command(name='sync', hidden=True)
    @commands.is_owner()
    async def sync(ctx, id = None):
        if id:
            await bot.tree.sync(guild=discord.Object(id))
            print('Syncing')
            await ctx.reply(f'Synced the {id}', ephemeral=True)
        else:
            await bot.tree.sync()
            print('Global Syncing ~ 1 hour')
            await ctx.reply(f'Syncing | ~ 1 hour', ephemeral=True)
    
    @bot.event
    async def on_ready():
        print(f'Logged as {bot.user.name}')
        await bot.change_presence(activity=discord.Game(f'{bot.command_prefix}Help | ProgrammDuck'), status=discord.Status.idle)
        
        for cog in load_cogs:
            try:
                await bot.load_extension(cog)
                print(f'Loaded extension: {cog}')
            except Exception as e:
                print(f'Failed to load extension {cog}: {e}')
        
    bot.run(str(os.getenv('DISCORD_TOKEN')))
main()