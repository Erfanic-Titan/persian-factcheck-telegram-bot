from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackQueryHandler
from config.config import Config
from .handlers.command_handlers import start_command, help_command
from .handlers.message_handlers import (
    handle_text,
    handle_image,
    handle_video,
    handle_audio,
    handle_document
)
from .handlers.callback_handlers import handle_callback_query

async def run_bot():
    """Initialize and run the bot"""
    # Create application
    application = Application.builder().token(Config.BOT_TOKEN).build()

    # Add handlers
    # Command handlers
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("help", help_command))

    # Message handlers
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))
    application.add_handler(MessageHandler(filters.PHOTO, handle_image))
    application.add_handler(MessageHandler(filters.VIDEO, handle_video))
    application.add_handler(MessageHandler(filters.AUDIO | filters.VOICE, handle_audio))
    application.add_handler(MessageHandler(filters.Document.ALL, handle_document))

    # Callback query handler
    application.add_handler(CallbackQueryHandler(handle_callback_query))

    # Start the bot
    await application.initialize()
    await application.start()
    await application.run_polling()