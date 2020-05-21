import discord
from discord.ext import commands
import random
import time
import asyncio


description = '''All the daily info you need!'''

bot = commands.Bot('!', description=description)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="The Weather Report"))
    print('The bot is active')

@bot.command() #This command prints the ping of the bot
async def ping(ctx):
    ping = round(bot.latency*1000)
    await ctx.send(f"The ping of this bot is {ping} ms")



bot.run(token)