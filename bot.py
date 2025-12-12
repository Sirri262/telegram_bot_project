import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "7819757152:AAH56vlN7XvSbhFG4VkmeNuD-n7VZcHMVhw"

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hello! 🤖 The bot is running!\nAll your messages will be automatically handled by n8n."
    )

async def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("Bot is running with Telegram Trigger (n8n handles messages)...")
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())