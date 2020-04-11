import discord
from discord.ext import commands
from discord.utils import get
import os

client = commands.Bot(command_prefix="#")

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Streaming(name="ItsCopex#9227", url="https://twitch.tv/itscopex"))

@client.event
async def on_member_join(member):
    role = get(member.guild.roles, name="Army")
    await member.add_roles(role)

@client.command()
async def YouTube(ctx):
    await ctx.send(f"**YouTube: https://www.youtube.com/channel/UC4lsQ9cTpe4rkbom4E7kC5g?view_as=subscriber**")

@client.event
async def on_raw_reaction_add(self, payload): 
channel = discord.utils.get(self.guild.text_channels, name='rules') 
if not payload.guild_id: 
return if payload.channel_id != channel.id:
return	guild = self.get_guild(payload.guild_id) 
member = guild.get_member(payload.user_id)
if payload.emoji.id != 698647548084355154:
role = discord.utils.get(guild.roles, name="Army") else:
return await member.add_roles(role, reason='Reaction role')

@client.event
async def on_raw_reaction_remove(self, payload):
channel = discord.utils.get(self.guild.text_channels, name='rules') 
if not payload.guild_id: 
return if payload.channel_id != channel.id: 
return	 guild = self.get_guild(payload.guild_id) member = guild.get_member(payload.user_id) 
if payload.emoji.id != 698647548084355154:
role = discord.utils.get(guild.roles, name="Army") else: 
return await member.remove_roles(role, reason='Reaction role') 

@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)
    await ctx.send(f"**{amount} Nachrichten wurden gelöscht**")

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f"**Das Mitglied {member} wurde vom Discord gekickt**")

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f"**Das Mitglied {member} wurde vom Discord gebant**")

@client.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
    banned_user = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")

    for ban_entry in banned_user:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"**Das Mitglied {member} wurde Endband**")


client.run(os.environ["DISCORD_TOKEN"])
