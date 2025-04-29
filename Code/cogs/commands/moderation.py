import discord
import asyncio
from discord.ext import commands

scemb = discord.Embed(
    title='✅ Success ✅',
    colour=discord.Colour.green()
)
eremb = discord.Embed(
    title='❌ Error❌',
    colour=discord.Colour.red()
)



class moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.hybrid_command('kick', help='Kick a user from the server')
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        msg = scemb.copy()
        msg.description = f'**{member.name.capitalize()}** has been kicked for `{reason}`'
        await ctx.send(embed=msg)

    @commands.hybrid_command('mute', help='Mute a user in the server')
    async def mute(self, ctx, member: discord.Member, duration: str, *, reason=None):
        duration = duration.lower()
        if duration.endswith('d'):
            time = int(duration[:-1]) * 86400
        elif duration.endswith('h'):
            time = int(duration[:-1]) * 3600
        elif duration.endswith('m'):
            time = int(duration[:-1]) * 60
        elif duration.endswith('s'):
            time = int(duration[:-1])
        else:
            msg = eremb.copy()
            msg.description = 'Invalid duration format. Use **d for days**, **h for hours**, **m for minutes**, **s for seconds.**'
            await ctx.send(embed=msg)
            return

        muted_role = discord.utils.get(ctx.guild.roles, name='Muted')
        if not muted_role:
            muted_role = await ctx.guild.create_role(name='Muted')
            for channel in ctx.guild.channels:
                await channel.set_permissions(muted_role, send_messages=False)
                
                
        await member.add_roles(muted_role)
        msg = scemb.copy()
        msg.description = f'**{member.name.capitalize}** has been muted for **{duration}** for `{reason}`'
        await ctx.send(embed=msg)
        await asyncio.sleep(time)
        await member.remove_roles(muted_role)
        msg = scemb.copy()
        msg.description = f'You have been unmuted after **{duration}**. Please, dont break rule.'
        await member.send(embed=msg)

    @commands.hybrid_command('ban', help='Ban a user from the server')
    async def ban(self, ctx, member: discord.Member, duration: str, *, reason=None):
        duration = duration.lower()
        if duration.endswith('d'):
            time = int(duration[:-1]) * 86400
        elif duration.endswith('h'):
            time = int(duration[:-1]) * 3600
        elif duration.endswith('m'):
            time = int(duration[:-1]) * 60
        elif duration.endswith('s'):
            time = int(duration[:-1])
        else:
            msg = eremb.copy()
            msg.description = 'Invalid duration format. Use **d for days**, **h for hours**, **m for minute**, **s for seconds.**'
            await ctx.send(embed=msg)
            return

        await member.ban(reason=reason)
        msg = scemb.copy()
        msg.description = f'**{member.name.capitalize}** has been banned for **{duration}** for `{reason}`'
        
        await ctx.send(embed=msg)
        await asyncio.sleep(time)
        await ctx.guild.unban(member)
        
        msg = scemb.copy()
        msg.description = f'You have been unbanned after **{duration}**. Please, dont break rule.'
        await member.send(embed=msg)

    @commands.hybrid_command('unmute', help='Unmute a user in the server')
    async def unmute(self, ctx, member: discord.Member):
        muted_role = discord.utils.get(ctx.guild.roles, name='Muted')
        if not muted_role:
            msg = eremb.copy()
            msg.description = 'Muted role not found. Please create a role named "Muted" and configure it.'
            await ctx.send(embed=msg)
            return
        await member.remove_roles(muted_role)
        msg = scemb.copy()
        msg.description = f'{member} has been unmuted.'
        await ctx.send(embed=msg)
    
async def setup(bot):
    await bot.add_cog(moderation(bot))
