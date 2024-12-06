import discord
import random
from discord.ext import commands

chistes = [
    "¿Por qué los pájaros no usan Facebook? Porque ya tienen Twitter.",
    "¿Qué hace una abeja en el gimnasio? Zum-ba.",
    "¿Por qué los esqueletos no pelean entre ellos? Porque no tienen agallas.",
    "¿Cómo se despiden los químicos? Ácido un placer.",
    "¿Qué le dice una iguana a su hermana gemela? Iguanita."
]
    
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/b ', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hola(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def jaja(ctx, name, count_heh = 5):
    await ctx.send(name + "se cayó al piso" + "jajaja" * count_heh)
    
@bot.command()
async def registrar_evento(ctx, nombre_evento: str, fecha: str, hora: str, ubicacion: str):
    await ctx.send(f'¡Evento registrado!\nNombre del evento: {nombre_evento}\nFecha: {fecha}\nHora: {hora}\nUbicación: {ubicacion}')
    
@bot.command()
async def chiste(ctx):
    chiste_aleatorio = random.choice(chistes)
    await ctx.send(chiste_aleatorio)
