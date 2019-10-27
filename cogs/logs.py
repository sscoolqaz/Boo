import discord
from discord.ext import commands
import utils
import config
import logging

logging.basicConfig(level=logging.INFO)

class Logs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    

    # @commands.command()
    # @commands.has_role(config.role_dict.get("admin"))
    # async def log(self, ctx):
    #     logging.debug('Pong!')


def setup(bot):
    bot.add_cog(Logs(bot))
