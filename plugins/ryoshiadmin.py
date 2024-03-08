# EdBebop - UserBot
# Copyright (C) 2024 WegegtaTech
#
# This file is a part of < https://github.com/NehemiahAklil/EdBebop/>
# PLease read the GNU Affero General Public License in
# <https://www.github.com/NehemiahAklil/EdBebop/blob/main/LICENSE/>.
# from . import get_help

# __doc__ = get_help("help_ryoshiadmin")

from telethon.errors import BadRequestError
from . import eor, get_string
from telethon.events import NewMessage 
from . import get_string, ultroid_bot,ultroid_cmd

@ultroid_bot.on(NewMessage(chats=[-1001437225779,-1001312396621],
                from_users=[1029642148,618096097,175844556,797954152], 
                   pattern='(?i)#players\:+'
                   ),
)
async def autopin(event):
    chat_id = event.chat_id
    message_id = event.message.id
    text = f"<b> ꧁ Autopin Players List ꧂ </b>"
    # Pin the message
    try:
        await event.client.pin_message(chat_id, message_id,notify=False,)
    except BadRequestError:
        return await eor(event, get_string("adm_2"))
    except Exception as e:
        return await eor(event, f"**ERROR:**`{e}`")
    await eor(event, text,parse_mode="html",time=10)



@ultroid_cmd(pattern="e( (.*)|$)", manager=True)
async def extend(event):
    raw_sec = event.pattern_match.group(1).strip()
    sec = 30
    if raw_sec == "":
        raw_sec = ""
    else:
        try:
            sec = int(raw_sec)
        except ValueError:
            return await eor(event, "ww extend command only accepts seconds in ints dummy")
    
    await event.delete()
    await event.client.send_message(event.chat_id, f"/extend {sec}")

@ultroid_cmd(pattern="kg", manager=True)
async def kill_game(event):
    await event.delete()
    await event.client.send_message(event.chat_id, f"/killgame")


@ultroid_cmd(pattern="fsg", manager=True)
async def force_start_game(event):
    await event.delete()
    await event.client.send_message(event.chat_id,f"/forcestart")


@ultroid_cmd(pattern="nxt( (.*)|$)", manager=True)
async def next_game(event):
    bot_type = event.pattern_match.group(1).strip()
    
    if not bot_type.isdigit(): 
            bot_type="blackwerewolfbot" 
    else:
        match int(bot_type):
                case 1:
                    bot_type=" " 
                case 2:
                    bot_type="Blackwwrobot"
                case 3:
                    bot_type="werewolfbot"
                case _:
                    bot_type="blackwerewolfbot" 

    bot_payload ='' if bot_type.isspace() else f'@{bot_type}'
    return await eor(event,f"/nextgame{bot_payload}")

@ultroid_cmd(pattern="st( (.*)|$)", manager=True)
async def start_game(event):
    try:
        game_type = event.pattern_match.group(1).split(" ")[1]
    except IndexError:
        game_type = "" 
    try:
        bot_type = event.pattern_match.group(1).split(" ")[2]
    except IndexError:
        bot_type = "" 
    if not bot_type.isdigit(): 
            bot_type="blackwerewolfbot" 
    else:
        match int(bot_type):
                case 1:
                    bot_type=" " 
                case 2:
                    bot_type="Blackwwrobot"
                case 3:
                    bot_type="werewolfbot"
                case _:
                    bot_type="blackwerewolfbot" 

    bot_payload ='' if bot_type.isspace() else f'@{bot_type}'

    match(game_type.strip()):
        case "m":
            msg = f"/startmighty{bot_payload}"
        case "n":
            msg = f"/startgame{bot_payload}"
        case "clt":
            msg = f"/startcultus{bot_payload}"
        case "cls":
            msg = f"/startclassic{bot_payload}"
        case "c":
            msg = f"/startchaos{bot_payload}"
        case "mx":
           msg = f"/startmax{bot_payload}"
        case "w":
           msg = f"/startwolves{bot_payload}"
        case "r":
           msg = f"/startromance{bot_payload}"
        case "f":
           msg = f"/startfoolish{bot_payload}"
        case _:
            msg = f"/startmighty{bot_payload}"
    
    await event.delete()
    await event.client.send_message(event.chat_id, msg)
