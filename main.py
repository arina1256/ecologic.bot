
import random
from random import choice
import discord
from discord.ext import commands
import os
import requests


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)



@bot.command()
async def location(ctx):
    with open('ecologic.bot/ecopoints.png', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
@bot.command('eco')
async def eco(ctx):
    eco_str = '''Экология - это наука, которая изучает взаимодействие живых организмов между собой и с окружающей средой. 
    Цель экологии - сохранение биологического видообразия и поддержание экосистем в равновесном состоянии. 
    Мы должны заботиться о природе и экологически устойчивом развитии, чтобы не нарушать баланс в природе.
    '''
    await ctx.send(eco_str)
@bot.command('hello')
async def hello(ctx):
    hello_str = '''Привет!Я - ecobot. Ты можешь написать '$help', чтобы узнать какие команды у меня есть.
    '''
    await ctx.send(hello_str)
@bot.command('helpMe')
async def helpMe(ctx):
    helpMe_str = '''
      !hello поздороваться с ботом
      !advice получить совет от бота, чтобы уменьшить количество отходов
      !eco узнать об экологии
      !location узнать местонахождение Экопунктов
    '''
    await ctx.send(helpMe_str)

@bot.command('advice')
async def advice(ctx):
    await ctx.send(random.choice(["откажитесь от лишнего и отдайте эти вещи другим.","Сократите отходы там, где возможно","Используйте вещи повторно","Сортируйте отходы и сдавайте их на переработку","Компостируйте органический мусор","Используйте многоразовую посуду вместо пластиковой","Используйте шопперы вместо пакетов"]))


bot.run('TOKEN')
