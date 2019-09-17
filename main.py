import discord
from discord.ext import commands
import random
import utils
import config


bot = commands.Bot(command_prefix = "/")
extensions = ["fun","member_mod","chat_mod","update"] # list of cogs to call


@bot.event
async def on_ready():
    print(f"{bot.user.name} - {bot.user.id}")
    print(discord.__version__)
    print("Ready...")


# immediately stop the bot
@bot.command(hidden = True)
@commands.has_role(config.role_dict.get("red_panda"))
async def stop(ctx):
    await bot.logout()


# manually load a cog
@bot.command(hidden = True)
@commands.has_role(config.role_dict.get("red_panda"))
async def load(ctx, extension):
    try:
        bot.load_extension(extension)
        print(f"Loaded {extension}.\n")
    except Exception as error:
        print(f"{extension} could not be loaded. [{error}]")


# manually unload a cog
@bot.command(hidden = True)
@commands.has_role(config.role_dict.get("red_panda"))
async def unload(ctx, extension):
    try:
        bot.unload_extension(extension)
        print(f"Unloaded {extension}.\n")
    except Exception as error:
        print(f"{extension} could not be unloaded. [{error}]")


# manually reload a cog
@bot.command(hidden = True)
@commands.has_role(config.role_dict.get("red_panda"))
async def reload(ctx, extension):
    try:
        bot.reload_extension(extension)
        print(f"Reloaded {extension}.\n")
    except Exception as error:
        print(f"{extension} could not be reloaded. [{error}]")


if __name__ == '__main__':
    for extension in extensions:
        try:
            bot.load_extension(f"cogs.{extension}")
            print(f"Loaded cog: {extension}")
        except Exception as error:
            print(f"{extension} could not be loaded. [{error}]")
    bot.run("NTU0MDYyOTgyMzAxMjIwOTA1.XJ_imQ.2eQyYDsWfzAGQ3RsqlC7IxBtkOM") # real token
