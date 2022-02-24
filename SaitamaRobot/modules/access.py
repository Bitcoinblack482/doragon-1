import logging
from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import CommandHandler, InlineQueryHandler, ConversationHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, ParseMode
from telegram.ext import Updater, CallbackQueryHandler, CallbackContext
import random
import time
import requests
from SaitamaRobot import CASH_API_KEY, dispatcher
from telegram import Update, ParseMode
from telegram.ext import CallbackContext, CommandHandler, run_async


def access(update , context):
    a = random.randint(100,200)
    user_id = update.effective_user.id
    user_first = update.effective_user.first_name
    name = update.effective_user.name
    txt = "logging in 3...2...1..."
    blank = ""
    if user_id != 163494588:
     y = update.message.reply_text(f"<b>{name} You are <i>Not authorized</i> to use this command</b>\n\n"
                               f"<i>Encryption           = FALSE</i>\n"
                               f"<i>private key          = FALSE</i> \n"
                               f"<i>User_id                =<code>{user_id}</code></i> \n"
                               f"<i>User_FirstName</i> = <code>{user_first}</code>" , parse_mode= ParseMode.HTML)
     z = update.message.reply_text(f"<code>logging user's report in </code>"
                               , parse_mode=ParseMode.HTML)

     a = context.bot.send_message(chat_id = update.effective_chat.id ,text ="start logging",parse_mode= ParseMode.HTML) 
     for ch in txt:
      blank+= ch
      if ch == " ":
        continue
      a.edit_text(f"<code>{blank}</code>", parse_mode= ParseMode.HTML) 
     context.bot.delete_message(chat_id = update.effective_chat.id ,message_id = a.message_id)
     
     #a = context.bot.send_message(chat_id = update.effective_chat.id ,text ="3")
     #time.sleep(1)
     #context.bot.delete_message(chat_id = update.effective_chat.id ,message_id = a.message_id)

     #b =context.bot.send_message(chat_id = update.effective_chat.id ,text ="2")
     #time.sleep(1)
     #context.bot.delete_message(chat_id = update.effective_chat.id ,message_id = b.message_id)

     #c =context.bot.send_message(chat_id = update.effective_chat.id ,text ="1")
     #time.sleep(1)
     #context.bot.delete_message(chat_id = update.effective_chat.id ,message_id = c.message_id)

     context.bot.delete_message(chat_id = update.effective_chat.id ,message_id = z.message_id)
     x = update.message.reply_text(f'<code>report logged....</code>', parse_mode = ParseMode.HTML)
 
     context.bot.delete_message(chat_id=update.effective_chat.id, message_id=y.message_id)
     context.bot.delete_message(chat_id=update.effective_chat.id, message_id=x.message_id)


    else:
        keyboard = [

            [InlineKeyboardButton("🤖 Bot stats", callback_data="1"),
             InlineKeyboardButton("👮 Manager lists", callback_data="2")] ,

             [InlineKeyboardButton("🕹 Control Panel", callback_data="3")],

            [InlineKeyboardButton("💳 Server balance",callback_data="4") ,
             InlineKeyboardButton("🖲 Broadcast message",callback_data="5")],


            [InlineKeyboardButton("🚥 Security Access ",callback_data="6"),
             InlineKeyboardButton('📂 Mainfile.py',callback_data="7")],

             [InlineKeyboardButton("🗂Database file",callback_data="8")],
        ]

        r = InlineKeyboardMarkup(keyboard)
        update.message.reply_text(f"<b>Welcome back {update.message.from_user.first_name}</b>\n\n"
                                  f"<i>What would you like to do today sir</i>\n"
                                  f"<i>Here are all credential access to the bot</i>\n\n"
                                  f"<code>Owner access    = True</code>\n"
                                  f"<code>Server running  = True</code>\n"
                                  f"<code>Breach          = False</code>\n"
                                  f"<code>Database status = </code> <b>{a/100}/100% covered</b>"
                                  ,
                                 reply_markup = r, parse_mode = ParseMode.HTML)
        
ACCESS_HANDLER = CommandHandler('access', access)


dispatcher.add_handler(ACCESS_HANDLER)


__command_list__ = ["access"]
__handlers__ = [ACCESS_HANDLER]
