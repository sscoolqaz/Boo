import discord
from discord.ext import commands
import utils
import channels


class update(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(hidden = True)
    async def update_rules(self, ctx):
        if utils.check_roles(["Administrator"], [y.name for y in ctx.message.author.roles]): # check the user has the required role
            # update the rules channel with any updates
            lewd_role = ctx.guild.get_role(588951733980495902)
            embed = discord.Embed(title=f"-Zer0 Server Community Guidelines-", description=f"""1. No Advertising & Self Promoting of any kind.\n
                2. Spamming is not allowed.\n
                3. Do not ask to become staff.\n
                4. No mass mentions.\n
                5. No unicode / blank names.\n
                6. No dangerous & shortened links.\n
                7. Racism & degrading behavior is not acceptable.\n\n
                Channel Rules of Use are in all channel descriptions.""", color=0xaf68c9) # set up embed
            embed.add_field(name = "TO VERIFY USE THE COMMAND", value = f"`/verify`\nThe NSFW Channels are Locked to the {lewd_role.mention} Role, to get this role please contact a active administrator.", inline = False)
            await ctx.send(embed=embed)
        else:
            await ctx.send("You do not have permission to use this command")


    @commands.command(pass_context = True, hidden = True)
    async def update_roles(self, ctx):
        if utils.check_roles(["Administrator"], [y.name for y in ctx.message.author.roles]): # check the user has the required role
            # delete existing messages
            channel = self.bot.get_channel(channels.channel_dict["auto_role"]) # get the channel to clear the messages from
            i = 0
            async for message in channel.history():
                if i < (2):
                    i += 1
                    await message.delete()
            print("Roles channel cleared\n")

            # update the roles channel for autoroles
            embed1 = discord.Embed(title=f"Roles!", description=f"React to obtain the following roles:", color=0xaf68c9) # set up embed
            embed1.add_field(name = f"\u200b", value = f"""Sub Freak 🍌\n
                Dub Peasant🍑\n
                Seasonal 🍊\n
                Roulette 🍎\n
                Spoilers 🍉\n""", inline=False)
            channel_roles = await channel.send(embed=embed1)
            # add the emojis to react with
            await channel_roles.add_reaction("🍌")
            await channel_roles.add_reaction("🍑")
            await channel_roles.add_reaction("🍊")
            await channel_roles.add_reaction("🍎")
            await channel_roles.add_reaction("🍉")

            # coloured roles
            embed2 = discord.Embed(title=f"Roles!", description=f"React to obtain the following roles:", color=0xaf68c9) # set up embed
            embed2.add_field(name = f"\u200b", value = f"""Blue 💦\n
                Black 🎱\n
                Yellow 💛\n
                Pink 🐷\n
                Red 🔴\n
                White ⚪\n
                Orange 🔶\n
                Green 💚\n
                Purple 💜\n""", inline=False)
            channel_roles = await channel.send(embed=embed2)
            # add the emojis to react with
            await channel_roles.add_reaction("💦")
            await channel_roles.add_reaction("🎱")
            await channel_roles.add_reaction("💛")
            await channel_roles.add_reaction("🐷")
            await channel_roles.add_reaction("🔴")
            await channel_roles.add_reaction("⚪")
            await channel_roles.add_reaction("🔶")
            await channel_roles.add_reaction("💚")
            await channel_roles.add_reaction("💜")
        else:
            await ctx.send("You do not have permission to use this command")


#             async def on_ready():
#
# #delete msgs from verify chan
#
#     channel = client.get_channel("567859475365756928")
#     msg=[]
#     async for x in client.logs_from(channel, limit = 100):
#         msg.append(x)
#     await client.delete_messages(msg)
#
# #send verification msg w/ reaction
#
#     await client.send_message(channel, "**Verify you are human**")
#     verifymsg2 = await client.send_message(channel, "React with ✅ to gain access to Hard Chats.")
#     await client.add_reaction(verifymsg2, "✅")
#
#
# @client.event
# async def on_reaction_add(reaction, user):
#     channel = client.get_channel('567859475365756928')
#     if reaction.message.channel.id != channel:
#         return
#     else:
#         if reaction.emoji == "✅":
#             unverified = discord.utils.get(user.server.roles, id="567859230661541927")
#             verified = discord.utils.get(user.server.roles, id="567876192229785610")
#             await client.remove_roles(user, unverified)
#             await client.add_roles(user, verified)


def setup(bot):
    bot.add_cog(update(bot))
