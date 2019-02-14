import discord
from discord.ext import commands
import random

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
    # if (message.author.id == "247810647667113996"):
    #     await client.send_message(message.channel, "https://www.skiddle.com/artists/basshunter-123458771/")
    #     return

    # random switch statement
    ranNo = random.randint(1,4)
    if ranNo == 1:
        await client.send_message(message.channel, "Case 1")
    elif ranNo == 2:
        await client.send_message(message.channel, "Case 2")
    elif ranNo == 3:
        await client.send_message(message.channel, "Case 3")
    elif ranNo == 4:
        await client.send_message(message.channel, "Case 4")

    # check if a command should also be executed as on_message has priority
    await client.process_commands(message)

@client.command()
async def ping():
    await client.say("Pong!")

# @client.command()
# async def randomMessage(args):
#     print(args[1])
#     switcher = {
#         1: "Hi 1",
#         2: "Hii 2",
#         3: "Hiii 3"
#     }
#     print switcher.get(args[1], "Invalid month")

@client.command(pass_context = True)
async def echo(msg, *args):
    await client.delete_message(msg.message)
    output = ""
    for word in args:
        output += word
        output += " "
    await client.say(output)

client.run(TOKEN)
