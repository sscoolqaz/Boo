import discord
from discord.ext import commands

TOKEN = "NTQ1MDExNDU0MTYwNjY2NjM0.D0Tc_g.y-9swzzfUUwueJQVZnRSosC7ZhQ"

client = commands.Bot(command_prefix = ">")

@client.event
async def on_ready():
    print("Bot is ready...")

@client.command()
async def ping():
    await client.say("Pong!")

@client.command()
async def echo(*args):
    output = ""
    for word in args:
        output += word
        output += " "
    await client.say(output)

client.run(TOKEN)
