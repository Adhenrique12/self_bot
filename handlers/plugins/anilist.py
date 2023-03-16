from telethon import events


@events.register(events.NewMessage(outgoing=True, pattern=r".anilist"))
async def cmd(event):
    client = event.client
    entity = await event.get_chat()
    event_msg = event.message
    msg_id = event.id

    msg = await client.get_messages(entity, ids=msg_id)
    print(msg.message)
