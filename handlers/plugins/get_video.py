from telethon import events
from telethon.tl.types import DocumentAttributeVideo
import ffmpeg
from ffmpy import FFmpeg
from handlers.tools import soup, convert_size, download_video, clear
import os
from random import randint


convert = convert_size.convert_size


@events.register(events.NewMessage(outgoing=True, pattern=r"https"))
async def cmd(event):
    clear.clear()
    client = event.client
    entity = await event.get_chat()
    msg = event.message

    link_video = event.message.message

    link_soup = soup.soup(link_video)
    if link_soup:
        msg = await client.send_message(entity=entity, message="Downloading ...")

        async def callback(current, total):
            message = await client.get_messages(entity, ids=msg.id)

            percent = (current / total) * 100

            if 20.0 < percent < 30.0:
                if message.text == "Downloading ...":
                    await client.edit_message(
                        entity, msg.id, text=f"'Uploaded 25 out of', {convert(total)}"
                    )

            elif 50.0 < percent < 60.0:
                if message.text == f"'Uploaded 25 out of', {convert(total)}":
                    await client.edit_message(
                        entity, msg.id, text=f"'Uploaded 50 out of', {convert(total)}"
                    )

            elif 70.0 < percent < 80.0:
                if message.text == f"'Uploaded 50 out of', {convert(total)}":
                    await client.edit_message(
                        entity, msg.id, text=f"'Uploaded 75 out of', {convert(total)}"
                    )

            elif 80.0 < percent < 95.0:
                if message.text == f"'Uploaded 75 out of', {convert(total)}":
                    await client.edit_message(
                        entity, msg.id, text=f"'Uploaded 95 out of', {convert(total)}"
                    )

        download_video.download_video_ydl(link_soup)

        video = list(filter(lambda x: x.endswith(".mp4"), os.listdir(".")))[0]

        info = ffmpeg.probe(video)["streams"]
        height = info[0]["coded_height"]
        width = info[0]["coded_width"]
        duration = info[0]["duration"]

        ff = FFmpeg(
            inputs={video: None},
            outputs={"output.png": ["-ss", "00:00:02", "-vframes", "1"]},
        )
        ff.run()

        await client.send_file(
            entity=entity,
            file=video,
            progress_callback=callback,
            attributes=(
                DocumentAttributeVideo(
                    int(float(duration)), width, height, supports_streaming=True
                ),
            ),
            thumb="output.png",
        )

        await client.delete_messages(entity, msg)
        clear.clear()
    else:
        await client.send_message(entity, link_soup)
