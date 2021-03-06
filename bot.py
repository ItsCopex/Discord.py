import discord
from discord.ext import commands
from discord.utils import get
import os

client = commands.Bot(command_prefix="-")

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="Abonniert BeCalmFN"))

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
