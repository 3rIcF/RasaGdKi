import os

import discord



TOKEN = os.getenv('OTMwODYwMTMzMTY3MjcxOTc2.Yd8BDg.lBLzMTm8JomVUT1_m7w0-pkbr6I')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == 'Hallo!':
        await message.channel.send("Hi!")
    elif message.content == 'Wie findest du rasa?':
        await message.channel.send("Ist okay")


client.run('OTMwODYwMTMzMTY3MjcxOTc2.Yd8BDg.lBLzMTm8JomVUT1_m7w0-pkbr6I')