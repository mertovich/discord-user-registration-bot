import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='')

# MARK - bot commend
@bot.command()
async def ping(ctx):
    await ctx.send('pong')

# MARK - return user avatar
@bot.command()
async def avatar(ctx, member : discord.Member = None):
   await ctx.reply(member.avatar_url)

# MARK - return User registration date
@bot.command()
async def record(ctx, member : discord.Member = None):
    date_format = "%a, %b %d, %Y @ %I:%M %p"
    join = member.created_at.strftime(date_format)
    await ctx.reply(join)
 
# MARK - return the date the user registered on the server
@bot.command()
async def registry(ctx, member : discord.Member = None):
    date_format = "%a, %b %d, %Y @ %I:%M %p"
    join = member.joined_at.strftime(date_format)
    await ctx.reply(join)

# MARK - return Server user registration
@bot.command()
async def userRecord(ctx,*args):
    folder = open('Server_user.txt','a')
    folder.writelines(f'Name : {args[0]} Date of registration to the server : {args[1]} Age : {args[2]} User Id : {args[3]} \n')
    folder.close()
    await ctx.reply(f'Name : {args[0]} Date of registration to the server : {args[1]} Age : {args[2]} User Id : {args[3]}')

# MARK - return get user id
@bot.command()
async def getUserId(ctx,member : discord.user.User = None):
    userId = member.id
    await ctx.reply(userId)

# MARK - Discord bot TOKEN
bot.run('')