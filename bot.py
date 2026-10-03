import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")

@bot.command()
async def support(ctx):
    await ctx.send("أهلاً بك في الدعم الفني! كيف يمكنني مساعدتك اليوم؟")

bot.run("MTU1NTgyNTU4NTI3NDQ5MDg4MA.GZ-BaR.SmvBAwzMyBBQsF3llYfeq7SBeaJ94bCry6gfKs")
