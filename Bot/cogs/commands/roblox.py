import discord
from discord.ext import commands

import aiohttp
import os
import logging

from Bot.embeds import scemb, eremb


class roblox(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.logger = logging.getLogger(__name__)
        
    @commands.hybrid_command('send', help='Sending your message to roblox servers')
    @commands.cooldown(1, 3, commands.BucketType.guild)
    async def send(self, ctx, *, message):
        key = os.getenv('ROBLOX_API_KEY1')
        universeid = 6362476013
        url = f'https://apis.roblox.com/cloud/v2/universes/{universeid}:publishMessage'
        
        headers = {
            'x-api-key': key,
            'Content-Type': 'application/json'
        }
        
        payload = {
            "topic": "SendMessage", 
            "message": message 
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(url, headers=headers, json=payload) as responce:
                if responce.status == 200:
                    msg = scemb.copy()
                    msg.description = 'Your message delivered to roblox.'
                    self.logger.info(f'{ctx.author.name} sended "{message}" to roblox')
                    await ctx.reply(embed=msg)
                else:
                    msg = eremb.copy()
                    msg.description = f'code: {responce.status}'
                    await ctx.reply(embed=msg)

async def setup(bot):
    await bot.add_cog(roblox(bot))
