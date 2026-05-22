```markdown
# 🎵 بوت موسيقى تيليجرام | Telegram Music Bot v6

<p align="center">
  <b>سورس احترافي متكامل لبث وتشغيل الصوتيات داخل مكالمات تيليجرام</b>
</p>

<p align="center">
  <a href="https://github.com/saifali2580/telegram-music-bot/stargazers"><img src="https://img.shields.io/github/stars/saifali2580/telegram-music-bot?style=for-the-badge&color=yellow" alt="Stars"></a>
  <a href="https://github.com/saifali2580/telegram-music-bot/network/members"><img src="https://img.shields.io/github/forks/saifali2580/telegram-music-bot?style=for-the-badge&color=blue" alt="Forks"></a>
  <a href="https://github.com/saifali2580/telegram-music-bot/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License"></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python" alt="Python"></a>
</p>

---

## ✨ المميزات

- 🎧 **تشغيل عالي الجودة**: بث صوتي بدون تقطيع.
- 🔍 **بحث متعدد المنصات**: YouTube • SoundCloud • Spotify.
- 📜 **نظام Queue احترافي**: قائمة انتظار متقدمة مع حفظ دائم.
- ⏭️ **تخطي حقيقي**: تشغيل تلقائي للأغنية التالية.
- 🔐 **اشتراك إجباري**: حماية كاملة مع أزرار تحقق انلاين.
- 👑 **لوحة تحكم كاملة**: للمالك والمطورين بأزرار شفافة.
- 📢 **نظام إذاعة متقدم**: مع حماية من FloodWait.
- 🔄 **استعادة تلقائية**: استئناف التشغيل بعد إعادة التشغيل.
- 🗑️ **تنظيف تلقائي**: حذف الملفات المؤقتة دورياً.
- 🛡️ **حماية من السبام**: تحديد وقت بين الأوامر.
- 📊 **نظام سجلات (Logging)**: لمراقبة الأداء والأخطاء.
- 🤖 **حساب مساعد ذكي**: للانضمام التلقائي للمكالمات.
- 💾 **قاعدة بيانات SQLite**: حفظ دائم لجميع البيانات.

---

## 🛠️ جميع الأوامر

### 🎵 أوامر التشغيل (للمشرفين)

| الأمر | الوظيفة |
|--------|---------|
| `شغل` أو `play` + اسم الأغنية | البحث في يوتيوب والتشغيل مباشرة |
| `تخطي` أو `skip` | تخطي الأغنية الحالية وتشغيل التالية |
| `ايقاف` أو `stop` | إيقاف التشغيل ومسح قائمة الانتظار |
| `كتم` أو `mute` | كتم صوت المساعد داخل المكالمة |
| `تحدث` أو `unmute` | إلغاء الكتم وإعادة الصوت |

### 📜 أوامر قائمة الانتظار

| الأمر | الوظيفة |
|--------|---------|
| `كيو` أو `queue` | عرض قائمة الانتظار الحالية |
| `احذف` + رقم الأغنية | حذف أغنية محددة من القائمة |
| `مسح_الكيو` أو `clear` | مسح قائمة الانتظار بالكامل |

### ⚡ أوامر عامة

| الأمر | الوظيفة |
|--------|---------|
| `بنك` أو `ping` | فحص سرعة استجابة السيرفر |
| `/start` | عرض واجهة البوت الرئيسية |

### 👑 أوامر المالك (خاصة)

| الأمر | الوظيفة |
|--------|---------|
| `اضف` + ايدي | رفع مطور جديد للبوت |
| `حذف` + ايدي | تنزيل مطور من البوت |
| `تعيين` + اسم | تغيير اسم البوت |
| `تفعيل_اشتراك` + @معرف_القناة | تفعيل الاشتراك الإجباري |
| `تعطيل_اشتراك` | تعطيل الاشتراك الإجباري |
| `اذاعة` + رسالة | إرسال إذاعة لجميع المجموعات النشطة |

---

## 📋 المتطلبات (Requirements)

| المتطلب | الإصدار |
|----------|----------|
| Python | 3.9 أو أحدث |
| Pyrogram | 2.0.106 أو أحدث |
| PyTgCalls | 3.0.0.dev25 أو أحدث |
| yt-dlp | 2024.08.06 أو أحدث |
| FFmpeg | أي إصدار حديث |

---

## ☁️ النشر المباشر

### 🚀 النشر على Railway (بنقرة واحدة)

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/template/your-template-id)

**الخطوات:**
1. اضغط على زر النشر أعلاه.
2. سجل الدخول إلى Railway.
3. أضف المتغيرات (Variables):
   - `API_ID` - من my.telegram.org
   - `API_HASH` - من my.telegram.org
   - `BOT_TOKEN` - من @BotFather
   - `STRING_SESSION` - جلسة الحساب المساعد
   - `OWNER_ID` - ايديك الرقمي
4. انتظر حتى يكتمل النشر.

---

### 🐳 النشر باستخدام Docker

```bash
# بناء الصورة
docker build -t music-bot .

# تشغيل الحاوية
docker run -d --name music-bot \
  -e API_ID=123456 \
  -e API_HASH="your_api_hash" \
  -e BOT_TOKEN="your_bot_token" \
  -e STRING_SESSION="your_session" \
  -e OWNER_ID=123456789 \
  --restart always \
  music-bot
```

---

🖥️ النشر على VPS (سطر واحد)

```bash
git clone https://github.com/saifali2580/telegram-music-bot.git && cd telegram-music-bot && chmod +x setup.sh && sudo bash setup.sh
```

سكريبت setup.sh راح يسألك عن البيانات ويضبط كل شيء تلقائياً:

· تحديث النظام وتثبيت Python و FFmpeg
· تحميل المشروع وتثبيت المتطلبات
· إنشاء ملف config.env
· إعداد خدمة systemd للتشغيل 24/7

---

📁 هيكل المشروع

```
telegram-music-bot/
├── main.py                  # الملف الرئيسي - كود البوت
├── config.py                # ملف الإعدادات (يقرأ من متغيرات البيئة)
├── config.env.example       # قالب المتغيرات (للمستخدمين)
├── requirements.txt         # المكتبات المطلوبة
├── Dockerfile               # لبناء حاوية Docker
├── Procfile                 # أمر التشغيل للمنصات السحابية
├── setup.sh                 # سكريبت تنصيب تفاعلي كامل
├── .gitignore               # ملفات مستثناة من Git
├── README.md                # توثيق المشروع
├── music_bot.db             # قاعدة بيانات SQLite (تتكون تلقائياً)
└── downloads/               # مجلد التحميلات المؤقتة (يتكون تلقائياً)
```

---

❓ الأسئلة الشائعة (FAQ)

<details>
<summary><b>كيف أحصل على STRING_SESSION؟</b></summary>
<br>
يمكنك توليد جلسة Pyrogram باستخدام:
<br>
• تشغيل سكريبت بايروجرام محلياً على جهازك
<br>
• استخدام بوتات توليد الجلسات المتوفرة في تيليجرام
<br>
• استخدام موقع Replit لتشغيل كود توليد الجلسة
</details>

<details>
<summary><b>البوت لا ينضم للمكالمة الصوتية؟</b></summary>
<br>
تأكد من:
<br>
1. الحساب المساعد موجود في المجموعة
<br>
2. الحساب المساعد لديه صلاحية التحدث
<br>
3. STRING_SESSION صالحة ولم تنتهِ
<br>
4. تم رفع البوت والمساعد كمشرفين في القناة
</details>

<details>
<summary><b>كيف أضيف البوت إلى مجموعتي؟</b></summary>
<br>
1. اذهب إلى بوتك في تيليجرام
<br>
2. اضغط على اسم البوت
<br>
3. اختر "إضافة إلى مجموعة" وحدد المجموعة
<br>
4. تأكد من إضافة الحساب المساعد أيضاً إلى نفس المجموعة
</details>

---

👨‍💻 للمطورين

```bash
# استنساخ المستودع
git clone https://github.com/saifali2580/telegram-music-bot.git
cd telegram-music-bot

# إنشاء بيئة افتراضية
python3 -m venv venv
source venv/bin/activate

# تثبيت المتطلبات
pip install -r requirements.txt

# نسخ القالب وإضافة بياناتك
cp config.env.example config.env
nano config.env

# تشغيل البوت
source config.env && python3 main.py
```

---

📱 تواصل معنا

<p align="center">
  <a href="https://t.me/DowzC"><img src="https://img.shields.io/badge/Telegram-%40DowzC-blue?style=for-the-badge&logo=telegram"></a>
  <a href="https://t.me/wofkq"><img src="https://img.shields.io/badge/Channel-Dowz%20Source-red?style=for-the-badge&logo=telegram"></a>
  <a href="https://github.com/saifali2580"><img src="https://img.shields.io/badge/GitHub-saifali2580-black?style=for-the-badge&logo=github"></a>
</p>

---

📄 الترخيص

هذا المشروع مرخص تحت MIT License.

---

<p align="center">
  <b>صنع بـ ❤️ بواسطة <a href="https://t.me/DowzC">سيف - DowzC</a></b>
</p>
```

---
