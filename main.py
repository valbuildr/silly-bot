import discord
from discord.ext import commands
from discord import app_commands as appcmds
from logging import getLogger
from dotenv import dotenv_values

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
bot.remove_command("help")

config = dotenv_values(".env")

log = getLogger("discord.sillybot")

@bot.event
async def on_ready():
    log.info(f"Logged in as {bot.user.name}!")

@bot.command(name="s", hidden=True)
@commands.is_owner()
@commands.dm_only()
async def sync(ctx: commands.Context):
    await ctx.send(content="Syncing...")
    await bot.tree.sync()
    await ctx.send(content="Synced!")

@bot.tree.command(name="bleh", description="silly cat!!")
@appcmds.user_install()
@appcmds.allowed_installs(guilds=True, users=True)
@appcmds.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def bleh(interaction: discord.Interaction):
    await interaction.response.defer()
    await interaction.followup.send(file=discord.File("sillycat.png"))

@bot.tree.command(name="about", description="about this very silly bot!!")
@appcmds.user_install()
@appcmds.allowed_installs(guilds=True, users=True)
@appcmds.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def about(interaction: discord.Interaction):
    e = discord.Embed()
    e.colour = discord.Colour.blurple()
    e.title("about silly bot")
    e.description("just a silly little bot :3")
    await interaction.response.send_message(embed=e, ephemeral=True)

bot.run(config["TOKEN"])