import discord
from discord.ext import commands


import random
import time
import asyncio
import requests, json 
import re

from newsapi import NewsApiClient



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
    complete_url = base_url + "appid=" + owm_key + "&q=" + City
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


    bbc = Newscatcher(website = 'https://www.bbc.com')
    results = bbc.get_news()
    bbcArticles = results['articles']
    aSummary = bbcArticles[0]['summary']
    aTitle = bbcArticles[0]['title']

    embed = discord.Embed(
        title= str("News"),
        color= 0xADD8E6)
    embed.set_author(
        name="BBC", url="https://www.bbc.com/news")
    embed.add_field(
        name=str(bbcArticles[0]['title']),
        value=str(bbcArticles[0]['summary']),
        inline=False)
    embed.add_field(
        name=str(bbcArticles[1]['title']),
        value=str(bbcArticles[1]['summary']),
        inline=False)
    embed.add_field(
        name=str(bbcArticles[2]['title']),
        value=str(bbcArticles[2]['summary']),
        inline=False)
    embed.add_field(
        name=str(bbcArticles[3]['title']),
        value=str(bbcArticles[3]['summary']),
        inline=False)
    embed.add_field(
        name=str(bbcArticles[4]['title']),
        value=str(bbcArticles[4]['summary']),
        inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def news(ctx, *keyword):

    if keyword:
        keyword = str(keyword)
        keyword = re.sub(r'[()]', '', keyword)
        keyword = keyword.replace("'", "")
        keyword = keyword.replace(",", "")
        category = ['business', 'entertainment', 'general', 'health', 'science', 'sports', 'technology']

        if keyword in category:
            news = newsapi.get_top_headlines(category = keyword)
            Articles = news['articles']

            embed = discord.Embed(
                title= str(Articles[0]['title']), 
                url = Articles[0]['url'],
                description=str(Articles[0]['description']),
                color= 0xFF0000)
            embed.set_author(
                name= Articles[0]['author'])
            embed.set_thumbnail(url = Articles[0]['urlToImage'])
            await ctx.send(embed=embed)

            embed = discord.Embed(
                title= str(Articles[1]['title']), 
                url = Articles[1]['url'],
                description=str(Articles[1]['description']),
                color= 0xFF0000)
            embed.set_author(
                name= Articles[1]['author'])
            embed.set_thumbnail(url = Articles[1]['urlToImage'])
            await ctx.send(embed=embed)

            embed = discord.Embed(
                title= str(Articles[2]['title']), 
                url = Articles[2]['url'],
                description=str(Articles[2]['description']),
                color= 0xFF0000)
            embed.set_author(
                name= Articles[2]['author'])
            embed.set_thumbnail(url = Articles[2]['urlToImage'])
            await ctx.send(embed=embed)

            embed = discord.Embed(
                title= str(Articles[3]['title']), 
                url = Articles[3]['url'],
                description=str(Articles[3]['description']),
                color= 0xFF0000)
            embed.set_author(
                name= Articles[3]['author'])
            embed.set_thumbnail(url = Articles[3]['urlToImage'])
            await ctx.send(embed=embed)

            embed = discord.Embed(
                title= str(Articles[4]['title']), 
                url = Articles[4]['url'],
                description=str(Articles[4]['description']),
                color= 0xFF0000)
            embed.set_author(
                name= Articles[4]['author'])
            embed.set_thumbnail(url = Articles[4]['urlToImage'])
            await ctx.send(embed=embed)
        else: 
            news = newsapi.get_everything(q = keyword, 
                                        sort_by='relevancy')
            Articles = news['articles']

            embed = discord.Embed(
                title= str(Articles[0]['title']), 
                url = Articles[0]['url'],
                description=str(Articles[0]['description']),
                color= 0xFF0000)
            embed.set_author(
                name= Articles[0]['author'])
            embed.set_thumbnail(url = Articles[0]['urlToImage'])
            await ctx.send(embed=embed)

            embed = discord.Embed(
                title= str(Articles[1]['title']), 
                url = Articles[1]['url'],
                description=str(Articles[1]['description']),
                color= 0xFF0000)
            embed.set_author(
                name= Articles[1]['author'])
            embed.set_thumbnail(url = Articles[1]['urlToImage'])
            await ctx.send(embed=embed)

            embed = discord.Embed(
                title= str(Articles[2]['title']), 
                url = Articles[2]['url'],
                description=str(Articles[2]['description']),
                color= 0xFF0000)
            embed.set_author(
                name= Articles[2]['author'])
            embed.set_thumbnail(url = Articles[2]['urlToImage'])
            await ctx.send(embed=embed)

            embed = discord.Embed(
                title= str(Articles[3]['title']), 
                url = Articles[3]['url'],
                description=str(Articles[3]['description']),
                color= 0xFF0000)
            embed.set_author(
                name= Articles[3]['author'])
            embed.set_thumbnail(url = Articles[3]['urlToImage'])
            await ctx.send(embed=embed)

            embed = discord.Embed(
                title= str(Articles[4]['title']), 
                url = Articles[4]['url'],
                description=str(Articles[4]['description']),
                color= 0xFF0000)
            embed.set_author(
                name= Articles[4]['author'])
            embed.set_thumbnail(url = Articles[4]['urlToImage'])
            await ctx.send(embed=embed)

    else:
        sources = 'bbc-news, al-jazeera-english'
        topHeadlines = newsapi.get_top_headlines(sources= sources)
        Articles = topHeadlines['articles']

        embed = discord.Embed(
            title= str(Articles[0]['title']), 
            url = Articles[0]['url'],
            description=str(Articles[0]['description']),
            color= 0xFF0000)
        embed.set_author(
            name= Articles[0]['author'])
        embed.set_thumbnail(url = Articles[0]['urlToImage'])
        await ctx.send(embed=embed)

        embed = discord.Embed(
            title= str(Articles[1]['title']), 
            url = Articles[1]['url'],
            description=str(Articles[1]['description']),
            color= 0xFF0000)
        embed.set_author(
            name= Articles[1]['author'])
        embed.set_thumbnail(url = Articles[1]['urlToImage'])
        await ctx.send(embed=embed)

        embed = discord.Embed(
            title= str(Articles[2]['title']), 
            url = Articles[2]['url'],
            description=str(Articles[2]['description']),
            color= 0xFF0000)
        embed.set_author(
            name= Articles[2]['author'])
        embed.set_thumbnail(url = Articles[2]['urlToImage'])
        await ctx.send(embed=embed)

        embed = discord.Embed(
            title= str(Articles[3]['title']), 
            url = Articles[3]['url'],
            description=str(Articles[3]['description']),
            color= 0xFF0000)
        embed.set_author(
            name= Articles[3]['author'])
        embed.set_thumbnail(url = Articles[3]['urlToImage'])
        await ctx.send(embed=embed)

        embed = discord.Embed(
            title= str(Articles[4]['title']), 
            url = Articles[4]['url'],
            description=str(Articles[4]['description']),
            color= 0xFF0000)
        embed.set_author(
            name= Articles[4]['author'])
        embed.set_thumbnail(url = Articles[4]['urlToImage'])
        await ctx.send(embed=embed)

bot.run(token)
