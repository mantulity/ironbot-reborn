import logging
from pathlib import Path
from sys import argv
import os
import telethon.utils
from telethon import TelegramClient
from telethon import __version__ as tv
import sys
import platform
from ironbot import bot, client2, client3, iron_version
from ironbot.Configs import Config
from telethon.tl.types import InputMessagesFilterDocument
from ironbot.utils import load_module, start_assistant, load_module_dclient
from ironbot.Configs import Config

ironbotdevs = logging.getLogger("IRONBOT")

async def add_bot(bot_token):
    await bot.start(bot_token)
    bot.me = await bot.get_me()
    bot.uid = telethon.utils.get_peer_id(bot.me)
   
        
# Bleck Megic         
async def check_inline_on_warner(ws):
    w_s = await ws.get_me()
    if not w_s.bot_inline_placeholder:
        ironbotdevs.info("Warning : We Have Detected That You Have Not Turned On Inline Mode For Your Assistant Bot, Please Go To @BotFather And Enable This.")
    return
Lol = "folyl's Token"
async def lol_s(client):
    client.me = await client.get_me()
    client.uid = telethon.utils.get_peer_id(client.me)
    
def multiple_client():
    if client2:
        ironbotdevs.info("Starting Client 2")
        try:
            warnerstark = None
            client2.start()
            client2.loop.run_until_complete(lol_s(client2))
        except:
            warnerstark = True
            ironbotdevs.info("Client 2 Failed To Load. Check Your String.")
    if client3:
        ironbotdevs.info("Starting Client 3")
        try:
            chsaiujwal = None
            cleint3.start
            client3.loop.run_until_complete(lol_s(client3))
        except:
            chsaiujwal = True
            ironbotdevs.info("Client 3 Failed To Load.")
    if not client2:
        warnerstark = True
    if not client3:
        chsaiujwal = True
    return warnerstark, chsaiujwal    

async def get_other_plugins(Config, client_s, ironbotdevs):
    try:
        a_plugins = await client_s.get_messages(
            entity=Config.LOAD_OTHER_PLUGINS_CHNNL,
            filter=InputMessagesFilterDocument,
            limit=None,
            search=".py",
        )
    except:
        ironbotdevs.info("Failed To Other Modules :(")
        return
    for meisnub in a_plugins:
        hmm = meisnub.media.document.attributes[-1].file_name
        pathh = "ironbot/modules/"
        if os.path.exists(os.path.join(pathh, hmm)):
            pass
        else:
            await client_s.download_media(meisnub.media, "ironbot/modules/")
    ironbotdevs.info("Extra Plugins Downloaded.")

if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    if Config.TG_BOT_TOKEN_BF_HER is not None:
        bot.tgbot = TelegramClient(
            "TG_BOT_TOKEN", api_id=Config.APP_ID, api_hash=Config.API_HASH
        ).start(bot_token=Config.TG_BOT_TOKEN_BF_HER)
        failed2, failed3 = multiple_client()
        bot.loop.run_until_complete(add_bot("SXJvbmJvdCBpcyBCZXN0Cg=="))
    else:
        bot.loop.run_until_complete(add_bot("SXJvbmJvdCBpcyBCZXN0Cg=="))
        failed2, failed3 = multiple_client()

if Config.LOAD_OTHER_PLUGINS:
        bot.loop.run_until_complete(get_other_plugins(Config, bot, ironbotdevs))
        
import glob

path = "ironbot/modules/*.py"
files = glob.glob(path)
failed_warner = 0
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        try:
            load_module(shortname.replace(".py", ""))    
        except Exception as e:
            failed_warner += 1
            ironbotdevs.info("------------------------")
            ironbotdevs.info("Failed To Load : " + str(shortname.replace(".py", "")) + f" Error : {str(e)}")
            ironbotdevs.info("------------------------")
        if failed2 is None:
            try:
                load_module_dclient(shortname.replace(".py", ""), client2)
            except:
                pass
        if failed3 is None:
            try:
                load_module_dclient(shortname.replace(".py", ""), client3)
            except:
                pass

if Config.ENABLE_ASSISTANTBOT == "ENABLE":
    path = "ironbot/modules/assistant/*.py"
    files = glob.glob(path)
    for name in files:
        with open(name) as f:
            path1 = Path(f.name)
            shortname = path1.stem
            start_assistant(shortname.replace(".py", ""))
    wsta = "Ironbot Have Been Installed Successfully !"
else:
    wsta = "Ironbot Has Been Installed Sucessfully"

total_clients = 1
if failed2 is None:
    total_clients += 1
if failed3 is None:
    total_clients += 1
    
ironbotdevs.info(f"""{wsta}
-------------------------------------------
Ironbot-reborn Based On Telethon V{tv}
Python Version : {platform.python_version()}
Ironbot-reborn Version : V{iron_version}
Total Clients : {total_clients}
Dev : @ndourbae
Thanks to : @freedom_reborn
-------------------------------------------""")
        
bot.tgbot.loop.run_until_complete(check_inline_on_warner(bot.tgbot))

if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
