from zed_bot import terminal
import discord
from datetime import datetime
from zed_bot import enums


token = enums.TOKEN
server_id = enums.GUILD_ID

intents = discord.Intents.all()

bot = discord.Bot(intents=intents, debug_guilds=[server_id])


@bot.event
async def on_ready():
    now = datetime.now()
    now = now.strftime("%d/%m/%Y %H:%M:%S")
    print(f"Running {bot.user}. \nStarted at {now}.\nPing {bot.latency:3f}ms.")


@bot.slash_command(name="start", description="start new terminal")
async def start(ctx: discord.ApplicationContext):
    await terminal.create_terminal(ctx.author, ctx=ctx)


@bot.event
async def on_message(msg: discord.Message):
    if not msg.author.bot:
        if str(msg.channel.category) == "Terminals":
            terminal.on_command(msg)


bot.run(token)
