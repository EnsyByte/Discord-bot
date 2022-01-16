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

    if message.content == 'hello':
        await message.channel.send('Greetings tester!')


client.run('TOKEN')
