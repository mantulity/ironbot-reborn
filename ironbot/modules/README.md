## IRONBOT
# EXAMPLE CODE !
```python3
from ironbot.utils import iron_on_cmd, sudo_cmd, edit_or_reply
from ironbot.Configs import Config
@iron.on(iron_on_cmd(pattern="alive"))
@iron.on(sudo_cmd(pattern="alive", allow_sudo=True))
async def hello_world(event):
    if event.fwd_from:
        return
    iron = await edit_or_reply(event, "Finding My Controllers....")
    await iron.edit("**HELLO WORLD**\n\nThe following is controlling me too!\n" + Config.SUDO_USERS)
```
