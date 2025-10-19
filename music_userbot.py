import os
import asyncio
from pyrogram import Client, filters
from pytgcalls import PyTgCalls, idle
from pytgcalls.types.input_stream import AudioPiped
import yt_dlp

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
STRING_SESSION = os.environ.get("STRING_SESSION")

app = Client(STRING_SESSION, api_id=API_ID, api_hash=API_HASH)
pytgcalls = PyTgCalls(app)

@app.on_message(filters.group & filters.text)
async def play_file(client, message):
    if message.text.startswith("شغل "):
        filename = message.text.replace("شغل ", "").strip()
        if not os.path.exists(filename):
            await message.reply_text("الملف مو موجود 😕")
            return
        chat_id = message.chat.id
        pytgcalls.join_group_call(chat_id, AudioPiped(filename))
        await message.reply_text(f"شغلت الملف: {filename} ✅")

@app.on_message(filters.group & filters.text)
async def play_youtube(client, message):
    if message.text.startswith("يوت "):
        url = message.text.replace("يوت ", "").strip()
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': 'audio.%(ext)s',
            'noplaylist': True
        }
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                filename = ydl.prepare_filename(info)
        except Exception as e:
            await message.reply_text(f"خطأ بالتحميل: {e}")
            return
        chat_id = message.chat.id
        pytgcalls.join_group_call(chat_id, AudioPiped(filename))
        await message.reply_text(f"شغلت: {info['title']} ✅")

@app.on_message(filters.group & filters.text)
async def stop(client, message):
    if message.text.strip() == "ايقاف":
        chat_id = message.chat.id
        await pytgcalls.leave_group_call(chat_id)
        await message.reply_text("تم إيقاف الصوت ✅")

async def main():
    await app.start()
    await pytgcalls.start()
    print("بوت الموسيقى شغال ✅")
    await idle()
    await app.stop()

if __name__ == "__main__":
    asyncio.run(main())
