import logging
from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def delete_stickers(update: Update, context: CallbackContext) -> None:
    message = update.message
    if message.sticker:
        message.delete()

def main() -> None:
    token = 'Your token telegram bot'
    
    updater = Updater(token, use_context=True)
    
    dispatcher = updater.dispatcher
    
    dispatcher.add_handler(MessageHandler(Filters.sticker, delete_stickers))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
