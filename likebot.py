#Import libraries
from telegram.ext import Updater,CommandHandler,CallbackContext,MessageHandler,Filters,CallbackQueryHandler
from telegram import Update,ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton
from like_db import LikeDB

#Import TOKEN from envoirment variable
TOKEN = '5549407151:AAGVaQx5L2bvwBYnZE3a50yycdBQfPvl1fo'

updater = Updater(TOKEN)
#Create start command handler
def start(update:Update, context:CallbackContext):
    """Starts with picture all likes and all dislikes"""
    bot=context.bot
    chat_id=update.message.chat.id
    
    data = LikeDB('like_db.json')
    like = data.all_likes()
    liked = data.all_dislikes()
    user_id = str(update.message.from_user.id)
    dat_db = data.db
    data.add_user(user_id=user_id)
    user_like = dat_db[user_id]['like']
    user_dislike = dat_db[user_id]['dislike']

    keyboard = InlineKeyboardMarkup([
    [InlineKeyboardButton(text='👍',callback_data='like'),
    InlineKeyboardButton(text='👎', callback_data='dislikes')]
    ])
   
    bot.sendMessage(chat_id=chat_id,reply_markup=keyboard,
    text=f'You have {user_like} likes and {user_dislike} dislikes')

def like(update:Update, context:CallbackContext):
    """Send the message with the number of likes and dislikes"""
    query = update.callback_query
    user_id = query.from_user.id

    data = LikeDB('like_db.json')
    data.add_like(str(user_id))
    user_id2 = str(query.from_user.id)
    dat_db = data.db
    user_like = dat_db[user_id2]['like']
    user_dislike = dat_db[user_id2]['dislike']

    keyboard = InlineKeyboardMarkup([
    [InlineKeyboardButton(f'👍{user_like}', callback_data='like'),
        InlineKeyboardButton(f'👎{user_dislike}',callback_data='dislikes'),]
    ])
   
    query.edit_message_text(reply_markup=keyboard, 
    text=f'You have {user_like} likes and {user_dislike} dislikes')

def dislike(update:Update, context:CallbackContext):
    """Send the message with the number of likes and dislikes"""
    query = update.callback_query
    user_id = query.from_user.id

    data = LikeDB('like_db.json')
    data.add_dislike(str(user_id))
    user_id2 = str(query.from_user.id)
    dat_db = data.db
    user_like = dat_db[user_id2]['like']
    user_dislike = dat_db[user_id2]['dislike']

    keyboard = InlineKeyboardMarkup([
    [InlineKeyboardButton(f'👍{user_like}', callback_data='like'),
        InlineKeyboardButton(f'👎{user_dislike}',callback_data='dislike'),]
    ])
    query.edit_message_text(reply_markup=keyboard , text=f'You have {user_like} likes and {user_dislike} dislikes')
#Create updater and dispatcher
updater = Updater(TOKEN)

#add handler to updater
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CallbackQueryHandler(like, pattern='like'))
updater.dispatcher.add_handler(CallbackQueryHandler(dislike, pattern='dislike'))

#Start the bot
updater.start_polling()
updater.idle()



