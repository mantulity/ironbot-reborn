from ironbot.Configs import Config
import time
from telethon import __version__ as tv
import sys
import platform
from git import Repo
from ironbot import ALIVE_NAME
from ironbot.modules import currentversion

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"
PM_IMG = "https://telegra.ph/file/d48eab138afb66385f1f9.jpg"
pm_caption = "➥ **ASSISTANT IS:** `ONLINE`\n\n"
pm_caption += "➥ **SYSTEMS STATS**\n"
pm_caption += f"➥ **Telethon Version:** `{tv}` \n"
pm_caption += f"➥ **Python:** `{platform.python_version()}` \n"
pm_caption += "➥ **Database Status:**  `Functional`\n"
pm_caption += "➥ **Current Branch** : `master`\n"
pm_caption += f"➥ **Version** : `{currentversion}`\n"
pm_caption += f"➥ **My Boss** : {DEFAULTUSER} \n"
pm_caption += "➥ **Heroku Database** : `AWS - Working Properly`\n\n"
pm_caption += "➥ **License** : [GNU General Public License v3.0](github.com/mabotsss/ironbot-reborn/blob/master/LICENSE)\n"

# only Owner Can Use it
@assistant_cmd("alive", is_args=False)
@peru_only
async def iron(event):
    await tgbot.send_file(event.chat_id, PM_IMG, caption=pm_caption)
