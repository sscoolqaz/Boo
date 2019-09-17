import discord
from discord.ext import commands
import json
import utils
import config


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    @commands.has_role(config.role_dict.get("admin"))
    async def ping(self, ctx):
        await ctx.send(f'Pong!')


    # copies the senders message
    @commands.command(hidden = True)
    @commands.has_role(config.role_dict.get("admin"))
    async def echo(self, ctx, *, words):
        """
        Repeats whatever you type in
        """
        await ctx.message.delete() # delete the original message
        await ctx.send(words) # send the message


    # copies the senders message
    # @commands.command(hidden = True)
    # @commands.has_role(config.role_dict.get("admin"))
    # async def gen_echo(self, ctx, *, words):
    #     await ctx.message.delete() # delete the original message
    #     await self.bot.get_channel(547907603494338610).send(words) # send the message


def setup(bot):
    bot.add_cog(Fun(bot))
