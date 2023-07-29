"""Constants and enumerations for zedBot."""
from os import getenv
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

#################################
#         CONSTANTS             #
#################################
IS_LOCAL = getenv("is_local")
GUILD_ID = int(getenv("DISCORD_GUILD_ID"))
TOKEN = str(getenv("ZEDBOT_TOKEN"))
