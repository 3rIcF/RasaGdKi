import discord
import requests


from rasa_connection import curl_request
from dotenv import load_dotenv

#Load Discord Bot Token
load_dotenv()
token = 'OTMwODYwMTMzMTY3MjcxOTc2.Yd8BDg.lBLzMTm8JomVUT1_m7w0-pkbr6I'
client = discord.Client()

@client.event
async def on_ready():
	print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

#Wait for a new Message
@client.event
async def on_message(message):
	
	#Verify that the User is not the Bot itself
	
	if message.author != client.user:
		#Use curl_request Function (located in rasa_connection.py)
		answers = curl_request(message.content, str(message.author))

		#Insert all Respons into one String so we can return it into the Discord Channel
		end_response = " \n ".join((answers))

		#Return the message in a Discord Channel
		return await message.channel.send(f'{message.author.mention} ' + end_response)

client.run(token)