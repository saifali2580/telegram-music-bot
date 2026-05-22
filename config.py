import os

# بيانات الاتصال الأساسية
API_ID = int(os.getenv("API_ID", "1234567")) # ضع الـ API ID الافتراضي هنا أو بالسيرفر
API_HASH = os.getenv("API_HASH", "your_api_hash")
BOT_TOKEN = os.getenv("BOT_TOKEN", "your_bot_token")
STRING_SESSION = os.getenv("STRING_SESSION", "your_string_session")

# آيدي المطور الأساسي للبوت (يتم سحبه تلقائياً عند التنصيب)
OWNER_ID = int(os.getenv("OWNER_ID", "your_telegram_id")) # ضع آيديك هنا كافتراضي
