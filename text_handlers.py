from telegram import Update
from telegram.ext import ContextTypes
from utils.ai_client import AIClient

ai = AIClient()

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text
    await update.message.reply_chat_action("typing")
    try:
        reply = ai.chat(user_input)
        await update.message.reply_text(reply, parse_mode="Markdown")
    except Exception as e:
        await update.message.reply_text("⚠️ Đã xảy ra lỗi khi xử lý yêu cầu của bạn.")
        print(e)
