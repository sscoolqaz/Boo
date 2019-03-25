import discord
from discord.ext import commands
import asyncio
import json
import utils


# VARIABLES
roleChannelId = '513515376022388786'
entrance_id = "547907603494338610"
verify_id = "554120068619829249"
booette_id = "554062982301220905"


class member_moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    # mute all users -not finished-
    @commands.command(hidden = True)
    async def verify(self, ctx):
        if ctx.message.channel.id == verify_id:
            user = ctx.message.author
            add_role = discord.utils.get(user.server.roles, name = "Member")
            await self.bot.add_roles(user, add_role)
            print(f"The role {add_role} was added to {user}")
            await asyncio.sleep(1)
            rmv_role = discord.utils.get(user.server.roles, name = "Temp")
            await self.bot.remove_roles(user, rmv_role)
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


    # mute specific user
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
                    await self.bot.say(f"{user['name']} now has {user['warnings']} warnings.")
                    record_exists = True # record has been found
            # if no record exists for the mentioned user
            if record_exists == False:
                data.append( {'id': warning_id, 'name': str(warning_name), 'warnings': 1} )
            # write the edited dict to the json file
            with open('warnings.json', 'w') as f:
                json.dump(data, f, indent = 2)

        else:
            await self.bot.say("You do not have permission to use this command")


    # mute specific user
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
                    await self.bot.say(f"{user['name']} now has {user['warnings']} warnings.")
            # write the edited dict to the json file
            with open('warnings.json', 'w') as f:
                json.dump(data, f, indent = 2)

        else:
            await self.bot.say("You do not have permission to use this command")


    # assign roles based on adding a reaction
    async def on_reaction_add(self, reaction, user):
        if user.id == booette_id: # don't assign roles for Booette
            return

        if reaction.message.channel.id != roleChannelId:
            return # not in the role channel

        # first message
        elif str(reaction.emoji) == "🍌":
            add_role = discord.utils.get(user.server.roles, name = "Sub Freak")
            await self.bot.add_roles(user, add_role)
        elif(str(reaction.emoji) == "🍑"):
            add_role = discord.utils.get(user.server.roles, name = "Dub Peasant")
            await self.bot.add_roles(user, add_role)
        elif str(reaction.emoji) == "🍊":
            add_role = discord.utils.get(user.server.roles, name = "Seasonal")
            await self.bot.add_roles(user, add_role)
        elif(str(reaction.emoji) == "🍎"):
            add_role = discord.utils.get(user.server.roles, name = "Roulette")
            await self.bot.add_roles(user, add_role)
        elif(str(reaction.emoji) == "🥝"):
            add_role = discord.utils.get(user.server.roles, name = "Lewd")
            await self.bot.add_roles(user, add_role)
        elif(str(reaction.emoji) == "🍉"):
            add_role = discord.utils.get(user.server.roles, name = "Spoilers")
            await self.bot.add_roles(user, add_role)
        # second message
        elif str(reaction.emoji) == "💦":
            add_role = discord.utils.get(user.server.roles, name = "Blue")
            await self.bot.add_roles(user, add_role)
        elif(str(reaction.emoji) == "🎱"):
            add_role = discord.utils.get(user.server.roles, name = "Black")
            await self.bot.add_roles(user, add_role)
        elif str(reaction.emoji) == "💛":
            add_role = discord.utils.get(user.server.roles, name = "Yellow")
            await self.bot.add_roles(user, add_role)
        elif(str(reaction.emoji) == "🐷"):
            add_role = discord.utils.get(user.server.roles, name = "Pink")
            await self.bot.add_roles(user, add_role)
        elif(str(reaction.emoji) == "🔴"):
            add_role = discord.utils.get(user.server.roles, name = "Red")
            await self.bot.add_roles(user, add_role)
        elif(str(reaction.emoji) == "⚪"):
            add_role = discord.utils.get(user.server.roles, name = "White")
            await self.bot.add_roles(user, add_role)
        elif str(reaction.emoji) == "🔶":
            add_role = discord.utils.get(user.server.roles, name = "Orange")
            await self.bot.add_roles(user, add_role)
        elif(str(reaction.emoji) == "💚"):
            add_role = discord.utils.get(user.server.roles, name = "Green")
            await self.bot.add_roles(user, add_role)
        elif str(reaction.emoji) == "💜":
            add_role = discord.utils.get(user.server.roles, name = "Purple")
            await self.bot.add_roles(user, add_role)


    # remove roles based on removing a reaction
    async def on_reaction_remove(self, reaction, user):
        if reaction.message.channel.id != roleChannelId:
            return # not in the role channel
        #first message
        elif str(reaction.emoji) == "🍌":
            remove_role = discord.utils.get(user.server.roles, name = "Sub Freak")
            await self.bot.remove_roles(user, remove_role)
        elif(str(reaction.emoji) == "🍑"):
            remove_role = discord.utils.get(user.server.roles, name = "Dub Peasant")
            await self.bot.remove_roles(user, remove_role)
        elif str(reaction.emoji) == "🍊":
            remove_role = discord.utils.get(user.server.roles, name = "Seasonal")
            await self.bot.remove_roles(user, remove_role)
        elif(str(reaction.emoji) == "🍎"):
            remove_role = discord.utils.get(user.server.roles, name = "Roulette")
            await self.bot.remove_roles(user, remove_role)
        elif(str(reaction.emoji) == "🥝"):
            remove_role = discord.utils.get(user.server.roles, name = "Lewd")
            await self.bot.remove_roles(user, remove_role)
        elif(str(reaction.emoji) == "🍉"):
            remove_role = discord.utils.get(user.server.roles, name = "Spoilers")
            await self.bot.remove_roles(user, remove_role)
        # second message
        elif str(reaction.emoji) == "💦":
            remove_role = discord.utils.get(user.server.roles, name = "Blue")
            await self.bot.remove_roles(user, remove_role)
        elif(str(reaction.emoji) == "🎱"):
            remove_role = discord.utils.get(user.server.roles, name = "Black")
            await self.bot.remove_roles(user, remove_role)
        elif str(reaction.emoji) == "💛":
            remove_role = discord.utils.get(user.server.roles, name = "Yellow")
            await self.bot.remove_roles(user, remove_role)
        elif(str(reaction.emoji) == "🐷"):
            remove_role = discord.utils.get(user.server.roles, name = "Pink")
            await self.bot.remove_roles(user, remove_role)
        elif(str(reaction.emoji) == "🔴"):
            remove_role = discord.utils.get(user.server.roles, name = "Red")
            await self.bot.remove_roles(user, remove_role)
        elif(str(reaction.emoji) == "⚪"):
            remove_role = discord.utils.get(user.server.roles, name = "White")
            await self.bot.remove_roles(user, remove_role)
        elif str(reaction.emoji) == "🔶":
            remove_role = discord.utils.get(user.server.roles, name = "Orange")
            await self.bot.remove_roles(user, remove_role)
        elif(str(reaction.emoji) == "💚"):
            remove_role = discord.utils.get(user.server.roles, name = "Green")
            await self.bot.remove_roles(user, remove_role)
        elif str(reaction.emoji) == "💜":
            remove_role = discord.utils.get(user.server.roles, name = "Purple")
            await self.bot.remove_roles(user, remove_role)


    # a new member joins
    async def on_member_join(self, member):
        # welcome new user
        # message destinations
        new_member = await self.bot.get_user_info(member.id)
        entrance = self.bot.get_channel(entrance_id)
        verify_channel = self.bot.get_channel(verify_id)
        # send messages
        await self.bot.send_message(new_member, f"BOO! Welcome to Zer0!\nPlease read through our rules page then type `/verify` into the #verify channel to access the server")
        await self.bot.send_message(entrance, f"<@{new_member.id}> just joined the server!")

        # auto assign role to new member
        add_role = discord.utils.get(member.server.roles, name = "Temp")
        await self.bot.add_roles(member, add_role)


def setup(bot):
    bot.add_cog(member_moderation(bot))
