import discord
from discord.ext import commands
import json

# VARIABLES
# ghost_id = ""
# plugs_id = "146737110974595073"
# admin_role = ""
# approved_users = [ghost_id, plugs_id]
# approved_roles = [admin_role]
# general_id = "547907603494338610"

class fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def ping(self, ctx):
        allowed_role = ["Red Panda Enthusiast", "Administrator"] # role allowed to use this command
        user_roles = [y.name for y in ctx.message.author.roles] # get the users roles
        if bool(set(user_roles) & set(allowed_role)): # check the user has the required role
            await ctx.send('Pong!')
            # ms = (t.timestamp-ctx.message.timestamp).total_seconds() * 1000
            # await self.bot.edit_message(t, new_content='Pong! Took: {}ms'.format(int(ms)))
        else:
            await self.bot.say("You do not have permission to use this command")


def setup(bot):
    bot.add_cog(fun(bot))
