import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os
import webserver

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='+', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} is ready to work')

@bot.event
async def on_member_join(member):
    await member.send(f'Welcome to the server {member.name}')
    await member.channel.send('WElcomE')
    
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if "shit" in message.content.lower():
        await message.delete()
        await message.channel.send(f'{message.author.mention} you message is incorrect please do not say that')

    await bot.process_commands(message)

webserver.keep_alive()
bot.run(token, log_handler=handler, log_level=logging.DEBUG)