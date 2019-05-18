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
            embed = discord.Embed(title=f"-Zer0 Server Community Guidelines-", description=f"""1. No Advertising & Self Promoting of any kind.\n
                2. Spamming is not allowed.\n\n
                3. Do not ask to become staff.\n
                4. No mass mentions.\n
                5. No unicode / blank names.\n
                6. No dangerous & shortened links.\n
                7. Racism & degrading behavior is not acceptable.\n\n
                Channel Rules of Use are in all channel descriptions.""", color=0xaf68c9) # set up embed

            embed.add_field(name = "TO VERIFY USE THE COMMAND", value = f"`/verify`", inline = False) #{self.bot.get_channel(channels.channel_dict["verify"])}
            # embed.add_field(name = f"-Channel Guidelines-", value = f"{self.bot.get_channel('513440916753874965').mention}\nServers Rules and Guidelines.", inline=False)
            # embed.add_field(name = f"\u200b", value = f"{self.bot.get_channel('554120068619829249').mention}\nUse Command ```/verify``` to verify.", inline=False)
            # embed.add_field(name = f"\u200b", value = f"{self.bot.get_channel('513515376022388786').mention}\nAutomatic Roles for Locked Channels.", inline=False)
            # embed.add_field(name = f"\u200b", value = f"{self.bot.get_channel('513441260925747201').mention}\nServer Announcements Channel.", inline=False)
            # embed.add_field(name = f"\u200b", value = f"{self.bot.get_channel('547907603494338610').mention}\nGeneral conversation. Keep memes to a minimum.\nNo bot commands.", inline=False)
            # embed.add_field(name = f"\u200b", value = f"{self.bot.get_channel('513515185617764352').mention}\nMeme Channel & Off topic Conversations not suitable for General.", inline=False)
            # embed.add_field(name = f"\u200b", value = f"{self.bot.get_channel('513495363706159165').mention}\nConversations about Video games.", inline=False)
            # embed.add_field(name = f"\u200b", value = f"{self.bot.get_channel('513515417126305803').mention}\nBot Commands Channel.", inline=False)
            # embed.add_field(name = f"\u200b", value = f"{self.bot.get_channel('554073196077514755').mention} & {self.bot.get_channel('554073266646417408').mention}\nMain Channels for Mudae Game.", inline=False)
            # embed.add_field(name = f"\u200b", value = f"{self.bot.get_channel('513495341291536385').mention}\nMain channel for talking about anime.", inline=False)
            # embed.add_field(name = f"\u200b", value = f"{self.bot.get_channel('554075464088682507').mention}\nTalk about Currently airing & Recently aired anime.", inline=False)
            # embed.add_field(name = f"\u200b", value = f"{self.bot.get_channel('513515256010768384').mention}\nShare Art.", inline=False)
            # embed.add_field(name = f"\u200b", value = f"{self.bot.get_channel('530632404717535242').mention}\nClaim a Waifu or Husbondo 1 per user.", inline=False)
            # embed.add_field(name = f"\u200b", value = f"{self.bot.get_channel('550909941469282304').mention}\nRequest a Waifu or Husbondo.\nMust Provide There name and a Image.", inline=False)
            # embed.add_field(name = f"\u200b", value = f"{self.bot.get_channel('513515703354261513').mention}\nGeneral Hentai Channel.\nImage Drops Only. No Conversations.\nNo Loli , Furry , Gore.", inline=False)
            # embed.add_field(name = f"\u200b", value = f"{self.bot.get_channel('513515766910418945').mention}\nConversations on NSFW Topics.", inline=False)
            # embed.add_field(name = f"\u200b", value = f"{self.bot.get_channel('550923952126427156').mention}\nShare Direct Links to Hentai Mangas\nAdd a flag reaction under the image for it's Language.\nNo conversations.", inline=False)
            # embed.add_field(name = f"\u200b", value = f"{self.bot.get_channel('555275664224157698').mention}\nNSFW Cosplay.", inline=False)
            # embed.add_field(name = f"\u200b", value = f"{self.bot.get_channel('555275959222272002').mention}\n\n\u200b", inline=False)
            embed.add_field(name = f"Invite Link", value = f"https://discord.gg/wjf9suT", inline=False)
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
                Lewd 🥝\n
                Spoilers 🍉\n""", inline=False)
            channel_roles = await channel.send(embed=embed1)
            # add the emojis to react with
            await channel_roles.add_reaction("🍌")
            await channel_roles.add_reaction("🍑")
            await channel_roles.add_reaction("🍊")
            await channel_roles.add_reaction("🍎")
            await channel_roles.add_reaction("🥝")
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
