from ironbot.Configs import Config
from ironbot.utils import iron_on_cmd
from ironbot.Configs import Config
issudousing = Config.SUDO_USERS
islogokay = Config.PRIVATE_GROUP_ID
isdbfine = Config.DB_URI
isherokuokay = Config.HEROKU_APP_NAME
gdriveisshit = Config.AUTH_TOKEN_DATA
wttrapi = Config.OPEN_WEATHER_MAP_APPID
rmbg = Config.REM_BG_API_KEY
hmmok = Config.LYDIA_API
currentversion = "1.0"
if issudousing:
    amiusingsudo = "Aktif✅"
else:
    amiusingsudo = "Inactive ❌"

if islogokay:
    logchat = "Connected ✅"
else:
    logchat = "Dis-Connected ❌"

if isherokuokay:
    riplife = "Connected ✅"
else:
    riplife = "Not Connected ❌"

if gdriveisshit:
    wearenoob = "Active ✅"
else:
    wearenoob = "Inactive ❌"

if rmbg:
    gendu = "Added ✅"
else:
    gendu = "Not Added ❌"

if wttrapi:
    starknoobs = "Added ✅"
else:
    starknoobs = "Not Added ❌"

if hmmok:
    meiko = "Added ✅"
else:
    meiko = "Not Added ❌"

if isdbfine:
    dbstats = "Fine ✅"
else:
    dbstats = "Not Fine ❌"

inlinestats = (
    f"✘ SHOWING IRONBOT STATS ✘\n"
    f"VERSION    = {currentversion} \n"
    f"DATABASE  = {dbstats} \n"
    f"SUDOUSER  = {amiusingsudo} \n"
    f"LOGCHAT   = {logchat} \n"
    f"HEROKU.    = {riplife} \n"
    f"GDRIVE.     = {wearenoob}\n"
    f"RMBG.      = {gendu}"
)
