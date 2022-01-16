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
async def help(ctx):
    """
    Example: !help
    Shows you what commands you can use
    """
    embed = discord.Embed(
        title='Bot Commands',
        description='This is a help section. All useful commands that you need are here',
        color=discord.Colour.blue()
    )

    embed.set_thumbnail(url='https://miro.medium.com/fit/c/1360/1360/1*ronxBJ6VXPlR-bZ6vkfCug.png')
    embed.add_field(
        name='!help',
        value='List of commands',
        inline=False
    )
    embed.add_field(
        name='!info',
        value="Shows user's statistics",
        inline=False
    )
    embed.add_field(
        name='!hit',
        value='Hit another player',
        inline=False
    )
    embed.add_field(
        name='!ban',
        value='Just ban a user',
        inline=False
    )

    embed.add_field(
        name='!kill',
        value='Become a killer',
        inline=False
    )
    embed.add_field(
        name='!hello',
        value='Say hello to bot',
        inline=False
    )

    await ctx.send(embed=embed)

bot.run('ODg5MTk2NzY0MDk4MzYzNDMy.YUdvBQ.ptl55T0jP0wJpwZcEjnXK7NDb_0')
client.run('ODg5MTk2NzY0MDk4MzYzNDMy.YUdvBQ.ptl55T0jP0wJpwZcEjnXK7NDb_0')
