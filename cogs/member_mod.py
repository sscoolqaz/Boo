import discord
from discord.ext import commands
import asyncio
import json
import utils
import channels
import users


class member_moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    # mute all users -not finished-
    @commands.command(hidden = True)
    async def verify(self, ctx):
        if ctx.message.channel.id == channels.channel_dict["verify"]:
            user = ctx.message.author
            add_role = discord.utils.get(ctx.guild.roles, name = "Member")
            await user.add_roles(add_role)
            print(f"The role {add_role} was added to {user}")
            await asyncio.sleep(1)
            rmv_role = discord.utils.get(ctx.guild.roles, name = "Temp")
            await user.remove_roles(rmv_role)
            print(f"The role {rmv_role} was removed from {user}")


    # mute specific user
    @commands.command(hidden = True)
    async def mute(self, ctx, mute_user):
        if utils.check_roles(["Red Panda Enthusiast", "Administrator"], [y.name for y in ctx.message.author.roles]): # check the user has the required role
            user_to_mute = ctx.message.mentions[0] # id of person to mute that was mentioned in command
            mute_role = discord.utils.get(ctx.guild.roles, name = "Muted") # get the role to apply
            await user_to_mute.add_roles(mute_role) # assign the role
            await ctx.send(f"{ctx.message.author} has muted {user_to_mute}")
        else:
            await self.bot.say("You do not have permission to use this command")


    # unmute specific user
    @commands.command(hidden = True)
    async def unmute(self, ctx, unmute_user):
        if utils.check_roles(["Red Panda Enthusiast", "Administrator"], [y.name for y in ctx.message.author.roles]): # check the user has the required role
            user_to_unmute = ctx.message.mentions[0] # id of person to unmute that was mentioned in command
            unmute_role = discord.utils.get(ctx.guild.roles, name = "Muted") # get the role to apply
            await user_to_unmute.remove_roles(unmute_role) # assign the role
            await ctx.send(f"{ctx.message.author} has unmuted {user_to_unmute}")
        else:
            await self.bot.say("You do not have permission to use this command")


    # warn specific user
    @commands.command(hidden = True)
    async def warn(self, ctx, mute_user):
        if utils.check_roles(["Red Panda Enthusiast", "Administrator"], [y.name for y in ctx.message.author.roles]): # check the user has the required role
            message_sender = ctx.message.author # get message author
            warning_name = ctx.message.mentions[0].display_name # name of person to that was warned
            warning_id = ctx.message.mentions[0].id # id of person to that was warned
            # load the json file
            with open('warnings.json') as f:
                data = json.load(f)
            record_exists = False
            # search for the warned user
            for user in data:
                if user['id'] == warning_id: # if the warning id sent mathes the one in the json file
                    # increase the users warning count
                    user['warnings'] += 1
                    print(f"{user['name']} now has {user['warnings']} warnings.")
                    record_exists = True # record has been found
            # if no record exists for the mentioned user
            if record_exists == False:
                data.append( {'id': warning_id, 'name': str(warning_name), 'warnings': 1} )
            # write the edited dict to the json file
            with open('warnings.json', 'w') as f:
                json.dump(data, f, indent = 2)
        else:
            await self.bot.say("You do not have permission to use this command")


    # remove warning from specific user
    @commands.command(hidden = True)
    async def unwarn(self, ctx, mute_user):
        if utils.check_roles(["Red Panda Enthusiast", "Administrator"], [y.name for y in ctx.message.author.roles]): # check the user has the required role
            message_sender = ctx.message.author # get message author
            warning_name = ctx.message.mentions[0].display_name # name of person to that was warned
            warning_id = ctx.message.mentions[0].id # id of person to that was warned
            # load the json file
            with open('warnings.json') as f:
                data = json.load(f)
            # search for the warned user
            for user in data:
                if user['id'] == warning_id: # if the warning id sent mathes the one in the json file
                    # increase the users warning count
                    user['warnings'] = 0
                    print(f"{user['name']} now has {user['warnings']} warnings.")
            # write the edited dict to the json file
            with open('warnings.json', 'w') as f:
                json.dump(data, f, indent = 2)

        else:
            await self.bot.say("You do not have permission to use this command")


    # kick mentioned user
    @commands.command(hidden = True)
    async def kick(self, ctx, ban_user):
        if utils.check_roles(["Red Panda Enthusiast", "Administrator"], [y.name for y in ctx.message.author.roles]): # check the user has the required role
            await kick(ctx.message.mentions[0])


    # ban mentioned user
    @commands.command(hidden = True)
    async def ban(self, ctx, ban_user):
        if utils.check_roles(["Red Panda Enthusiast", "Administrator"], [y.name for y in ctx.message.author.roles]): # check the user has the required role
            await ban(ctx.message.mentions[0])


    # assign roles based on adding a reaction
    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        if user.id == users.users_dict["Booette"]: # don't assign roles for Booette
            return

        if reaction.message.channel.id != channels.channel_dict["auto_role"]:
            return # not in the role channel

        # first message
        elif str(reaction.emoji) == "🍌":
            add_role = discord.utils.get(user.guild.roles, name = "Sub Freak")
            await user.add_roles(add_role)
        elif(str(reaction.emoji) == "🍑"):
            add_role = discord.utils.get(user.guild.roles, name = "Dub Peasant")
            await user.add_roles(add_role)
        elif str(reaction.emoji) == "🍊":
            add_role = discord.utils.get(user.guild.roles, name = "Seasonal")
            await user.add_roles(add_role)
        elif(str(reaction.emoji) == "🍎"):
            add_role = discord.utils.get(user.guild.roles, name = "Roulette")
            await user.add_roles(add_role)
        elif(str(reaction.emoji) == "🥝"):
            add_role = discord.utils.get(user.guild.roles, name = "Lewd")
            await user.add_roles(add_role)
        elif(str(reaction.emoji) == "🍉"):
            add_role = discord.utils.get(user.guild.roles, name = "Spoilers")
            await user.add_roles(add_role)
        # second message
        elif str(reaction.emoji) == "💦":
            add_role = discord.utils.get(user.guild.roles, name = "Blue")
            await user.add_roles(add_role)
        elif(str(reaction.emoji) == "🎱"):
            add_role = discord.utils.get(user.guild.roles, name = "Black")
            await user.add_roles(add_role)
        elif str(reaction.emoji) == "💛":
            add_role = discord.utils.get(user.guild.roles, name = "Yellow")
            await user.add_roles(add_role)
        elif(str(reaction.emoji) == "🐷"):
            add_role = discord.utils.get(user.guild.roles, name = "Pink")
            await user.add_roles(add_role)
        elif(str(reaction.emoji) == "🔴"):
            add_role = discord.utils.get(user.guild.roles, name = "Red")
            await user.add_roles(add_role)
        elif(str(reaction.emoji) == "⚪"):
            add_role = discord.utils.get(user.guild.roles, name = "White")
            await user.add_roles(add_role)
        elif str(reaction.emoji) == "🔶":
            add_role = discord.utils.get(user.guild.roles, name = "Orange")
            await user.add_roles(add_role)
        elif(str(reaction.emoji) == "💚"):
            add_role = discord.utils.get(user.guild.roles, name = "Green")
            await user.add_roles(add_role)
        elif str(reaction.emoji) == "💜":
            add_role = discord.utils.get(user.guild.roles, name = "Purple")
            await user.add_roles(add_role)


    # remove roles based on removing a reaction
    @commands.Cog.listener()
    async def on_reaction_remove(self, reaction, user):
        if reaction.message.channel.id != channels.channel_dict["auto_role"]:
            return # not in the role channel
        #first message
        elif str(reaction.emoji) == "🍌":
            remove_role = discord.utils.get(user.guild.roles, name = "Sub Freak")
            await user.remove_roles(remove_role)
        elif(str(reaction.emoji) == "🍑"):
            remove_role = discord.utils.get(user.guild.roles, name = "Dub Peasant")
            await user.remove_roles(remove_role)
        elif str(reaction.emoji) == "🍊":
            remove_role = discord.utils.get(user.guild.roles, name = "Seasonal")
            await user.remove_roles(remove_role)
        elif(str(reaction.emoji) == "🍎"):
            remove_role = discord.utils.get(user.guild.roles, name = "Roulette")
            await user.remove_roles(remove_role)
        elif(str(reaction.emoji) == "🥝"):
            remove_role = discord.utils.get(user.guild.roles, name = "Lewd")
            await user.remove_roles(remove_role)
        elif(str(reaction.emoji) == "🍉"):
            remove_role = discord.utils.get(user.guild.roles, name = "Spoilers")
            await user.remove_roles(remove_role)
        # second message
        elif str(reaction.emoji) == "💦":
            remove_role = discord.utils.get(user.guild.roles, name = "Blue")
            await user.remove_roles(remove_role)
        elif(str(reaction.emoji) == "🎱"):
            remove_role = discord.utils.get(user.guild.roles, name = "Black")
            await user.remove_roles(remove_role)
        elif str(reaction.emoji) == "💛":
            remove_role = discord.utils.get(user.guild.roles, name = "Yellow")
            await user.remove_roles(remove_role)
        elif(str(reaction.emoji) == "🐷"):
            remove_role = discord.utils.get(user.guild.roles, name = "Pink")
            await user.remove_roles(remove_role)
        elif(str(reaction.emoji) == "🔴"):
            remove_role = discord.utils.get(user.guild.roles, name = "Red")
            await user.remove_roles(remove_role)
        elif(str(reaction.emoji) == "⚪"):
            remove_role = discord.utils.get(user.guild.roles, name = "White")
            await user.remove_roles(remove_role)
        elif str(reaction.emoji) == "🔶":
            remove_role = discord.utils.get(user.guild.roles, name = "Orange")
            await user.remove_roles(remove_role)
        elif(str(reaction.emoji) == "💚"):
            remove_role = discord.utils.get(user.guild.roles, name = "Green")
            await user.remove_roles(remove_role)
        elif str(reaction.emoji) == "💜":
            remove_role = discord.utils.get(user.guild.roles, name = "Purple")
            await user.remove_roles(remove_role)


    # a new member joins
    @commands.Cog.listener()
    async def on_member_join(self, member):
        # welcome new user
        # message destinations
        new_member = await self.bot.fetch_user(member.id)
        entrance = self.bot.get_channel(channels.channel_dict["entrance"])
        # send messages
        await new_member.send(f"BOO! Welcome to Zer0!\nPlease read through our rules page then type `/verify` into the #verify channel to access the server")
        await entrance.send(f"<@{new_member.id}> just joined the server!")

        # auto assign role to new member
        add_role = discord.utils.get(member.guild.roles, name = "Temp")
        await member.add_roles(add_role)


def setup(bot):
    bot.add_cog(member_moderation(bot))
