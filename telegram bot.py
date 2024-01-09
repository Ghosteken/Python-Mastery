# pip install python-telegram-bot

# from telegram import Update
# from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# # Replace 'YOUR_BOT_TOKEN' with the token you got from the BotFather
# TOKEN = 'YOUR_BOT_TOKEN'

# def start(update: Update, context: CallbackContext) -> None:
#     update.message.reply_text('Hello! I am your bot.')

# def echo(update: Update, context: CallbackContext) -> None:
#     update.message.reply_text(update.message.text)

# def main() -> None:
#     updater = Updater(TOKEN)
#     dp = updater.dispatcher

#     dp.add_handler(CommandHandler("start", start))
#     dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

#     updater.start_polling()

#     updater.idle()

# if __name__ == '__main__':
#     main()
