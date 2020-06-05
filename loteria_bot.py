# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 16:32:47 2020

@author: Joseph
"""
# loteria_bot.py

import discord
import pickle

TOKEN = '' #redacted
SERVER = ''#redacted

client = discord.Client()

list = []
#need a counter for boards plus a list for boards
try:        
    with open('listfile.data', 'rb') as filehandle:
        # read the data as binary data stream
        list = pickle.load(filehandle)
except IOError:
    print("file not found")

@client.event
async def on_message(message):
        
    if message.author == client.user:
        return
    
    if message.content.lower() == 'board me':
        if str(message.author) in list:
            response = 'Hey! You already got one, silly goose!'
            await message.author.send(response)
        else:
            response = "Here you go!"
            await message.author.send(response)
            # send file to hacker
            await client.get_channel(692535391357632512).send(response + "\n" + str(message.author))
            # send file to log
            list.append(str(message.author))
            with open('listfile.data', 'wb') as filehandle:
                pickle.dump(list, filehandle)
        

client.run(TOKEN)
