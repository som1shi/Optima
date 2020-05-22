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
async def weather(ctx, *, City):
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

        embed = discord.Embed(
            title= str(City),
            color= 0xADD8E6)
        embed.set_author(
            name="OpenWeatherMap", url="https://www.openweathermap.org")
        embed.set_thumbnail(url ="https://cdn2.iconfinder.com/data/icons/weather-flat-14/64/weather02-512.png")
        faren = (current_temperature-273.15)*9/5+32
        embed.add_field(
            name="Temperature",
            value=str(format(round(current_temperature - 273.15, 2))) + "°C" +" / " + str(format(round(faren, 2))) + "°F",
            inline=False)
        embed.add_field(
            name="Atmospheric Pressure",
            value=str(current_pressure) + " hPa",
            inline=False)
        embed.add_field(
            name="Humidity", value=str(current_humidiy) + "%", inline=False)
        embed.add_field(
            name="Description",
            value=str(weather_description),
            inline=False)
        await ctx.send(embed=embed)
    else: 
        await ctx.send("City Not Found ") 

bot.run(token)