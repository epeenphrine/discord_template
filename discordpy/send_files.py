from discord.ext import commands, tasks
import discord
import re
import json 
import time 
import random
import asyncio
import os
import datetime

client = commands.Bot('!')
messages = [
    'example',
    'EAXMPEL2'
]
target_channel_id = 663669544321286148 
'''
@tasks.loop() can be changed to seconds, minutes, hours
https://discordpy.readthedocs.io/en/latest/ext/tasks/
'''

@tasks.loop(seconds=1)
async def called_second():
    print('in called once a day')
    message_channel = client.get_channel(target_channel_id)
    print(f"Got channel {message_channel}")
    await message_channel.send(file=discord.File('./ass_naked.png'))

@called_second.before_loop
async def before():
    await client.wait_until_ready()
    print("Finished waiting")

called_second.start()
client.run(dev)