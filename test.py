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

    if 'options' in message.content:
        with open("./images/achievement_theresoptions.png", "rb") as fh:
            f = discord.File(fh, filename="./images/achievement_theresoptions.png")
        await message.channel.send(file=f)

# loading variables from .env file
load_dotenv() 

client.run(os.getenv("BOT_TOKEN"))
