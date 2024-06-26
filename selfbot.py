import discord
from discord.ext import commands
import dotenv
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()

bot = commands.Bot(command_prefix=os.getenv('PREFIX'), self_bot=True)
bot._connection.max_messages = 0
bot.remove_command('help')

@bot.event
async def on_ready():
    print(f'Le selfbot est désormais connecté en tant que {bot.user.name}.')
    print(f'Identifiant du compte actuel: {bot.user.id}.')

    while True:
        await asyncio.sleep(30)
        await check_groups()

async def check_groups():
    groups = [channel for channel in bot.private_channels if channel.type == discord.ChannelType.group]

    if groups:
        for group in groups:
            await group.send(f"{os.getenv('MESSAGE_LOCK')}")
            await group.leave()
            print ('Vous avez été supprimer de tout les groupes ou vous êtes présent.')

bot.run(os.getenv('TOKEN'))