import asyncio
import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pytgcalls import PyTgCalls
from pytgcalls.types import AudioVideoPiped
from yt_dlp import YoutubeDL
import config # استدعاء ملف الإعدادات

# تشغيل البوت والحساب المساعد
bot = Client("MusicBot", api_id=config.API_ID, api_hash=config.API_HASH, bot_token=config.BOT_TOKEN)
assistant = Client("AssistantAccount", api_id=config.API_ID, api_hash=config.API_HASH, session_string=config.STRING_SESSION)
call_py = PyTgCalls(assistant)

# إعدادات تحميل الصوت من يوتيوب
ydl_opts = {"format": "bestaudio/best", "outtmpl": "downloads/%(id)s.%(ext)s", "quiet": True}

def search_and_download(query):
    with YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(f"ytsearch:{query}", download=True)["entries"][0]
            return ydl.prepare_filename(info), info["title"]
        except Exception:
            return None, None

# أمر الـ start بالواجهة اللي طلبتها
@bot.on_message(filters.command("start") & filters.private)
async def start_command(client, message):
    text = (
        "• اهلا بك في بوت الميوزك\n\n"
        "• بوت خاص لتشغيل الأغاني الصوتية والمرئية\n"
        "• قم بإضافة البوت إلى مجموعتك أو قناتك\n"
        "• سيتم تفعيل البوت وانضمام المساعد تلقائياً"
    )
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("طريقة الاستخدام", callback_data="help_data")],
        [InlineKeyboardButton("المطور ↗️", url="https://t.me/DowzC"),
         InlineKeyboardButton("اضفني +", url=f"https://t.me/{client.me.username}?startgroup=true")],
        [InlineKeyboardButton("SOURCE DOWZ ↗️", url="https://github.com/saifali2580/telegram-music-bot")]
    ])
    await message.reply_text(text, reply_markup=keyboard)

# أوامر التشغيل والتحكم
@bot.on_message(filters.command(["شغل", "تشغيل"]) & filters.group)
async def play_audio(client, message):
    if len(message.command) < 2:
        return await message.reply_text("• يرجى كتابة اسم الأغنية. مثال: `شغل إليسا`")
    query = message.text.split(None, 1)[1]
    msg = await message.reply_text("🔍 جاري البحث والتحميل...")
    
    loop = asyncio.get_event_loop()
    file_path, title = await loop.run_in_executor(None, search_and_download, query)
    
    if not file_path:
        return await msg.edit("❌ لم يتم العثور على الأغنية.")
        
    try:
        await call_py.join_group_call(message.chat.id, AudioVideoPiped(file_path))
        await msg.edit(f"🎵 جاري تشغيل: **{title}**")
    except Exception as e:
        await msg.edit(f"❌ خطأ في التشغيل: {e}")

@bot.on_message(filters.command("ايقاف") & filters.group)
async def stop_audio(client, message):
    try:
        await call_py.leave_group_call(message.chat.id)
        await message.reply_text("⏹️ تم إيقاف التشغيل ومغادرة المساعد.")
    except Exception:
        await message.reply_text("• المساعد ليس في المكالمة.")

@bot.on_message(filters.command("كتم") & filters.group)
async def mute_assistant(client, message):
    try:
        await call_py.change_volume_call(message.chat.id, 0)
        await message.reply_text("🔇 تم كتم الصوت.")
    except Exception:
        await message.reply_text("• المساعد ليس في المكالمة.")

@bot.on_message(filters.command("تحدث") & filters.group)
async def unmute_assistant(client, message):
    try:
        await call_py.change_volume_call(message.chat.id, 100)
        await message.reply_text("🔊 تم إلغاء الكتم.")
    except Exception:
        await message.reply_text("• المساعد ليس في المكالمة.")

async def main():
    await bot.start()
    await assistant.start()
    await call_py.start()
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())

