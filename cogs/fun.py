import discord
from discord.ext import commands
import json
import utils
import config
import users


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    @commands.has_role(config.role_dict.get("admin"))
    async def ping(self, ctx):
        await ctx.send(f'Pong!')


    @commands.command()
    async def credit(self, ctx):
        bot_name = users.users_dict.get("Booette")
        developer = users.users_dict.get("Plugs")
        embed = discord.Embed(title = "Booette Credits", description = f"<@{bot_name}> was developed by <@{developer}>\n\n" +
                                f"<@{bot_name}>'s Profile image was created by jokanhiyou @ https://twitter.com/jokanhiyou?s=09")
        embed.set_thumbnail(url=(self.bot.get_user(users.users_dict.get("Booette")).avatar_url))
        await ctx.send(embed=embed)


    @commands.command()
    async def uwu(self, ctx, *, message):
        uwufied = Fun.uwufication(message)
        await ctx.message.delete()
        await ctx.send(uwufied)

    @staticmethod
    def uwufication(message):
        # r or l -> w
        message = message.replace("l","w")
        message = message.replace("L","W")
        message = message.replace("r","w")
        message = message.replace("R","W")
        # n+<vowel> -> ny+<voewl>
        message = message.replace("na","nya")
        message = message.replace("NA","NYA")
        message = message.replace("ne","nye")
        message = message.replace("NE","NYE")
        message = message.replace("ni","nyi")
        message = message.replace("NI","NYI")
        message = message.replace("no","nyo")
        message = message.replace("NO","NYO")
        message = message.replace("nu","nyu")
        message = message.replace("NU","NYU")
        # ove -> uv
        message = message.replace("ove","uv")
        message = message.replace("OVE","UV")
        return message


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
    @commands.command(hidden = True)
    @commands.has_role(config.role_dict.get("admin"))
    async def channel_echo(self, ctx, channel: discord.TextChannel, *, words):
        await ctx.message.delete() # delete the original message
        await channel.send(words)


def setup(bot):
    bot.add_cog(Fun(bot))
