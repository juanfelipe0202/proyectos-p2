import discord
from logic import genaradorpassword

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif message.content.startswith('hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('bye'):
        await message.channel.send("\U0001f642")
    elif message.content.startswith('como_estas'):
        await message.channel.send("Bien")
    elif message.content.startswith('pass'):
        await message.channel.send(genaradorpassword(10))
    else:
        await message.channel.send(message.content)
