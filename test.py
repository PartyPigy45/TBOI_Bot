# This example requires the 'message_content' intent.

import discord
import os
from dotenv import load_dotenv, dotenv_values 

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$optoins'):
        await message.channel.send('Options have appered in the bacement')


# loading variables from .env file
load_dotenv() 

client.run(os.getenv("BOT_TOKEN"))
