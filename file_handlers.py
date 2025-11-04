import os
from telegram import Update
from telegram.ext import ContextTypes
from utils.ai_client import AIClient

ai = AIClient()

async def handle_file(update: Update, context: ContextTypes.DEFAULT_TYPE):
    doc = update.message.document
    file = await doc.get_file()
    path = f"temp_{update.message.from_user.id}_{doc.file_name}"
    await file.download_to_drive(path)

    if os.path.getsize(path) > 3 * 1024 * 1024:
        await update.message.reply_text("⚠️ File quá lớn (giới hạn 3MB).")
        os.remove(path)
        return

    await update.message.reply_chat_action("typing")
    try:
        reply = ai.chat(f"Hãy đọc và giải thích nội dung của file {doc.file_name}.")
        await update.message.reply_text(reply, parse_mode="Markdown")
    except Exception as e:
        await update.message.reply_text("❌ Không thể xử lý file.")
        print(e)
    finally:
        os.remove(path)
