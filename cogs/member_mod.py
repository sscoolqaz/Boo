import discord
from discord.ext import commands
import asyncio
import json
import utils
import users
import config
import logging


class member_moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    # logging.basicConfig(level=logging.DEBUG)


    # mute all users -not finished-
    @commands.command(hidden = True)
    async def verify(self, ctx):
        if ctx.message.channel.id == config.channel_dict["verify"]:
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
    @commands.has_role(config.role_dict.get("admin"))
    async def mute(self, ctx, mute_user):
        user_to_mute = ctx.message.mentions[0] # id of person to mute that was mentioned in command
        mute_role = discord.utils.get(ctx.guild.roles, name = "Muted") # get the role to apply
        await user_to_mute.add_roles(mute_role) # assign the role
        await ctx.send(f"{ctx.message.author} has muted {user_to_mute}")


    # unmute specific user
    @commands.command(hidden = True)
    @commands.has_role(config.role_dict.get("admin"))
    async def unmute(self, ctx, unmute_user):
        user_to_unmute = ctx.message.mentions[0] # id of person to unmute that was mentioned in command
        unmute_role = discord.utils.get(ctx.guild.roles, name = "Muted") # get the role to apply
        await user_to_unmute.remove_roles(unmute_role) # assign the role
        await ctx.send(f"{ctx.message.author} has unmuted {user_to_unmute}")


    # warn specific user
    @commands.command(hidden = True)
    @commands.has_role(config.role_dict.get("admin"))
    async def warn(self, ctx, mute_user):
        warning_name    = ctx.message.mentions[0].display_name # name of person to that was warned
        warning_id      = ctx.message.mentions[0].id # id of person to that was warned
        # load the json file
        with open('warnings.json') as f:
            data = json.load(f)
        record_exists = False
        # search for the warned user
        for user in data:
            if user['id'] == warning_id: # if the warning id sent matches the one in the json file
                # increase the users warning count
                user['warnings'] += 1
                print(f"{user['name']} now has {user['warnings']} warnings.") # console
                await ctx.send(f"{user['name']} now has {user['warnings']} warnings.") # discord
                record_exists = True # record has been found
        # if no record exists for the mentioned user
        if record_exists == False:
            data.append( {'id': warning_id, 'name': str(warning_name), 'warnings': 1} )
        # write the edited dict to the json file
        with open('warnings.json', 'w') as f:
            json.dump(data, f, indent = 2)


    # remove warning from specific user
    @commands.command(hidden = True)
    @commands.has_role(config.role_dict.get("admin"))
    async def unwarn(self, ctx, mute_user):
        warning_id      = ctx.message.mentions[0].id # id of person to that was warned
        # load the json file
        with open('warnings.json') as f:
            data = json.load(f)
        # search for the warned user
        for user in data:
            if user['id'] == warning_id: # if the warning id sent mathes the one in the json file
                if user['warnings'] == 0:
                    print(f"{user['name']} doesnt have any warnings!") # console
                    await ctx.send(f"{user['name']} doesnt have any warnings!") # discord
                    continue
                # decrements the users warning count
                user['warnings'] -= 1
                print(f"{user['name']} now has {user['warnings']} warnings.") # console
                await ctx.send(f"{user['name']} now has {user['warnings']} warnings.") # discord
        # write the edited dict to the json file
        with open('warnings.json', 'w') as f:
            json.dump(data, f, indent = 2)


    # kick mentioned user
    @commands.command(hidden = True)
    @commands.has_role(config.role_dict.get("admin"))
    async def kick(self, ctx, ban_user, *, words):
        await ctx.message.mentions[0].kick(reason = words)


    # ban mentioned user
    @commands.command(hidden = True)
    @commands.has_role(config.role_dict.get("admin"))
    async def ban(self, ctx, ban_user):
        await ctx.message.mentions[0].ban()


    # assign roles based on adding a reaction
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        # variables
        guild   = self.bot.get_guild(payload.guild_id)
        user    = guild.get_member(payload.user_id)
        channel = self.bot.get_channel(payload.channel_id)

        if payload.user_id != users.users_dict["Booette"]: # reaction author wasn't bot
            if payload.channel_id == config.channel_dict["auto_role"]: # in the role channel
                role_to_add = discord.utils.get(channel.guild.roles, id = config.role_dict.get(str(payload.emoji)))
                await user.add_roles(role_to_add) # add role to user depending on the reaction emoji
                await self.bot.get_channel(config.channel_dict["logs"]).send(embed=self.role_embed("added.", user, role_to_add))


    # remove roles based on removing a reaction
    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        # variables
        guild   = self.bot.get_guild(payload.guild_id)
        user    = guild.get_member(payload.user_id)
        channel = self.bot.get_channel(payload.channel_id)

        if payload.channel_id == config.channel_dict["auto_role"]:
            role_to_remove = discord.utils.get(channel.guild.roles, id = config.role_dict.get(str(payload.emoji)))
            await user.remove_roles(role_to_remove) # remove role to user depending on the reaction emoji
            await self.bot.get_channel(config.channel_dict["logs"]).send(embed=self.role_embed("removed.", user, role_to_remove))


    # post an embed logging someone getting/losing a role
    def role_embed(self, status, user, role):
        embed = discord.Embed(title = "Role Change", description = f"<@{user.id}> had the role {role.name} {status}", color=0xaf68c9)
        embed.set_thumbnail(url=user.avatar_url)
        embed.set_footer(text=f"ID: {user.id}")
        return embed


    # a new member joins
    @commands.Cog.listener()
    async def on_member_join(self, member):
        # welcome new user
        # message destinations
        new_member = await self.bot.fetch_user(member.id)
        entrance = self.bot.get_channel(config.channel_dict["entrance"])
        # send messages
        await new_member.send("BOO! Welcome to Zer0!\nPlease read through our rules page then type `/verify` into the #verify channel to access the server")
        await entrance.send(f"<@{new_member.id}> just joined the server!")

        # log
        embed = discord.Embed(title="Member Joined", description=f"<@{new_member.id}> {new_member.name}", color=0xaf68c9) # set up embed
        embed.set_thumbnail(url=new_member.avatar_url)
        embed.add_field(name = "Account Creation", value = new_member.created_at.strftime("%c"), inline = False)
        embed.set_footer(text=f"ID: {new_member.id}")
        await self.bot.get_channel(config.channel_dict["logs"]).send(embed=embed)

        # auto assign role to new member
        add_role = discord.utils.get(member.guild.roles, name = "Temp")
        await member.add_roles(add_role)


    # a member leaves
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        # log
        embed = discord.Embed(title="Member Left", description=f"<@{member.id}> {member.name}", color=0xaf68c9) # set up embed
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text=f"ID: {member.id}")
        await self.bot.get_channel(config.channel_dict["logs"]).send(embed=embed)


def setup(bot):
    bot.add_cog(member_moderation(bot))
