import discord
from discord.ext import commands
import json
import utils


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def ping(self, ctx):
        if utils.check_roles(["Red Panda Enthusiast", "Administrator"], [y.name for y in ctx.message.author.roles]): # check the user has the required role
            await ctx.send('Pong!')
            # ms = (t.timestamp-ctx.message.timestamp).total_seconds() * 1000
            # await self.bot.edit_message(t, new_content='Pong! Took: {}ms'.format(int(ms)))
        else:
            await ctx.send("You do not have permission to use this command")


    # copies the senders message
    @commands.command(hidden = True)
    async def echo(self, ctx, *, words):
        """
        Repeats whatever you type in
        """
        if utils.check_roles(["Red Panda Enthusiast", "Administrator"], [y.name for y in ctx.message.author.roles]): # check the user has the required role
            await ctx.message.delete() # delete the original message
            await ctx.send(words) # send the message
        else:
            await ctx.send("You do not have permission to use this command")


    # copies the senders message
    @commands.command(hidden = True)
    async def gen_echo(self, ctx, *, words):
        if utils.check_roles(["Red Panda Enthusiast", "Administrator"], [y.name for y in ctx.message.author.roles]): # check the user has the required role
            await ctx.message.delete() # delete the original message
            await self.bot.get_channel(554062734950531094).send(words) # send the message
        else:
            await ctx.send("You do not have permission to use this command")


def setup(bot):
    bot.add_cog(Fun(bot))
