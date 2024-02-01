
# from . import get_help

# __doc__ = get_help("help_admintools")

from telethon.errors import BadRequestError
from . import eor, get_string
from telethon.events import NewMessage 
from . import get_string, ultroid_bot

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

