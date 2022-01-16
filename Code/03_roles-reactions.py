import discord

"""
client = discord.Client()

@client.event
async def on_ready():
    print('Connected!')

client.run('ODg5MTk2NzY0MDk4MzYzNDMy.YUdvBQ.BNSIh4Yb61s_h6mMoVzTJVyF4OU')
"""


class MyRobot(discord.Client):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.target_message_id = 905910178652758027

    async def on_ready(self):
        print('Connected!')

    async def on_raw_reaction_add(self, payload):
        """
        Даёт роль по эмодзи, которую выберит пользователь
        """

        if payload.message_id != self.target_message_id:
            return

        guild = client.get_guild(payload.guild_id)

        if payload.emoji.name == '💯':
            role = discord.utils.get(guild.roles, name='100% guys')
            await payload.member.add_roles(role)
        elif payload.emoji.name == '🐼':
            role = discord.utils.get(guild.roles, name='Panda guys')
            await payload.member.add_roles(role)
        elif payload.emoji.name == '🍴':
            role = discord.utils.get(guild.roles, name='Knife and fork guys')
            await payload.member.add_roles(role)

    async def on_raw_reaction_remove(self, payload):
        """
        Remove a role based on a reaction emoji
        """

        if payload.message_id != self.target_message_id:
            return

        guild = client.get_guild(payload.guild_id)
        member = guild.get_member(payload.user_id)

        if payload.emoji.name == '💯':
            role = discord.utils.get(guild.roles, name='100% guys')
            await member.remove_roles(role)
        elif payload.emoji.name == '🐼':
            role = discord.utils.get(guild.roles, name='Panda guys')
            await member.remove_roles(role)
        elif payload.emoji.name == '🍴':
            role = discord.utils.get(guild.roles, name='Knife and fork guys')
            await member.remove_roles(role)


intents = discord.Intents.default()
intents.members = True

client = MyRobot(intents=intents)

client.run('ODg5MTk2NzY0MDk4MzYzNDMy.YUdvBQ.ptl55T0jP0wJpwZcEjnXK7NDb_0')
