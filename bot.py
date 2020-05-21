import discord
from discord.ext import commands

import random
import time
import asyncio
import requests, json 



base_url = "http://api.openweathermap.org/data/2.5/weather?"


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

@bot.command()
async def weather(ctx, City: str):
    complete_url = base_url + "appid=" + api_key + "&q=" + City
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404": 
        y = x["main"] 
        current_temperature = y["temp"] 
        current_pressure = y["pressure"] 
        current_humidiy = y["humidity"] 
        z = x["weather"] 
        weather_description = z[0]["description"] 
        await ctx.send(" Temperature (in kelvin unit) = " +
                        str(current_temperature) + 
                        "\n atmospheric pressure (in hPa unit) = " +
                        str(current_pressure) +
                        "\n humidity (in percentage) = " +
                        str(current_humidiy) +
                        "\n description = " +
                        str(weather_description)) 
  
    else: 
        print(" City Not Found ") 

bot.run(token)