from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import openai

app = Flask(__name__)
openai.api_key = "YOUR_OPENAI_API_KEY"

RESPONSE_MAP = {
    "طالب": "أرسل رقم الخدمة من 1 إلى 10، حسب ما تحتاج كمساعد طالب 🎓.",
    "موظف": "أرسل رقم الخدمة من 1 إلى 10، حسب ما تحتاج كمساعد موظف 💼.",
    "1": "📧 تم إعداد إيميل رسمي (اعتراض للطالب).",
    "2": "📅 تم تجهيز جدول مذاكرة مناسب.",
    "3": "❓ تم تسجيل استفسارك الأكاديمي.",
    "4": "📤 أرسل النص المطلوب ترجمته.",
    "5": "📁 تم تجهيز طلب أو شكوى.",
    "6": "📧 تم إعداد إيميل رسمي (للموظف).",
    "7": "📅 تم تجهيز جدول مهام العمل.",
    "8": "📄 تم إعداد عذر رسمي.",
    "9": "📄 تم تجهيز سيرة ذاتية.",
    "10": "🧠 أرسل تفاصيل المهمة وسأساعدك فيها.",
}

WELCOME_MESSAGE = "👋 مرحباً بك في مساعدك الذكي عبدالله! هل أنت طالب أم موظف؟"

@app.route("/bot", methods=["POST"])
def bot():
    incoming_msg = request.values.get('Body', '').strip()
    resp = MessagingResponse()
    msg = resp.message()

    reply = RESPONSE_MAP.get(incoming_msg)

    if not reply:
        reply = WELCOME_MESSAGE

    msg.body(reply)
    return str(resp)
