import time
import discord
from zed_bot import logger

log = logger.get_logger()


class Terminal:
    def __init__(self, user: discord.Member, channel: discord.TextChannel):
        self.user = user
        self.channel = channel
        self.creation_date = time.time()
        self.last_use_time = self.creation_date
        self.log = []
        self.command_log = []

    def lifespan_check(self):
        if self.last_use_time > time.time() + 120:
            return True
        else:
            return False

    def command(self, msg: discord.Message):
        log.info(f"Got command: {msg.content}")
        user = msg.author
        cmd = msg.content.lower()
        if self.check_if_command(cmd):
            log.info(f'User {user.name} used help cmd "{cmd}"')

    def check_if_command(self, cmd: str):
        is_command = False
        with open("./zed_bot/commands.txt", "r") as f:
            command_list = f.readlines()
            for command in command_list:
                if cmd.startswith(command):
                    is_command = True
        return is_command

    def on_command(self, msg: discord.Message):
        try:
            log.info(
                f"Channel: {str(self.channel.id)}, Message: {str(msg.channel.id)}"
            )
            try:
                if not (
                    self.channel.id == msg.channel.id or msg.author == self.user
                ):
                    log.error(
                        "Unable to execute command, channel or author discrepancy"
                    )
                    raise Exception("channel or author discrepancy")
                else:
                    self.command(msg=msg)
            except Exception as e:
                log.exception(f"Unknown exception: {e}")
                raise e
        except Exception as e:
            log.exception(f"Failed to find terminal: {e}")
