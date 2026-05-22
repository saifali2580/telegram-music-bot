import asyncio
import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pytgcalls import PyTgCalls
from pytgcalls.types import AudioVideoPiped
from yt_dlp import YoutubeDL
import config # استدعاء ملف الإعدادات

# تنفيـذ البوت والحساب المساعد
bot = Client("MusicBot", api_id=config.API_ID, api_hash=config.API_HASH, bot_token=config.BOT_TOKEN)
assistant = Client("AssistantAccount", api_id=config.API_ID, api_hash=config.API_HASH, session_string=config.STRING_SESSION)
call_py = PyTgCalls(assistant)

# قائمة مؤقتة لحفظ آيديهات المجموعات المفعلة لمعرفة الإحصائيات والإذاعة
# (ملاحظة: السورس الاحترافي يحتاج لقاعدة بيانات مستقبلاً لتخزينها دائماً)
ACTIVATED_CHATS = set()

# إعدادات تحميل الصوت من يوتيوب
ydl_opts = {
    "format": "bestaudio/best",
    "outtmpl": "downloads/%(id)s.%(ext)s",
    "geo_bypass": True,
    "nocheckcertificate": True,
    "quiet": True
}

def search_and_download(query):
    with YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(f"ytsearch:{query}", download=True)["entries"][0]
            return ydl.prepare_filename(info), info["title"]
        except Exception:
            return None, None

# فلتر مخصص للتأكد من أن مستخدم الأمر هو المطور فقط
def is_owner(_, __, message):
    return message.from_user and message.from_user.id == config.OWNER_ID
owner_filter = filters.create(is_owner)


# ====== واجهة الـ /start ======
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


# ====== أوامر التشغيل والتحكم داخل المجموعات ======

@bot.on_message(filters.command(["شغل", "تشغيل"]) & filters.group)
async def play_audio(client, message):
    if len(message.command) < 2:
        return await message.reply_text("• يرجى كتابة اسم الأغنية بعد الأمر. مثال: `شغل إليسا`")
        
    chat_id = message.chat.id
    ACTIVATED_CHATS.add(chat_id) # حفظ المجموعة في الإحصائيات عند التشغيل
    
    query = message.text.split(None, 1)[1]
    msg = await message.reply_text("🔍 جاري البحث والتحميل من يوتيوب...")
    
    loop = asyncio.get_event_loop()
    file_path, title = await loop.run_in_executor(None, search_and_download, query)
    
    if not file_path:
        return await msg.edit("❌ لم يتم العثور على الأغنية أو حدث خطأ بالتحميل.")
        
    try:
        await call_py.join_group_call(chat_id, AudioVideoPiped(file_path))
        await msg.edit(f"🎵 جاري تشغيل: **{title}** عبر الحساب المساعد.")
    except Exception as e:
        await msg.edit(f"❌ خطأ في التشغيل والانضمام للمكالمة: {e}")
        if os.path.exists(file_path):
            os.remove(file_path)

@bot.on_message(filters.command("ايقاف") & filters.group)
async def stop_audio(client, message):
    try:
        await call_py.leave_group_call(message.chat.id)
        await message.reply_text("⏹️ تم إيقاف التشغيل بنجاح ومغادرة المساعد.")
    except Exception:
        await message.reply_text("• المساعد ليس في المكالمة حالياً.")

@bot.on_message(filters.command("كتم") & filters.group)
async def mute_assistant(client, message):
    try:
        await call_py.change_volume_call(message.chat.id, 0)
        await message.reply_text("🔇 تم كتم صوت الحساب المساعد.")
    except Exception:
        await message.reply_text("• المساعد ليس في المكالمة حالياً.")

@bot.on_message(filters.command("تحدث") & filters.group)
async def unmute_assistant(client, message):
    try:
        await call_py.change_volume_call(message.chat.id, 100)
        await message.reply_text("🔊 تم إلغاء الكتم، المساعد يتحدث الآن.")
    except Exception:
        await message.reply_text("• المساعد ليس في المكالمة حالياً.")


# ====== أوامر المطور الحصرية (Owner Commands) ======

@bot.on_message(filters.command("الاحصائيات") & owner_filter)
async def stats_command(client, message):
    total_chats = len(ACTIVATED_CHATS)
    await message.reply_text(f"📊 **إحصائيات سورس داوز:**\n\n• عدد المجموعات النشطة حالياً: {total_chats}")

@bot.on_message(filters.command("اذاعه") & owner_filter)
async def broadcast_command(client, message):
    if not message.reply_to_message:
        return await message.reply_text("• يرجى عمل رد (Reply) على الرسالة التي تريد إذاعتها.")
    
    msg = await message.reply_text("📢 جاري بدء الإذاعة في جميع المجموعات...")
    sent = 0
    
    for chat_id in ACTIVATED_CHATS:
        try:
            await message.reply_to_message.copy(chat_id)
            sent += 1
        except Exception:
            continue
            
    await msg.edit(f"✅ تم الانتهاء من الإذاعة بنجاح!\n• أُرسلت إلى {sent} مجموعة.")

@bot.on_message(filters.command("تنظيف") & owner_filter)
async def clean_downloads(client, message):
    folder = "downloads"
    if not os.path.exists(folder):
        return await message.reply_text("• مجلد التحميلات فارغ بالفعل.")
        
    deleted = 0
    for file in os.listdir(folder):
        file_path = os.path.join(folder, file)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
                deleted += 1
        except Exception:
            continue
            
    await message.reply_text(f"🧹 تم تنظيف السيرفر بنجاح!\n• تم حذف {deleted} من الملفات المؤقتة الصوتية.")


# دالة تشغيل السيرفر بالتزامن
async def main():
    await bot.start()
    await assistant.start()
    await call_py.start()
    print("🚀 سورس داوز المحدث جاهز للعمل مع أوامر المطور!")
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
