import discord
from discord.ext import commands

import logging
import aiohttp
from bs4 import BeautifulSoup
import random

scemb = discord.Embed(
    title='✅ | Success',
    colour=discord.Colour.green()
)
eremb = discord.Embed(
    title='❌ | Error',
    colour=discord.Colour.red()
)

class images_commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.logger = logging.getLogger(__name__)
        
    
    @commands.hybrid_command('meow', help='Gets random number of your arguments.')
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def meow(self, ctx):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get('https://api.thecatapi.com/v1/images/search') as response:
                    if response.status == 200:
                        data = await response.json()
                        image_url = data[0]['url']
                        
                        embed = discord.Embed(
                            title='🐱 Meow!', 
                            description=f'[Open in browser]({image_url})',
                            colour=discord.Colour.orange()
                        )
                        
                        embed.set_image(url=image_url)
                        embed.set_footer(text=f"The \"!meow\" command provides random cat images using a public API. This is done through integration with The Cat API, one of the most trusted sources of cat images on the web. (Powered by The Cat API - thecatapi.com)")
                        await ctx.send(embed=embed)
                    else:
                        await ctx.send("API error")
        
        except Exception as e:
            msg = eremb.copy()
            msg.description = f"Error: {str(e)}"
            await ctx.send(embed=msg)
            
async def setup(bot):
    await bot.add_cog(images_commands(bot))
