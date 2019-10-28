import discord
from discord.ext import commands
import utils
import config
import logging

logging.basicConfig(level=logging.INFO)

class Logs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # deletes messages containing specific words
    @commands.Cog.listener()
    async def on_raw_message_delete(self, payload):
        try:
            # message is cached
            print(f"Message content:\n{payload.cached_message.content}")
        except:
            # message is too old
            print(f"Message content: NADA")


def setup(bot):
    bot.add_cog(Logs(bot))
