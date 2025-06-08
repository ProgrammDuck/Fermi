import discord
from discord.ext import commands
from discord.ui import Button, View
import logging

from embeds import scemb, eremb

class project(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.logger = logging.getLogger(__name__)
    
    #⁡⁢⁣⁣---𝗘𝘃𝗲𝗻𝘁𝘀---⁡
    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        guild = member.guild
        channel = guild.system_channel
        if guild.id == 1318581808258089000:
                channel = guild.get_channel(1318645056487559319)
                msg = discord.Embed(
                    title='New member!',
                    description=f'Hello, {member.mention}. Welcome to **{guild.name}**. If u need anything dont worry to contact our staff!',
                    colour=discord.Colour.orange()
                )
                msg.add_field(name='Total members:', value=guild.member_count)
                await channel.send(embed=msg)
        else:
            msg = discord.Embed(
                    title='New member!',
                    description=f'Hello, {member.mention}. Welcome to **{guild.name}**.',
                    colour=discord.Colour.orange()
                )
            msg.add_field(name='Total members:', value=guild.member_count)
            await channel.send(embed=msg)
    
    
    #⁡⁢⁣⁣---𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀---⁡
    @commands.hybrid_command('embedmessage', help='Send the message as embed.')
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def embedmessage(self, ctx:commands.Context, title, *, message):
        msg = discord.Embed(
            title=title,
            description=message,
            colour=discord.Colour.orange()
        )
        msg.set_footer(text=f'Best regards, \n• Your {ctx.author.top_role.name} - {ctx.author.name}')
        await ctx.send(embed=msg)

        
async def setup(bot):
    await bot.add_cog(project(bot))
