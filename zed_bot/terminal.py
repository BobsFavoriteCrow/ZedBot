import time
import discord

active_terminals = []
async def create_terminal(user:discord.Member, ctx:discord.ApplicationContext):
    name = f'{user.id}'
    cat = discord.utils.get(ctx.guild.categories, name="Terminals")
    channel = await ctx.guild.create_text_channel(name, category=cat)
    new_terminal = Terminal(user, channel)
    active_terminals.append(new_terminal)
    await channel.set_permissions(user,read_messages=True, send_messages=True)
    await channel.send(f"```>\n>\n>\n>\n>\n>\n>\n>\n>\n>\n>\n>\n>STARTED NEW TERMINAL FOR {user.name.upper()} USE 'help' FOR COMMAND LIST```")


def check_if_command(cmd:str):
    is_command = False
    with open("commands.txt", "r") as f:
        command_list = f.readlines()
        for command in command_list:
            if cmd.startswith(command):
                is_command = True
    return is_command


def on_command(msg:discord.Message):
    for term in active_terminals:
        try:
            print(str(term.channel_id), ",", str(msg.channel.id))
            if str(term.channel_id) == str(msg.channel.id):
                try:
                    term.command(msg=msg)
                except:
                    print("Failed to exicute command")
        except:
            print("Failed to find terminal")

class Terminal():
    def __init__(self, user:discord.Member, channel:discord.TextChannel):
        self.user = user
        self.channel_id = channel.id
        self.creation_date = time.time()
        self.lastUseTime = self.creation_date
        self.log = []
        self.command_log = []
    def lifespan_check(self):
        if self.lastUseTime > time.time() + 120:
            return True
        else:
            return False
    def command(msg:discord.Message):
        print("Got command")
        user=msg.author
        cmd = msg.content.lower()
        if check_if_command(cmd):
            if cmd.startswith("help"):
                print(f"User{user} used help cmd \"{cmd}\"")
