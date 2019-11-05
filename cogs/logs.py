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
            embed = discord.Embed(title = "Message Deleted", description = "Message content: " + payload.cached_message.content)
            embed.set_thumbnail(url=payload.cached_message.author.avatar_url)
            embed.set_footer(text=f"Author ID: {payload.cached_message.author.id}")
        except:
            # message is too old
            embed = discord.Embed(title = "Message Deleted")
            embed.set_thumbnail(url=user.avatar_url)
            embed.set_footer(text=f"ID: {user.id}")
        await self.bot.get_channel(config.channel_dict["logs"]).send(embed=embed)


def setup(bot):
    bot.add_cog(Logs(bot))
