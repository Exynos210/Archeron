# This example requires the 'message_content' intent.
import discord
from discord.ext import commands 
import os 

bot_token:str = os.environ.get("TOKEN")

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())  # Prefijo para los comandos

@bot.event
async def on_ready():
    print(f"Conectado como {bot.user.name}")


@bot.command()
async def ping(ctx):
    await ctx.reply("Pong!")


@bot.event
async def on_message(ctx):
    if ctx.author == bot.user:
        return

    if ctx.content.startswith("$hello"):
        await ctx.channel.send("Hello World!")


# bot_token es una variable con env del token original
bot.run(bot_token)
