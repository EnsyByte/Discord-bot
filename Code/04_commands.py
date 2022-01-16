import discord

from discord.ext import commands

client = discord.Client()


@client.event
async def on_ready():
    print('Connected!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return


bot = commands.Bot(command_prefix='!')
bot.remove_command('help')


@bot.command()
async def hello(ctx):
    """
    Example: !hello
    Bot says hello to you
    """
    author = ctx.author
    await ctx.send(f'Hello {author}!')


@bot.command()
async def hit(ctx, per):
    """
    Example: !hit Justin
    Hit one person
    """
    await ctx.send(f'{per} was hit 👊')


@bot.command()
async def kill(ctx, per):
    """
    Example: !kill Loki
    Dirty killer...
    """
    await ctx.send(f'You kill {per} ☠\nNow you are killer and you will suffer forever... \nGoodbye')


@bot.command()
async def round_kick(ctx, *pers):
    """
    Example: !round_kick Boris Josh Elvin Mark
    OMG! You can kick 4 people at once!
    """

    everyone = ', '.join(pers)
    await ctx.send(f'{everyone} was(ere) kicked with roundhouse')


@bot.command()
async def info(ctx):
    """
    Example: !info
    Shows information about server, username and userid
    """

    await ctx.send(ctx.guild)
    await ctx.send(ctx.author)
    await ctx.send(ctx.message.id)


bot.run('TOKEN')
client.run('TOKEN')
