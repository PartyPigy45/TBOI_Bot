# This example requires the 'message_content' intent.

import discord
import os
import logging
from random import choice 
from dotenv import load_dotenv, dotenv_values 

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

def match_text_to_image(msg:str) -> list[str]:
    return [x for x in os.listdir("./images") if x[:-4] in msg.split(" ")]

@client.event
async def on_ready():
    logging.info(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    mach_list = match_text_to_image(message.content)

    if message.author == client.user:
        return

    logging.debug(f"Found {mach_list} in {message.author}: '{message.content}' from {message.guild.name}")

    if mach_list == []:
        return

    image = choice(mach_list)
    with open("./images/"+image, "rb") as fh:
        f = discord.File(fh, filename="./images/"+image)
    await message.channel.send(file=f)
    logging.info(f"Sent {image} to {message.guild.name} because {message.author} said '{message.content}'!!!")

# loading variables from .env file
load_dotenv() 

logging.basicConfig(filename="info.log", level=logging.DEBUG)
client.run(os.getenv("BOT_TOKEN"))
