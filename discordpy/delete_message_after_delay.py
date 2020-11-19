from discord.ext import commands, tasks
import discord
import re
import json 
import time 
import random
import asyncio
import os
import datetime

from tokens import dev

client = commands.Bot('!')

'''
@tasks.loop() can be changed to seconds, minutes, hours
https://discordpy.readthedocs.io/en/latest/ext/tasks/
'''

@client.command()
async def autodel(ctx):
    print('in autodel')
    message = await ctx.send('hello')
    message2 = await ctx.send('hello2')
    await asyncio.sleep(3)
    await discord.Message.delete(message)
    await discord.Message.delete(message2)
    print('message deleted ')

client.run(dev)