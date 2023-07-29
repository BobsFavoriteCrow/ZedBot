"""Main module for calling zedBot."""
from random import randint

import discord

from zed_bot import bot as my_bot

from zed_bot import logger, enums

# Create logger
log = logger.get_logger()

# Instantiate ZedBot
bot = my_bot.ZedBot()


# Create slash commands
@bot.slash_command(
    name="hello",
    description="Say hello to the bot",
    guild_ids=[enums.GUILD_ID],
)
async def hello(ctx: discord.ApplicationContext):
    log.info("We received a slash command!")
    await ctx.respond("Hello!")


@bot.slash_command(
    name="ping",
    description="Check the latency of the bot",
    guild_ids=[enums.GUILD_ID],
)
async def ping(ctx: discord.ApplicationCommand):
    bot_latency = int(float(f"{bot.latency:.3f}")*1000)
    await ctx.respond(f"Pong! Latency is {bot_latency:3}ms.")


@bot.slash_command(
    name="guess_the_number",
    description="Guess the number between 1 and 10",
    guild_ids=[enums.GUILD_ID],
)
async def gtn(ctx: discord.ApplicationCommand):
    """Play this stupid game and guess a number.

    Parameters
    ----------
    ctx : discord.ApplicationCommand
        _description_
    """
    answer: int = randint(1, 10)
    log.info(f"The answer is: {answer}")
    await ctx.respond("Guess a number between 1 and 10 within 30 seconds.")

    win = False
    timeout = 30
    while not win:
        guess: discord.Message = await bot.wait_for(
            "message",
            check=lambda message: message.author == ctx.author,
            timeout=timeout,
        )
        log.info(f"User guess content: {guess.content}")

        if guess.content == "":
            await ctx.send(
                "Please respond directly to my messages for me to read your guess!"
            )
        elif int(float(guess.content)) == answer:
            await ctx.send("You guessed it!")
            win = True
            break
        else:
            await ctx.send("Nope, try again.")
        continue


# Run bot
bot.run(enums.TOKEN)
