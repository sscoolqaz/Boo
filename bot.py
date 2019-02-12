import discord
from discord.ext import commands

TOKEN = "NTQ1MDExNDU0MTYwNjY2NjM0.D0Tc_g.y-9swzzfUUwueJQVZnRSosC7ZhQ"

client = commands.Bot(command_prefix = ".")

@client.event
async def on_ready():
    print("Bot is ready...")

@client.event
async def on_message(message):
    author = message.author
    content = message.content
    print(`{}: {}`.format(author, content))

client.run(TOKEN)
