import discord
from datetime import datetime
from zed_bot import terminal, enums, logger

log = logger.get_logger()


token = enums.TOKEN
server_id = enums.GUILD_ID

intents = discord.Intents.all()

bot = discord.Bot(intents=intents, debug_guilds=[server_id])


@bot.event
async def on_ready():
    now = datetime.now()
    now = now.strftime("%d/%m/%Y %H:%M:%S")
    log.info(
        f"Running {bot.user}. \nStarted at {now}.\nPing {bot.latency:3f}ms."
    )


@bot.slash_command(name="start", description="start new terminal")
async def start(ctx: discord.ApplicationContext):
    if not ctx.author.bot:
        # name = f"{ctx.author.id}"
        cat = discord.utils.get(ctx.guild.categories, name="Terminals")
        channel = await ctx.guild.create_text_channel(ctx.author.id, category=cat)
        global active_terminal
        active_terminal = terminal.Terminal(user=ctx.author, channel=channel)
        await channel.set_permissions(ctx.author, read_messages=True, send_messages=True)
        await channel.send(
            f"```>\n>\n>\n>\n>\n>\n>\n>\n>\n>\n>\n>\n>STARTED NEW TERMINAL FOR {ctx.author.name.upper()} USE 'help' FOR COMMAND LIST```"
        )
    else:
        await ctx.send("You can't invoke this command, you nasty bot >:p")


@bot.event
async def on_message(msg: discord.Message):
    if "active_terminal" in globals():
        if msg.author.name == active_terminal.user.name:
            active_terminal.on_command(msg)
    else:
        log.warning("No active terminal found, aborting command")


bot.run(token)
