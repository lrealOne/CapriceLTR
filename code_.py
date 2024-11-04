"""
Caprice LTR

O bot está em desenvolvimento, feito para estudo e voltado para dar suporte a pessoas que se sintam sozinhas.

Versões e atualizações:


"""


import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import time

intents = discord.Intents.default()
intents.message_content = True;

bot = commands.Bot(command_prefix="/", intents=intents)

load_dotenv()
discordToken = os.environ.get("TOKEN_CapriceLTR")


options = {
    "1": "Você escolheu Motivação!",
    "2": "Você escolheu História de superação!",
    "3": "Você escolheu Mensagem carinhosa!",
    "4": "Você escolheu Elogio!"
}

@bot.event
async def on_ready():
    print("Running...")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if message.content.startswith('/ajuda'):
        await message.channel.send(
            "Olá :D!! Espero que esteja bem. Do que precisa?\n"
            "1 - Motivação\n"
            "2 - História de superação\n"
            "3 - Mensagem carinhosa\n"
            "4 - Elogio"
        )
        return

    if message.content in options:
        await message.channel.send(options[message.content])
        return
    else:
        await message.channel.send('Não entendi....')

    
        
bot.run(discordToken)