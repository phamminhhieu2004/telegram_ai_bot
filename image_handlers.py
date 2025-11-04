import os
from telegram import Update
from telegram.ext import ContextTypes
from utils.ai_client import AIClient

ai = AIClient()

async def handle_image(update: Update, context: ContextTypes.DEFAULT_TYPE):
    photo = update.message.photo[-1]
    file = await photo.get_file()
    path = f"temp_{update.message.from_user.id}.jpg"
    await file.download_to_drive(path)

    await update.message.reply_chat_action("typing")
    try:
        reply = ai.analyze_image(os.path.abspath(path))
        await update.message.reply_text(reply, parse_mode="Markdown")
    except Exception as e:
        await update.message.reply_text("❌ Không thể phân tích ảnh.")
        print(e)
    finally:
        os.remove(path)
