import discord
from discord.ext import commands
import random
import logging
import asyncio
import aiohttp

scemb = discord.Embed(
    title='✅ Success ✅',
    colour=discord.Colour.green()
)
eremb = discord.Embed(
    title='❌ Error ❌',
    colour=discord.Colour.red()
)

class fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.logger = logging.getLogger(__name__)
        
    
    @commands.hybrid_command('random', help='Gets random number of your arguments.')
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def random(self, ctx, number_1, number_2):
        if number_1 >= number_2:
            msg = eremb.copy()
            msg.description = 'Number 1 must be less than number 2'
            await ctx.reply(embed=msg)
            return
        
        try:
            number_1 = int(number_1)
            number_2 = int(number_2)
        except ValueError:
            msg = eremb.copy()
            msg.description = 'You need input number!'
            await ctx.reply(embed=msg)
            return

        value = random.randint(number_1, number_2)
        msg = scemb.copy()
        msg.description = f'Your number is **{value}**'
        await ctx.reply(embed=msg)
        
    @commands.hybrid_command('magicball', help='Return random answer to your quesion.')
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def magicball(self, ctx, *, question):
        yes = discord.Embed(
            title='I think...',
            description='Yes! Without reservations.',
            colour=discord.Colour.blurple()
        )
        
        yes1 = discord.Embed(
            title='I think...',
            description='Yes, partially.',
            colour=discord.Colour.blurple()
        )
        
        idk = discord.Embed(
            title='I dont know.',
            description='Ask at another time.',
            colour=discord.Colour.blurple()
        )
        
        no = discord.Embed(
            title='I think...',
            description='No! This is 100% the true answer.',
            colour=discord.Colour.blurple()
        )
        
        no1 = discord.Embed(
            title='I think...',
            description='No, partially.',
            colour=discord.Colour.blurple()
        )
        
        table = [yes, yes1, idk, no, no1]
        answer = table[random.randint(0, len(table) - 1)]
        
        self.logger.info(f'[MAGICBALL] {question} - {answer.description}')
        await ctx.reply(f'Question: `{question}`', embed=answer)
    
    @commands.hybrid_command('quiz', help='Starts a quiz.')
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def quiz(self, ctx):
        questions = {
            "Question: What is the first 10 digits after the decimal point of the number π? (3,..)": "1415926535",
            "Who created this bot?": "Programmduck"
        }
        question, answer = random.choice(list(questions.items()))
        emb = discord.Embed(
            title='❓Quiz',
            description=f"Question: {question}\n(Answer in 10 seconds!)",
            colour=discord.Colour.pink()
        )
        await ctx.reply(embed=emb)
        
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel
        
        try:
            msg = await self.bot.wait_for("message", timeout=10.0, check=check)
            if msg.content.lower() == answer.lower():
                msg = emb.copy()
                msg.description = "✅ Correct!"
                msg.colour = discord.Colour.brand_green()
                await ctx.reply(embed=msg)
            else:
                msg = emb.copy()
                msg.description = f"❌ Incorrect! Correct answer: **{answer}**"
                msg.colour = discord.Colour.brand_red()
                await ctx.reply(embed=msg)
        except asyncio.TimeoutError:
            await ctx.reply("⏰ Time's up!")

    @commands.hybrid_command('avatar', help='Returns player avatar')
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def avatar(self, ctx, user: discord.User = None):
        user = user or ctx.author
        
        msg = discord.Embed()
        msg.set_author(
            name=user.display_name,
            icon_url=user.avatar.url
        )
        msg.set_image(url=user.avatar.url)
        await ctx.reply(embed=msg)
    
    @commands.hybrid_command('userinfo', help='Send user information.')
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def userinfo(self, ctx: commands.Context, member: discord.Member = None):
        member = member or ctx.author
        
        msg = discord.Embed(
            description=f'{member.name.capitalize()}\'s Information',
            colour=discord.Colour.brand_green()
        )
        
        roles = [role for role in member.roles if role != ctx.guild.default_role]
        
        if roles:
            roles_str = "\n".join([role.mention for role in roles[:10]])
            if len(roles) > 10:
                roles_str += f"\n(+{len(roles)-10} more)"

            msg.add_field(name=f"Roles [{len(roles)}]", value=roles_str, inline=True)
        else:
            msg.add_field(name="Roles", value="No roles", inline=True)
        
        created_timestamp = int(member.created_at.timestamp())
        msg.add_field(
            name="Create date", 
            value=f"<t:{created_timestamp}:F> (<t:{created_timestamp}:R>)", 
            inline=True
        )
        
        joined_timestamp = int(member.joined_at.timestamp())
        msg.add_field(
            name='Join date',
            value=f'<t:{joined_timestamp}:F> (<t:{joined_timestamp}:R>)',
            inline=True
        )
        
        msg.set_author(
            name=member.name,
            icon_url=member.avatar.url
        )
        
        msg.set_footer(
            text=f'ID: {member.id}'
        )
        
        await ctx.reply(embed=msg)
    
    
    
async def setup(bot):
    await bot.add_cog(fun(bot))
