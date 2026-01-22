import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import mysql.connector
from store import create_player
from search import get_players_by_name
from datetime import datetime


load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()

intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# if get_connection.is_connected()

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")


@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")
@bot.command()
async def settime(ctx, time_str: str):

    # ① 時刻文字列を datetime.time に変換
    try:
        time_obj = datetime.strptime(time_str, "%H:%M").time()
    except ValueError:
        await ctx.send("時刻の形式が正しくありません。例: 12:30")
        return
    else:
        await ctx.send("起床時刻を設定しました")
    p = create_player(ctx.author.display_name,time_obj)
    await ctx.send("設定を保存しました")
    await ctx.send(f"{p.id} {p.username} {p.time}")
@bot.command()
async def check(ctx):

    p = get_players_by_name(ctx.author.display_name)
    for i in p:
        await ctx.send(f"{i.id} {i.username} {i.time}")
    



bot.run(TOKEN)
