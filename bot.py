import discord
from discord.ext import commands
import random

bot = commands.Bot(command_prefix = ">")


@bot.event
async def on_ready():
    print(f"{bot.user.name} - {bot.user.id}")
    print(discord.__version__)
    print("Ready...")


@bot.command()
async def repeat(ctx, *, word): #
    """
    Repeats whatever you type in
    """
    await ctx.send(word)


@bot.command()
async def stop(ctx):
    await bot.logout()


bot.run("NTQ0NjYyMTU3NDQzMjAzMDk1.D3CYwA.RL9KFnZyxqN4HDxQJzHAN7iGBxA")
