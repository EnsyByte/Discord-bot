import discord

client = discord.Client()


@client.event
async def on_ready():
    print('Connected!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == 'hello':
        await message.channel.send('Greetings tester!')


client.run('ODg5MTk2NzY0MDk4MzYzNDMy.YUdvBQ.ptl55T0jP0wJpwZcEjnXK7NDb_0')
