import discord
from discord.ext import commands


import random
import time
import asyncio
import requests, json 
import re

from google_currency import convert as conv

from newsapi import NewsApiClient


base_url = "http://api.openweathermap.org/data/2.5/weather?"

description = '''All the daily info you need!'''

bot = commands.Bot('!!', description=description)

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
        current_temperature = str(round(y["temp"]-273.15,2))
        current_pressure = y["pressure"] 
        current_humidiy = y["humidity"]
        min_temp = format(round(y["temp_min"]-273.15,2))
        max_temp = format(round(y["temp_max"]-273.15,2))
        feels_like = format(round(y["feels_like"]-273.15,2))
        z = x["weather"] 
        icon = z[0]["icon"]
        weather_description = z[0]["description"] 
        weather_main = z[0]["main"] 
        w = x["wind"]
        wind = w["speed"]
        wind_deg = w["deg"]

        def faren(tem):
          tem = float(tem)
          return str(round(tem*9/5+32,2))

        def degDir(d):
          dirs = ['N', 'N/NE', 'NE', 'E/NE', 'E', 'E/SE', 'SE', 'S/SE', 'S', 'S/SW', 'SW', 'W/SW', 'W', 'W/NW', 'NW', 'N/NW']
          ix = round(d / (360. / len(dirs)))
          return dirs[ix % len(dirs)]


        embed = discord.Embed(
            title= str(City),
            color= 0xADD8E6)
        embed.set_author(
            name="OpenWeatherMap", url="https://www.openweathermap.org")
        embed.set_thumbnail(url = str("http://openweathermap.org/img/w/" + icon + ".png"))

        embed.add_field(
            name="Temperature",
            value= current_temperature + "°C / " + str(faren(current_temperature)) + "°F",
            inline=True)
        
        embed.add_field(
            name="Feels Like",
            value=feels_like + "°C / " + str(faren(feels_like)) + "°F",
            inline=True)

        embed.add_field(
            name="Wind",
            value=str(wind) + " mph " + str(degDir(wind_deg)),inline=True)

        embed.add_field(
            name="Minimum Temperature",
            value=min_temp + "°C / " + str(faren(min_temp)) + "°F",
            inline=True)
        
        embed.add_field(
            name="Maximum Temperature",
            value=max_temp + "°C / " + str(faren(max_temp)) + "°F",
            inline=True)
            
        embed.add_field(
            name="Humidity", value= str(current_humidiy) + "%", inline=True)

        embed.add_field(
            name="Atmospheric Pressure",
            value= str(current_pressure) + " hPa",
            inline=True)
          
        embed.add_field(
            name="Description",
            value=weather_main + ": " + weather_description,inline=True)

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
    sources = 'bbc-news, al-jazeera-english, bbc-sport, bleacher-report, cnn, espn, fox-news, google-news, independent, national-geographic, reuters'
    if keyword:
        keyword = str(keyword)
        keyword = re.sub(r'[()]', '', keyword)
        keyword = keyword.replace("'", "")
        keyword = keyword.replace(",", "")
        category = ['business', 'entertainment', 'general', 'health', 'science', 'sports', 'technology']

        if keyword in category:
            news = newsapi.get_top_headlines(category = keyword, language='en', country= 'us, gb')
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
                                        sort_by='relevancy', sources= sources)
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

@bot.command()
async def convert(ctx, *currLoad):
    currLoad = str(currLoad)
    currLoad = re.sub(r'[()]', '', currLoad)
    currLoad = currLoad.replace("'", "")
    currLoad = currLoad.replace(",", "")
    currVar = currLoad.split()

    if len(currVar) == 3:
        currConv = conv(currVar[1], currVar[2], int(currVar[0]))

        currConv = json.loads(currConv)
        sendSyx = str(currVar[0]) + ' ' + currConv['from'] + " is equivalent to " + currConv['amount'] + ' ' + currConv['to']
        await ctx.send(sendSyx)


    elif len(currVar) ==4:
        currConv= conv(currVar[1], currVar[3], int(currVar[0]))

        currConv = json.loads(currConv)
        sendSyx = str(currVar[0]) + ' ' + currConv['from'] + " is equivalent to " + currConv['amount'] + ' ' + currConv['to']
        await ctx.send(sendSyx)

    else:
        await ctx.send("Invalid Syntax")


@bot.command()
async def help(ctx):
  embed = discord.Embed(
    title= "OptimaBot Commands",
    color= 0000000)
  embed.set_author( name= "By SlumberousCarp2#7916")

  embed.add_field(
    name="News",
    value= '`!!news` \n This shows you the top 5 headlines of the hour \n `!!news <category>` \n This commands shows you the top headlines in the category of your choice. The Categories are: `business`, `entertainment`, `general`, `health`, `science`, `sports`, and `technology`. \n `!!news <keyword>` \n This command shows you the top 5 headlines for any given keyword of your choice',
    inline=False)

  embed.add_field(
    name="Weather",
    value= '`!!weather <City>` \n This command tells you the weather in the a cetain city',
    inline=False)

  embed.add_field(
    name="Currency",
    value= '`!!convert <amount> <oldcurrency> <newcurrency>` \n This command helps you convert between currencies',
    inline=False)

  embed.add_field(
    name="Ping",
    value= '`!!ping` \n This shows the connection ping between the discord server and the bot host',
    inline=False)
  await ctx.send(embed=embed)

bot.run(token)




