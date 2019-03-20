import discord
from discord.ext import commands
import random


bot = commands.Bot(command_prefix = ">")
extensions = ["fun"] # list of cogs to call


@bot.event
async def on_ready():
    print(f"{bot.user.name} - {bot.user.id}")
    print(discord.__version__)
    print("Ready...")


# immediately stop the bot
@bot.command() # hidden = True
async def stop(ctx):
    if check_roles(["Red Panda Enthusiast"], [y.name for y in ctx.message.author.roles]): # check the user has the required role
        await bot.logout()
    else:
        await ctx.send("You do not have permission to use this command")


# manually load a cog
@bot.command(hidden = True)
async def load(ctx, extension):
    if check_roles(["Red Panda Enthusiast"], [y.name for y in ctx.message.author.roles]): # check the user has the required role
        try:
            bot.load_extension(extension)
            print(f"Loaded {extension}.\n")
        except Exception as error:
            print(f"{extension} could not be loaded. [{error}]")
    else:
        await ctx.send("You do not have permission to use this command")


# manually unload a cog
@bot.command(hidden = True)
async def unload(ctx, extension):
    if check_roles(["Red Panda Enthusiast"], [y.name for y in ctx.message.author.roles]): # check the user has the required role
        try:
            bot.unload_extension(extension)
            print(f"Unloaded {extension}.\n")
        except Exception as error:
            print(f"{extension} could not be unloaded. [{error}]")
    else:
        await ctx.send("You do not have permission to use this command")


# manually reload a cog
@bot.command(hidden = True)
async def reload(ctx, extension):
    if check_roles(["Red Panda Enthusiast"], [y.name for y in ctx.message.author.roles]): # check the user has the required role
        try:
            bot.reload_extension(extension)
            print(f"Reloaded {extension}.\n")
        except Exception as error:
            print(f"{extension} could not be reloaded. [{error}]")
    else:
        await ctx.send("You do not have permission to use this command")


# check if the user has permission to use this command
def check_roles(allowed_role, author_roles):
    return(bool(set(author_roles) & set(allowed_role)))


if __name__ == '__main__':
    for extension in extensions:
        try:
            bot.load_extension(extension)
            print(f"Loaded cog: {extension}")
        except Exception as error:
            print(f"{extension} could not be loaded. [{error}]")
    bot.run("NTQ0NjYyMTU3NDQzMjAzMDk1.D3CYwA.RL9KFnZyxqN4HDxQJzHAN7iGBxA")
