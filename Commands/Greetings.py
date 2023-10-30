import discord
from discord.ext import commands
import traceback
import random
from embed import color_Embed

# ***************************************
# **    Lista de Saludos Aleatorios    **
# ***************************************
saludos = [
    "¡Hola, {}! ¿Cómo estás hoy? 😊",
    "¡Buenos días, {}! Espero que tengas un gran día. ☀️",
    "¡Hola, {}! Estoy feliz de verte aquí. 🎉",
    "Es un placer saludarte, {}. 👋",
    "¡Hola, {}! ¿Cómo puedo ayudarte hoy? 🤝",
    "¡Buenas tardes, {}! ¿Cómo ha sido tu día hasta ahora? 🌆",
    "¡Hola, {}! Siempre es un placer verte por aquí. 😄",
    "¡Hola, {}! ¿Qué novedades tienes para compartir? 🗞️",
    "¡Hola, {}! ¿En qué puedo ayudarte hoy? 🆘",
    "¡Buenos días, {}! Espero que tengas un día maravilloso. 🌞",
    "¡Hola, {}! Estoy aquí para ayudarte en lo que necesites. 💼",
    "¡Hola, {}! ¿Cómo puedo hacer tu día mejor? 🌈",
    "¡Hola, {}! Tu presencia siempre alegra este lugar. 🌟",
    "¡Buenas tardes, {}! ¿Qué tal ha ido tu día hasta ahora? 🌇",
    "¡Hola, {}! ¿En qué puedo asistirte hoy? 🤗",
    "¡Hola, {}! Espero que estés teniendo un día genial. 🎈",
    "¡Hola, {}! ¿Qué aventuras te depara el día de hoy? 🌠",
    "¡Hola, {}! ¿Listo para enfrentar el día con energía? 💪",
    "¡Hola, {}! ¿Qué proyectos emocionantes tienes en mente? 🚀",
    "¡Buenos días, {}! Comencemos el día con entusiasmo. 🌄",
    "¡Hola, {}! ¿Qué objetivos te propones alcanzar hoy? 🎯",
    "¡Hola, {}! ¿Listo para escribir una nueva página en tu historia? 📖",
    "¡Hola, {}! ¿Qué te trae por aquí hoy? 🌼",
    "¡Hola, {}! La alegría de verte es indescriptible. 😄",
    "¡Buenas, {}! ¿En qué puedo asistirte en este momento? 🌟"
]

# ****************************************************
# **    Comando para Obtener un Saludo Aleatorio    **
# ****************************************************
def Saludar(bot):
    @bot.command()
    async def hola(ctx):
        try:
            # Obtener el color correspondiente al comando
            color_tuple = color_Embed["saludar"]
            color = discord.Colour.from_rgb(*color_tuple)

            # Seleccionar un saludo aleatorio de la lista y mencionar al autor
            saludo_aleatorio = random.choice(saludos).format(ctx.author.mention)

            # Crear un objeto Embed para la respuesta
            embed = discord.Embed(
                title="Saludo Aleatorio",
                description=saludo_aleatorio,
                color=color
            )

            # Responder al mensaje con el saludo mencionando al usuario
            await ctx.send(embed=embed)
        except Exception as e:
            # Mostrando un error en rojo
            color_error = discord.Colour.from_rgb(255, 0, 0)
            embed_error = discord.Embed(title="Error", color=color_error)
            embed_error.add_field(name="Ocurrió un error", value=str(e), inline=False)
            await ctx.send(embed=embed_error)
