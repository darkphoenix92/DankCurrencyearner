import time
import random
from discord.ext import commands
import discord

fuckyou = commands.Bot(command_prefix="l", self_bot=True)
key = ""


@fuckyou.event
async def on_ready():
    print("Let's go")


@fuckyou.command()
async def se(ctx):
    while True:
        await ctx.send("pls beg")
        time.sleep(8)
        await ctx.send("pls deposit max")
        time.sleep(6)
        time.sleep(4)
        await ctx.send("pls hunt")
        time.sleep(9)
        await ctx.send("pls fish")
        time.sleep(8)
        await ctx.send("pls dig")
        time.sleep(8)


fuckyou.run(key, bot=False)
