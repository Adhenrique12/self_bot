from telethon import events
from handlers.tools import convert_size
import time

convert = convert_size.convert_size


def get_info(msg: str, msg_id: int) -> str:
    media = msg.media.document
    media_size = convert(media.size)
    media_type = media.mime_type

    time_format = time.strftime(
        "%M:%S", time.gmtime(media.attributes[0].duration))

    info = (
        f"id: {msg_id} \ntype: {media_type} \ntime: {time_format} \nsize: {media_size}"
    )
    return info


@events.register(events.NewMessage(outgoing=True, pattern=r".info"))
async def cmd(event):
    client = event.client
    entity = await event.get_chat()
    event_msg = event.message

    msg_id = event_msg.reply_to.reply_to_msg_id
    msg = await client.get_messages(entity, ids=msg_id)

    info = get_info(msg, msg_id)

    await client.edit_message(entity, event_msg, info)
    print(await client.get_peer_id("me"))

    print(info)
