import discord
import asyncio
from discord.ext import commands
import logging

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
        self.bot: commands.Bot  = bot
        self.logger = logging.getLogger(__name__)

    @commands.hybrid_command('kick', help='Kick a user from the server')
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        if member == ctx.author:
            raise commands.CommandError("yourself")
        elif member == ctx.guild.me:
            raise commands.CommandError("bot_doing")
        elif ctx.guild.me.top_role <= member.top_role:
            raise commands.CommandError("BotRoleTooLow")
        elif ctx.author.top_role <= member.top_role and ctx.author != ctx.guild.owner:
            raise commands.CommandError("AuthorRoleTooLow")
        
        await member.kick(reason=reason)
        msg = scemb.copy()
        msg.description = f'**{member.name.capitalize()}** has been kicked for `{reason}`'
        await ctx.send(embed=msg)
        self.logger.info(f'[KICK] Kicked the {member.name} for {reason} by {ctx.author.name}')

    @commands.hybrid_command('mute', help='Mute a user in the server')
    async def mute(self, ctx, member: discord.Member, duration: str, *, reason=None):
        if member == ctx.author:
            raise commands.CommandError("yourself")
        elif member == ctx.guild.me:
            raise commands.CommandError("bot_doing")
        elif ctx.guild.me.top_role <= member.top_role:
            raise commands.CommandError("BotRoleTooLow")
        elif ctx.author.top_role <= member.top_role and ctx.author != ctx.guild.owner:
            raise commands.CommandError("AuthorRoleTooLow")
        
        
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
        self.logger.info(f'[KICK] {member.name} has been muted for {reason} by {ctx.author.name}')
        await ctx.send(embed=msg)
        await asyncio.sleep(time)
        await member.remove_roles(muted_role)
        msg = scemb.copy()
        msg.description = f'You have been unmuted after **{duration}**. Please, dont break rule.'
        await member.send(embed=msg)

    @commands.hybrid_command('ban', help='Ban a user from the server')
    async def ban(self, ctx, member: discord.Member, duration: str, *, reason=None):
        if member == ctx.author:
            raise commands.CommandError("yourself")
        elif member == ctx.guild.me:
            raise commands.CommandError("bot_doing")
        elif ctx.guild.me.top_role <= member.top_role:
            raise commands.CommandError("BotRoleTooLow")
        elif ctx.author.top_role <= member.top_role and ctx.author != ctx.guild.owner:
            raise commands.CommandError("AuthorRoleTooLow")
        
        
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
        msg.description = f'**{member.name.capitalize()}** has been banned for **{duration}** for `{reason}`'
        self.logger.info(f'[BAN] {member.name} has been banned for {reason} by {ctx.author.name}')
        
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
        self.logger.info(f'[UNMUTE] {member.name} has been unmuted by {ctx.author.name}')
        msg = scemb.copy()
        msg.description = f'{member} has been unmuted.'
        await ctx.send(embed=msg)

    @commands.hybrid_command('unban', help='Unban a user from the server')
    async def unban(self, ctx, member: discord.User):
        user = await self.bot.fetch_user(member.id)
        if user is None:
            msg = eremb.copy()
            msg.description = 'User not found.'
            await ctx.reply(embed=msg)
            return

        try:
            await ctx.guild.fetch_ban(user)
        except discord.NotFound:
            msg = eremb.copy()
            msg.description = f'**{user.name.capitalize()}** is not banned.'
            await ctx.reply(embed=msg)
            return

        await ctx.guild.unban(user)
        self.logger.info(f'[UNBAN] {user.name} has been unbanned by **{ctx.author.name}')
        
        msg = scemb.copy()
        msg.description = f'**{user.capitalize()}** has been unbanned.'
        await ctx.reply(embed=msg)
    
async def setup(bot):
    await bot.add_cog(moderation(bot))
