from deep_translator import GoogleTranslator
from googletrans import LANGUAGES
from google_trans_new import google_translator
from langdetect import detect
import requests
from ironbot import CMD_HELP
from ironbot.utils import edit_or_reply, iron_on_cmd, sudo_cmd


@iron.on(iron_on_cmd("tr ?(.*)"))
@iron.on(sudo_cmd("tr ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if "trim" in event.raw_text:
        return
    input_str = event.pattern_match.group(1)
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        text = previous_message.message
        lan = input_str or "id"
    elif "|" in input_str:
        lan, text = input_str.split("|")
    else:
        await edit_or_reply(event, "`.tr <Language-code>` as reply to a message")
        return

    lan = lan.strip()
    try:
        translator = google_translator()
        translated = translator.translate(text ,lang_tgt=lan)
        lmao_bruh = text
        lmao = detect(text)
        after_tr_text = lmao
        source_lan = LANGUAGES[after_tr_text]
        transl_lan = LANGUAGES[lan]
        output_str = f"""**TRANSLATED SUCCESSFULLY**
**Source ({source_lan})**:
`{text}`

**Translation ({transl_lan})**:
`{translated}`"""
      
        if len(output_str) >= 4096:
            out_file = output_str
            url = "https://del.dog/documents"
            r = requests.post(url, data=out_file.encode("UTF-8")).json()
            url2 = f"https://del.dog/{r['key']}"
            starky = f"Translated Text Was Too Big, Never Mind I Have Pasted It [Here]({url2})"
        else:
            starky = output_str
        await edit_or_reply(event, starky)
    except:
        translator = google_translator()
        translated = translator.translate(text ,lang_tgt=lan)
        lmao_bruh = text
        lmao = translator.detect(text)
        after_tr_text = lmao
        source_lano = translator.detect(text)
        try:
           source_lan = source_lano[1]
        except:
           source_lan = source_lano[0]
        output_str = f"""**TRANSLATED SUCCESSFULLY**
**Source ({source_lan})**:
`{text}`

**Translation ({lan})**:
`{translated}`"""
      
        if len(output_str) >= 4096:
            out_file = output_str
            url = "https://del.dog/documents"
            r = requests.post(url, data=out_file.encode("UTF-8")).json()
            url2 = f"https://del.dog/{r['key']}"
            starky = f"Translated Text Was Too Big, Never Mind I Have Pasted It [Here]({url2})"
        else:
            starky = output_str
        await edit_or_reply(event, starky)

CMD_HELP.update(
    {
        "translate": "**Translate**\
\n\n**Syntax : **`.tr <language Code> <reply to text>`\
\n**Usage :** Translates the given text into your language."
    }
)
