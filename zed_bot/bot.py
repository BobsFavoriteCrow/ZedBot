"""Primary module for defining the Discord bot."""
import discord

from zed_bot import logger

# Create logger
log = logger.get_logger()


class ZedBot(discord.Bot):
    def __init__(
        self,
        description: str=None,
        intents: discord.Intents=None,
        *args,
        **options,
    ):
        description = "Inspired by the greatest programmer in the world"
        intents = intents if intents else discord.Intents.all()
        super().__init__(description, *args, **options)

    async def on_ready(self):
        log.info(f"Logged in as {self.user.name}")
        print(f"{self.user} is ready and online!")

    async def on_member_join(member: discord.Member):
        await member.send(f"Hello, {member.display_name}!")
