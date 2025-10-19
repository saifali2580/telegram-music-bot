from pyrogram import Client, filters
from pytgcalls import PyTgCalls, idle
from pytgcalls.types.input_stream import AudioPiped
import yt_dlp
import os

# ===============================
API_ID = "ضع_هنا_API_ID"
API_HASH = "ضع_هنا_API_HASH"
STRING_SESSION = "ضع_هنا_STRING_SESSION"
# ===============================

app = Client(session_name=STRING_SESSION, api_id=API_ID, api_hash=API_HASH)
pytgcalls = PyTgCalls(app)

# أمر تشغيل ملف موجود مسبقاً
@app.on_message(filters.text & filters.group)
async def play_file(client, message):
    text = message.text.split()
    if text[0] == "شغل":
        if len(text) < 2:
            await message.reply_text("اكتب اسم الملف الصوتي لتشغيله")
            return
        filename = text[1]
        if not os.path.exists(filename):
            await message.reply_text("الملف مو موجود 😕")
            return
        chat_id = message.chat.id
        pytgcalls.join_group_call(chat_id, AudioPiped(filename))
        await message.reply_text(f"شغلت الملف: {filename} ✅")

# أمر تحميل أغنية من يوتيوب وتشغيلها
@app.on_message(filters.text & filters.group)
async def play_youtube(client, message):
    text = message.text.split()
    if text[0] == "يوت":
        if len(text) < 2:
            await message.reply_text("اكتب رابط اليوتيوب")
            return
        url = text[1]
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

# أمر إيقاف التشغيل
@app.on_message(filters.text & filters.group)
async def stop(client, message):
    if message.text == "ايقاف":
        chat_id = message.chat.id
        await pytgcalls.leave_group_call(chat_id)
        await message.reply_text("تم إيقاف الصوت ✅")

# تشغيل البوت
async def main():
    await app.start()
    await pytgcalls.start()
    print("بوت الموسيقى شغال ✅")
    await idle()
    await app.stop()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
