import logging
from telegram.ext import (
    ApplicationBuilder, CommandHandler,
    MessageHandler, filters
)
from config import TELEGRAM_BOT_TOKEN
from handlers.text_handler import handle_text
from handlers.image_handler import handle_image
from handlers.file_handler import handle_file

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def start(update, context):
    await update.message.reply_text(
        "🎓 **Trợ lý AI Đại học**\n\n"
        "Xin chào! Mình có thể giúp bạn:\n"
        "• Giải bài tập (Toán, Lý, Hóa, CNTT...)\n"
        "• Giải thích đề tài, khái niệm\n"
        "• Phân tích ảnh / file bài tập\n\n"
        "👉 Gửi câu hỏi, ảnh hoặc file để bắt đầu.",
        parse_mode="Markdown"
    )

app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.PHOTO, handle_image))
app.add_handler(MessageHandler(filters.Document.ALL, handle_file))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))

if __name__ == "__main__":
    logger.info("🤖 Bot AI Đại học đang hoạt động...")
    app.run_polling()
