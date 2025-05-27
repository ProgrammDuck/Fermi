import discord
from discord.ext import commands
from discord.ui import Button, View
import logging

scemb = discord.Embed(
    title='✅ Success ✅',
    colour=discord.Colour.green()
)
eremb = discord.Embed(
    title='❌ Error ❌',
    colour=discord.Colour.red()
)

class owner(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot
        self.logger = logging.getLogger(__name__)
    
    #⁡⁢⁣⁣---𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀---⁡
    @commands.command('delete_message', hidden=True)
    @commands.is_owner()
    async def delete_message(self, ctx, message:discord.Message):
        await message.delete()

    @commands.command('send_message', hidden=True)
    @commands.is_owner()
    async def send_message(self, ctx, channelid, *, message):
        channel = await self.bot.fetch_channel(channelid)
        await channel.send(message)
    
async def setup(bot):
    await bot.add_cog(owner(bot))
