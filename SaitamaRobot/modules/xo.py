import requests
from SaitamaRobot import CASH_API_KEY, dispatcher
from telegram import Update, ParseMode
from telegram.ext import CallbackContext, CommandHandler, run_async
import logging
from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import CommandHandler, InlineQueryHandler, ConversationHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, ParseMode
from telegram.ext import Updater, CallbackQueryHandler, CallbackContext
import random
import time


START_FIRST, KILL_FIRST, GAME_FIRST, XO_FIRST , FIGHT_FIRST, VERIFY_FIRST, *_ = range(1000)

def xo(update, context):
    cd = context.chat_data
    cd['xo'] = {
        "turn" : 0,
        "round" : 0,
        "user0" : update.message.from_user.first_name,
        "user1" : update.message.reply_to_message.from_user.first_name,
        "matrix" :
           [
            [0,0,0],
            [0,0,0],
            [0,0,0]
           ]

    }
    return xo_main(update, context, query=1)

XO_SYMBOLS = [
        " ", "❌", "⭕"
    ]


def xo_main(update , context, query=0):
    cd = context.chat_data
    if query == 1:
        pass
    else:
        query = update.callback_query
        cd["xo"]["matrix"][(int(query.data) - 1) // 3][(int(query.data) - 1) % 3] = (cd['xo']['turn'] + 1) % 2 + 1

    sym = XO_SYMBOLS


    keyboard = [
        [InlineKeyboardButton(sym[cd['xo']['matrix'][0][0]], callback_data='1'),
         InlineKeyboardButton(sym[cd['xo']['matrix'][0][1]], callback_data='2'),
         InlineKeyboardButton(sym[cd['xo']['matrix'][0][2]], callback_data='3')],

        [InlineKeyboardButton(sym[cd['xo']['matrix'][1][0]], callback_data='4'),
         InlineKeyboardButton(sym[cd['xo']['matrix'][1][1]], callback_data='5'),
         InlineKeyboardButton(sym[cd['xo']['matrix'][1][2]], callback_data='6')],

        [InlineKeyboardButton(sym[cd['xo']['matrix'][2][0]], callback_data='7'),
         InlineKeyboardButton(sym[cd['xo']['matrix'][2][1]], callback_data='8'),
         InlineKeyboardButton(sym[cd['xo']['matrix'][2][2]], callback_data='9')],
    ]


    turn = cd['xo']['turn']
    reply_markup = InlineKeyboardMarkup(keyboard)
    if query != 1:
        query.message.edit_text(
            f"Current turn : {cd['xo'][f'user{turn % 2}']} \n\n{cd['xo']['user0']} = ❌\n{cd['xo']['user1']} = ⭕"
            , reply_markup=reply_markup)
    else:
        update.message.reply_text(
            f'Current turn : <b>{update.message.from_user.first_name}</b> \n{update.message.from_user.first_name} = ❌\n{update.message.reply_to_message.from_user.first_name} = ⭕'
            , reply_markup=reply_markup, parse_mode=ParseMode.HTML)
    cd['xo']['turn'] += 1
    cd['xo']['round']+=1
    return XO_FIRST

  
  
  
xo_handler = ConversationHandler(
    entry_points=[CommandHandler('xo', xo)],
    states={
        XO_FIRST:
            [
                CallbackQueryHandler(xo_main, pattern=".")
            ]
    },
    fallbacks=[]
)


dispatcher.add_handler(xo_handler)
