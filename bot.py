import discord
from discord.ext import commands

TOKEN = "NTQ1MDExNDU0MTYwNjY2NjM0.D0Tc_g.y-9swzzfUUwueJQVZnRSosC7ZhQ"

client = commands.Bot(command_prefix = ">")

@client.event
async def on_ready():
    print("Bot is ready...")

@client.event
async def on_message(message):
    if (message.author.bot == True):
        print("The user was a bot")
        return
    if (message.author.id == "276883477318860800"):
        await client.send_message(message.channel, "i see you Aimee OwO")
        return
    if (message.author.id == "247810647667113996"):
        await client.send_message(message.channel, "https://www.skiddle.com/artists/basshunter-123458771/")
        return
    print("A user has send a message")
    await client.process_commands(message)

@client.command()
async def ping():
    await client.say("Pong!")

@client.command(pass_context = True)
async def echo(msg, *args):
    await client.delete_message(msg.message)
    output = ""
    for word in args:
        output += word
        output += " "
    await client.say(output)

client.run(TOKEN)
