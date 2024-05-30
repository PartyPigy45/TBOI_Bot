# This example requires the 'message_content' intent.

import discord
import os
import logging
from random import choice 
from dotenv import load_dotenv, dotenv_values 

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

def is_mach(file:str, msgs:str) -> bool:
    logging.info(f'{file[:-4].lower()} in {msgs.lower().replace(" ", "")}') if file[:-4].lower() in msgs.lower().replace(" ", "") else ""
    return file[:-4].lower() in msgs.lower().replace(" ", "")

@client.event
async def on_ready():
    logging.info(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    mach_list = [x for x in os.listdir("./images") if is_mach(x,message.content)]

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

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.DEBUG,
        filename="info.log")

    client.run(os.getenv("BOT_TOKEN"))
