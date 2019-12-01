import discord
from discord.ext import commands, tasks
import json
import utils
import config
from time import time

class moderation_tasks(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @tasks.loop(minutes=15)
    async def checkMuteTimer(self):
        with open("records.json") as f:
            data = json.load(f)
        for user in data:
            if user['timer'] < time() and user['isMute'] == 1:
                user['timer'] = 0
                user['isMute'] = 0
                user['muteReason'] = "None"
                guild = self.bot.get_guild(513196299613503488) # Hard coded zer0 server id
                mutedRole = discord.utils.get(guild.roles, id = config.role_dict.get("muted"))
                member = guild.get_member(user['id'])
                await member.remove_roles(mutedRole)
                

def setup(bot):
    bot.add_cog(moderation_tasks(bot))
