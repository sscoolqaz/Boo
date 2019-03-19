import discord
from discord.ext import commands


class Methods(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


# functions in here


def setup(bot):
    bot.add_cog(Methods(bot))
