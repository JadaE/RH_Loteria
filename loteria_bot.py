# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 16:32:47 2020

@author: Joseph
"""
# loteria_bot.py

import discord

TOKEN = 'NjkyNDc5MzY4MzUzNTQ2MzMy.XnvJEQ.bm6lTMTMDB5s9t5m5E1Hf1iUG8g'
SERVER = '687850748389752843'

client = discord.Client()

list = []
#need a counter for boards plus a list for boards

@client.event
async def on_message(message):
        
    if message.author == client.user:
        return
    
    if message.content.lower() == 'board me':
        if message.author in list:
            response = 'Hey! You already got one, silly goose!'
            await message.author.send(response)
        else:
            response = "Here you go!"
            await message.author.send(response)
            await client.get_channel(692535391357632512).send(response)
            #await client.get_channel(692535391357632512).send(file=discord.File(file)) importing file
            await client.get_channel(692535391357632512).send(message.author)
            list.append(message.author)
        

client.run(TOKEN)