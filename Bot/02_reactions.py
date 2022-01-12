import discord

client = discord.Client()


@client.event
async def on_ready():
    print('Connected!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '!happy' or '!smile' or '!smiley face' '!happy face':
        await message.add_reaction('\U0001F600')
    elif message.content == '!angry' or '!anger' or '!mad':
        await message.add_reaction('\U0001F620')
    elif message.content == '!kiss' or '!kissing' or '!blow a kiss':
        await message.add_reaction('\U0001F618')
    elif message.content == 'sad' or '!sadness' or '!cry' '!crying' or '!tear':
        await message.content.add_reaction('\U0001F622')


@client.event
async def on_message_edit(before, after):
    await before.channel.send(
        f'{before.author} edit a message.\n'
        f'Before: {before.content}\n'
        f'After: {after.content}'
    )


@client.event
async def on_reaction_add(reaction, user):
    await reaction.message.channel.send(f'{user} reacted with {reaction.emoji}')


client.run('TOKEN')
