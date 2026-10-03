import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")

bot.run("MTU1NTgyNTU4NTI3NDQ5MDg4MA.GNOVd3.4LaAf0AkLKhCmL2FZ9T6-Vxqa2RqU13zWjJEXA")
