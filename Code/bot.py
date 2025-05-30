# ⁡⁢⁣⁡⁢⁣⁡⁢⁡⁢⁣⁣𝗶𝗺𝗽𝗼𝗿𝘁 𝗹𝗶𝗯𝘀⁡
import discord
from discord.ext import commands
import os
import logging

load_cogs = [
    'cogs.commands.roblox',
    'cogs.commands.main_commands',
    'cogs.events.errors',
    'cogs.commands.moderation',
    'cogs.commands.fun',
    'cogs.commands.project',
    'cogs.commands.owner',
    'cogs.commands.misc'
]

scemb = discord.Embed(
    title='✅ | Success',
    colour=discord.Colour.green()
)
eremb = discord.Embed(
    title='❌ | Error',
    colour=discord.Colour.red()
)

def main():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('bot_logs.log'),
            logging.StreamHandler()
        ]
    )
    logging.warning('-----------------------NEW SESSION-----------------------')
    intents = discord.Intents.all()
    intents.message_content = True
    bot = commands.Bot('&', help_command=None, intents=intents, case_insensitive=True)

    @bot.event
    async def on_ready():
        logging.info(f'Logged as {bot.user.name}')
        await bot.change_presence(activity=discord.Game(f'{bot.command_prefix}Help | ProgrammDuck'), status=discord.Status.idle)

        logging.info('-----LOADING EXTENSIONS-----')
        for cog in load_cogs:
            try:
                await bot.load_extension(cog)
                logging.info(f'Loaded extension: {cog}')
            except Exception as e:
                logging.error(f'Failed to load extension {cog}: {e}')
        logging.info('----------------------------')
        
    bot.run(str(os.getenv('DISCORD_TOKEN')))
main()
