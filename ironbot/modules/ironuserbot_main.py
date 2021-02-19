from ironbot import CMD_HELP, CMD_LIST
from ironbot.utils import iron_on_cmd, sudo_cmd
import time
from telethon import __version__ as tv
import sys
import platform
from git import Repo
from uniborg.util import iron_on_cmd, sudo_cmd
from ironbot import ALIVE_NAME, CMD_HELP, Lastupdate, iron_version
from ironbot.Configs import Config
from ironbot.modules import currentversion
import time
import asyncio
import os
from pathlib import Path
import asyncio
import sys
from os import environ, execle, path, remove

from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError, NoSuchPathError

from ironbot import CMD_HELP
from ironbot.utils import iron_on_cmd
from ironbot.Configs import Config

UPSTREAM_REPO_URL = Config.UPSTREAM_REPO
UPSTREAM_REPO_BRANCH = "master"
HEROKU_APP_NAME = Config.HEROKU_APP_NAME
HEROKU_API_KEY = Config.HEROKU_API_KEY
requirements_path = path.join(
    path.dirname(path.dirname(path.dirname(__file__))), "requirements.txt"
)

from ironbot.utils import iron_on_cmd, load_module
from ironbot.function import get_all_modules
from ironbot import CMD_HELP
DELETE_TIMEOUT = 5
from datetime import datetime
from ironbot import CMD_HELP, Lastupdate
from ironbot.utils import edit_or_reply, iron_on_cmd, sudo_cmd


# Functions
def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"
PM_IMG = Config.ALIVE_IMAGE


@iron.on(iron_on_cmd(pattern=r"alive"))
@iron.on(sudo_cmd(pattern=r"alive", allow_sudo=True))
async def ironalive(alive):
    if alive.fwd_from:
        return
    await alive.get_chat()
    uptime = get_readable_time((time.time() - Lastupdate))
    repo = Repo()
    branch_name = repo.active_branch.name
    pm_caption = (
         "╭━━━━━━| 𝙸𝚁𝙾𝙽𝙱𝙾𝚃 |━━━━━━╮\n"
        f"┣[•👤 `USER     :` {bot.me.first_name}\n"
        f"┣▰▱▰▱▰▱▰▱▰▱▰▱▰▱\n"
        f"┣[•🤖 `Iron Ver : {iron_version} ➰`\n"
        f"┣[•🐍 `Python.  : v.{platform.python_version()} ➰`\n"
        f"┣[•⚙️ `Telethon : v.{tv} ➰`\n"
        f"┣[•💡 `Base on  : {branch_name} ➰`\n"
        f"┣[•🕒 `Uptime.  : {uptime} ➰`\n"
        f"╰━━━━━━━━━━━━━━━━━━━━╯\n"
    )
    
    await borg.send_message(
        alive.chat_id,
        pm_caption,
        reply_to=alive.message.reply_to_msg_id,
        file=PM_IMG,
        force_document=False,
        silent=True,
    )
    await alive.delete()


@iron.on(sudo_cmd(pattern="ahelp ?(.*)", allow_sudo=True))
@iron.on(iron_on_cmd(pattern="ahelp ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await event.edit(f"Here is some help for the {CMD_HELP[args]}")
        else:
            await event.edit(
                f"Help string for {args} not found! Type `.help` to see valid module names."
            )
    else:
        string = ""
        for i in CMD_HELP.values():
            string += f"`{str(i[0])}`, "
        string = string[:-2]
        await event.edit(
            "Please specify which module you want help for!\n\n" f"{string}"
        )
        
@iron.on(iron_on_cmd(pattern="ping$"))
@iron.on(sudo_cmd(pattern="ping$", allow_sudo=True))
async def _(event):
    starkislub = await edit_or_reply(event, "`Pong !`")
    if event.fwd_from:
        return
    hmm = await bot.get_me()
    rip = (f"[{hmm.first_name}](tg://user?id={hmm.id})")
    if not hmm.username:
        hmm.username = hmm.id
    bothmm = await tgbot.get_me()
    botrip = (f"[{bothmm.first_name}](tg://user?id={bothmm.id})")
    start = datetime.now()
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    uptime = get_readable_time((time.time() - Lastupdate))
    await starkislub.edit(
        f"➲ `{ms}` \n➲ `{uptime}` \n➲ {rip} \n➲ {bothmm.username}"
    )


@iron.on(iron_on_cmd(pattern="install"))
async def install(event):
    if event.fwd_from:
        return
    if event.reply_to_msg_id:
        sedplugin = await event.get_reply_message()
        try:
            downloaded_file_name = await event.client.download_media(
                sedplugin,
                "ironbot/modules/",
            )
            if "(" not in downloaded_file_name:
                path1 = Path(downloaded_file_name)
                shortname = path1.stem
                load_module(shortname.replace(".py", ""))
                await event.edit(
                    "IRON Has Installed `{}` Sucessfully.".format(
                        os.path.basename(downloaded_file_name)
                    )
                )
            else:
                os.remove(downloaded_file_name)
                await event.edit(
                    "Errors! This plugin is already installed/pre-installed."
                )
        except Exception as e:  # pylint:disable=C0103,W0703
            await event.edit(
                f"Error While Installing This Plugin, Please Make Sure That its py Extension. \n**ERROR :** {e}"
            )
            os.remove(downloaded_file_name)
    await asyncio.sleep(DELETE_TIMEOUT)
    await event.delete()
    

@borg.on(iron_on_cmd(pattern='pl ?(.*)'))
async def _(event):
    if event.fwd_from:
        return
    lul = event.pattern_match.group(1)
    yesm, nope, total_p = await get_all_modules(event, borg, lul)
    await event.edit(f"Installed {yesm} PLugins. Failed To Install {nope} Plugins And There Were Total {total_p} Plugins")
    
    
async def gen_chlog(repo, diff):
    ch_log = ""
    d_form = "%d/%m/%y **%H:%M**"
    for c in repo.iter_commits(diff):
        ch_log += (
            f"•[{c.committed_datetime.strftime(d_form)}]:\n"
            f"{c.summary} <{c.author}>\n"
        )
    return ch_log

async def print_changelogs(event, ac_br, changelog):
    changelog_str = (
        f"**Ada UPDATE Baru [{ac_br}]:\n\nPerubahan info :**\n`{changelog}`"
    )
    if len(changelog_str) > 4096:
        await event.edit("`Changelog is too big, view the file to see it.`")
        file = open("output.txt", "w+")
        file.write(changelog_str)
        file.close()
        await event.client.send_file(
            event.chat_id, "output.txt", reply_to=event.id,
        )
        remove("output.txt")
    else:
        await event.client.send_message(
            event.chat_id, changelog_str, reply_to=event.id,
        )
    return True


async def update_requirements():
    reqs = str(requirements_path)
    try:
        process = await asyncio.create_subprocess_shell(
            " ".join([sys.executable, "-m", "pip", "install", "-r", reqs]),
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        await process.communicate()
        return process.returncode
    except Exception as e:
        return repr(e)


async def deploy(event, repo, ups_rem, ac_br, txt):
    if HEROKU_API_KEY is not None:
        import heroku3

        heroku = heroku3.from_key(HEROKU_API_KEY)
        heroku_app = None
        heroku_applications = heroku.apps()
        if HEROKU_APP_NAME is None:
            await event.edit(
                "`[HEROKU]`\n`Pliss benerin settinganya` **HEROKU_APP_NAME** `variable"
                " Agar bisa mendeploy ironbot...`"
            )
            repo.__del__()
            return
        for app in heroku_applications:
            if app.name == HEROKU_APP_NAME:
                heroku_app = app
                break
        if heroku_app is None:
            await event.edit(
                f"{txt}\n" "`Gagal Heroku credentials untuk deploy ironbot dyno.`"
            )
            return repo.__del__()
        await event.edit(
            "`[IRONBOT]`" "\n⏳` Deploy proses, coba check .ping setelah 5 min... `⏳"
        )
        ups_rem.fetch(ac_br)
        repo.git.reset("--hard", "FETCH_HEAD")
        heroku_git_url = heroku_app.git_url.replace(
            "https://", "https://api:" + HEROKU_API_KEY + "@"
        )
        if "heroku" in repo.remotes:
            remote = repo.remote("heroku")
            remote.set_url(heroku_git_url)
        else:
            remote = repo.create_remote("heroku", heroku_git_url)
        try:
            remote.push(refspec="HEAD:refs/heads/master", force=True)
        except Exception as error:
            await event.edit(f"{txt}\n`Here is the error log:\n{error}`")
            return repo.__del__()
        build = app.builds(order_by="created_at", sort="desc")[0]
        if build.status == "failed":
            await event.edit(
                "`Build gagal!\n" "gagal atau mungkin ada error...`"
            )
            await asyncio.sleep(5)
            return await event.delete()
        else:
            await event.edit("`Deploy berhasil!\n" "Lagi restart bentar, tunggu ya...`")
    else:
        await event.edit(
            "`[HEROKU]`\n" "`Please set up`  **HEROKU_API_KEY**  `variable...`"
        )
    return


async def update(event, repo, ups_rem, ac_br):
    try:
        ups_rem.pull(ac_br)
    except GitCommandError:
        repo.git.reset("--hard", "FETCH_HEAD")
    await update_requirements()
    await event.edit("🚧`-B-`🚧")
    await event.edit("🚧`-B E-`🚧")
    await event.edit("🚧`-B E R-`🚧")
    await event.edit("🚧`-B E R H-`🚧")
    await event.edit("🚧`-B E R H A-`🚧")
    await event.edit("🚧`-B E R H A S-`🚧")
    await event.edit("🚧`-B E R H A S I-`🚧")
    await event.edit("🚧`-B E R H A S I L-`🚧")
    await event.edit("🚧`-B E R H A S I L  U-`🚧")
    await event.edit("🚧`-B E R H A S I L  U P-`🚧")
    await event.edit("🚧`-B E R H A S I L  U P D-`🚧")
    await event.edit("🚧`-B E R H A S I L  U P D A-`🚧")
    await event.edit("🚧`-B E R H A S I L  U P D A T-`🚧")
    await event.edit("🚧`-B E R H A S I L  U P D A T E-`🚧")
    await asyncio.sleep(2)
    await event.edit("`Bot akan restart tunggu beberapa detik`")
    await asyncio.sleep(1)
    await event.delete()
    # Spin a new instance of bot
    args = [sys.executable, "-m", "ironbot"]
    execle(sys.executable, *args, environ)
    return


@iron.on(iron_on_cmd(pattern=r"update( now| deploy|$)"))
async def upstream(event):
    "Untuk .update command, mengecek apakah ada update"
    await event.edit("`⚙️Memgambil informasi....`")
    conf = event.pattern_match.group(1).strip()
    off_repo = UPSTREAM_REPO_URL
    force_update = False
    try:
        txt = "`Oops.. Updater tidak bisa berjalan "
        txt += "beberapa masalah ditemukan`\n\n**LOGTRACE:**\n"
        repo = Repo()
    except NoSuchPathError as error:
        await event.edit(f"{txt}\n`directory {error} is not found`")
        return repo.__del__()
    except GitCommandError as error:
        await event.edit(f"{txt}\n`Early failure! {error}`")
        return repo.__del__()
    except InvalidGitRepositoryError as error:
        if conf is None:
            return await event.edit(
                f"`sayangnya, direktori {error} "
                "tampaknya bukan repositori git.\n"
                "Tapi kita bisa memperbaikinya dengan memperbarui paksa menggunakan ironbot "
                ".update now.`"
            )
        repo = Repo.init()
        origin = repo.create_remote("upstream", off_repo)
        origin.fetch()
        force_update = True
        repo.create_head("master", origin.refs.master)
        repo.heads.master.set_tracking_branch(origin.refs.master)
        repo.heads.master.checkout(True)

    ac_br = repo.active_branch.name
    if ac_br != UPSTREAM_REPO_BRANCH:
        await event.edit(
            "**[UPDATER]:**\n"
            f"`Sepertinya Anda menggunakan branch kustom Anda sendiri ({ac_br}). "
            "Dalam hal ini, Updater tidak dapat mengidentifikasi"
            "Branch mana yang akan digabungkan."
            "Silakan periksa ke branch asli`"
        )
        return repo.__del__()
    try:
        repo.create_remote("upstream", off_repo)
    except BaseException:
        pass

    ups_rem = repo.remote("upstream")
    ups_rem.fetch(ac_br)

    changelog = await gen_chlog(repo, f"HEAD..upstream/{ac_br}")
    """ - Special case for deploy - """
    if conf == "deploy":
        await event.edit("`⚡Deploying ironbot, check .alive jika sudah 5-10min...`")
        await deploy(event, repo, ups_rem, ac_br, txt)
        return

    if changelog == "" and not force_update:
        await event.edit(
            "\n`➰ Ironbot Info ➰`\n\n🔺 `Versi   :`  **terbaru** 🔺\n🔺 `Base on :`  "
            f"**{UPSTREAM_REPO_BRANCH}** 🔺\n"
        )
        await asyncio.sleep(3)
        await event.delete()
        return repo.__del__()

    if conf == "" and not force_update:
      #  await print_changelogs(event, ac_br, changelog)
       # await event.delete()
        await event.edit(f"** ADA UPDATE BOSS **\n`Base on :` [{ac_br}]\n\n**PERUBAHAN INFO:**\n{changelog}\n`Ketik : .update now/.update deploy untuk update ironbot.`")
        await asyncio.sleep(3)
        await event.delete()
       # await event.respond("`Ketik : .update now/.update deploy untuk update ironbot.`")

    if force_update:
        await event.edit(
            "`Force sync untuk ironbot,\ntunggu ya...`🛠️"
        )
        await update(event, repo, ups_rem, ac_br)
        await asyncio.sleep(4)
        await event.delete()
    if conf == "now":
        await asyncio.sleep(.1)
        await event.edit("`• Proses update ironbot\n• Sabar ya.🛠️`")
        await asyncio.sleep(.1)
        await event.edit("`• Proses update ironbot\n• Sabar ya..🛠️`")
        await asyncio.sleep(.1)
        await event.edit("`• Proses update ironbot\n• Sabar ya...🛠️`")
        await asyncio.sleep(.1)
        await event.edit("`• Proses update ironbot\n• Sabar ya....🛠️`")
        await asyncio.sleep(.1)
        await event.edit("`• Proses update ironbot\n• Sabar ya.....🛠️`")
        await update(event, repo, ups_rem, ac_br)
    return


@borg.on(iron_on_cmd(pattern="help ?(.*)"))
async def cmd_list(event):
    if event.fwd_from:
        return
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        sedstark = await tgbot.get_me()
        tgbotusername = sedstark.username
        input_str = event.pattern_match.group(1)
        if tgbotusername is None or input_str == "text":
            string = ""
            for i in CMD_LIST:
                string += "ℹ️ " + i + "\n"
                for iter_list in CMD_LIST[i]:
                    string += "    `" + str(iter_list) + "`"
                    string += "\n"
                string += "\n"
            if len(string) > 4095:
                await borg.send_message(event.chat_id, "Do .help cmd")
                await asyncio.sleep(5)
            else:
                await event.edit(string)
        elif input_str:
            if input_str in CMD_LIST:
                string = "Commands found in {}:\n".format(input_str)
                for i in CMD_LIST[input_str]:
                    string += "    " + i
                    string += "\n"
                await event.edit(string)
            else:
                await event.edit(input_str + " is not a valid plugin!")
        else:
            help_string = """IRON Userbot Modules Are Listed Here !\n
For More Help or Support Visit @freedom_reborn"""
            results = await bot.inline_query(  # pylint:disable=E0602
                tgbotusername, help_string
            )
            await results[0].click(
                event.chat_id, reply_to=event.reply_to_msg_id, hide_via=True
            )
            await event.delete()
            
CMD_HELP.update(
    {
        "update": ">`.update`"
        "\nUsage: Checks if the main userbot repository has any updates "
        "and shows a changelog if so."
        "\n\n>`.update now`"
        "\nUsage: Performs a quick update."
        "\n\n>`.update deploy`"
        "\nUsage: Performs a full update (recommended)."
    }
)
CMD_HELP.update(
    {
        "ping": "**Ping**\
\n\n**Syntax : **`.ping`\
\n**Usage :** Get uptime and speed of your bot."
    }
)
CMD_HELP.update(
    {
        "alive": "**ALive**\
\n\n**Syntax : **`.alive`\
\n**Usage :** Check if UserBot is Alive"
    }
)
