#Import libraries
from telegram.ext import Updater,MessageHandler,Filters,CallbackContext,CommandHandler,CallbackQueryHandler
from telegram import Update,ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardButton,InlineKeyboardMarkup
from like_db import LikeDB

#Import TOKEN from envoirment variable
import os
TOKEN = os.environ['TOKEN']

#Create start command handler
def start(update:Update, context:CallbackContext):
    """Starts with picture all likes and all dislikes"""
    pass

def like(update:Update, context:CallbackContext):
    """Send the message with the number of likes and dislikes"""
    pass

def dislike(update:Update, context:CallbackContext):
    """Send the message with the number of likes and dislikes"""
    pass

#Create updater and dispatcher
updater = Updater(TOKEN)

#add handler to updater
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CallbackQueryHandler(like, pattern='like'))
updater.dispatcher.add_handler(CallbackQueryHandler(dislike, pattern='dislike'))

#Start the bot
updater.start_polling()
updater.idle()



