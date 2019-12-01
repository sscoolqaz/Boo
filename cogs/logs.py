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
    
    # logs nickname changes
    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        if before.nick != after.nick: # on trigger check if nickname changed
            embed = discord.Embed(title = f"Nickname Changed", description = f"{after.mention}")
            embed.add_field(name = "From:"  , value = f"{before.nick}", inline = False)
            if after.nick is not None: # if the user resets their nickname
                embed.add_field(name = "To:"    , value = f"{after.nick}", inline = False)
            else:
                embed.add_field(name = "To:"    , value = f"{after.display_name}", inline = False)
            embed.set_thumbnail(url=after.avatar_url) # discord.py treats user as member
            embed.set_footer(text=f"User ID: {after.id}")
            await self.bot.get_channel(config.channel_dict.get("logs")).send(embed=embed)

def setup(bot):
    bot.add_cog(Logs(bot))
