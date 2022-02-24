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
import requests

'''
r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
data = r.json()

num = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "."]
b = ""

a = data['bpi']['USD']['rate']
for i in a:
    if i in num:
        b += i
c = b.split(".")
d = int(c[0]) + int(c[1])/100 # successfully convert to int

e = int(d*74)
INR =("{:,}".format(e)) # convert to INR

f = int(d*4.22)
MYR = ("{:,}".format(f)) # convert to MYR

g = int(d*1.36)
AUD = ("{:,}".format(g))

h = int(d*14440)
IDR = ("{:,}".format(h))

def btc(update , context):


    msg = context.bot.send_message(chat_id=update.effective_chat.id, text=f"<b>BTC :</b> {data['bpi']['USD']['rate']}$ 💶 <B>USD</b> \n"
                                                                          f"<b>BTC :</b> {data['bpi']['EUR']['rate']}$ 💵 <B>EUR</b>\n"
                                                                          f"<b>BTC :</b> {data['bpi']['GBP']['rate']}$ 💷 <B>GBP</b>\n\n"
                                                                          f"<b>BTC :</b> {INR}  <b>INR</b>\n"
                                                                          f"<b>BTC :</b> {IDR}  <b>IDR</b>\n"
                                                                          f"<b>BTC :</b> {AUD}  <b>AUD</b>\n"
                                                                          f"<b>BTC :</b> {MYR}  <b>MYR</b>\n\n\n"
                                                                          f"<b>Updated since:</b> {data['time']['updated']}\n"
                                                                          f"This data was produced from the CoinDesk Bitcoin Price Index (USD)."
                                                                          f" <code> credit to billy</code>"


                                   , parse_mode = ParseMode.HTML)'''
@run_async
def convert(update: Update, context: CallbackContext):
    args = update.effective_message.text.split(" ")

    if len(args) == 4:
        try:
            orig_cur_amount = float(args[1])

        except ValueError:
            update.effective_message.reply_text("Invalid Amount Of Currency")
            return

        orig_cur = args[2].upper()

        new_cur = args[3].upper()

        request_url = (f"https://www.alphavantage.co/query"
                       f"?function=CURRENCY_EXCHANGE_RATE"
                       f"&from_currency={orig_cur}"
                       f"&to_currency={new_cur}"
                       f"&apikey={CASH_API_KEY}")
        response = requests.get(request_url).json()
        try:
            current_rate = float(
                response['Realtime Currency Exchange Rate']['5. Exchange Rate'])
        except KeyError:
            update.effective_message.reply_text("Currency Not Supported.")
            return
        new_cur_amount = round(orig_cur_amount * current_rate, 5)
        update.effective_message.reply_text(
            f"{orig_cur_amount} {orig_cur} = {new_cur_amount} {new_cur}")

    elif len(args) == 1:
        update.effective_message.reply_text(
            __help__, parse_mode=ParseMode.MARKDOWN)

    else:
        update.effective_message.reply_text(
            f"*Invalid Args!!:* Required 3 But Passed {len(args) -1}",
            parse_mode=ParseMode.MARKDOWN)


CONVERTER_HANDLER = CommandHandler('cash', convert)
#BTC_HANDLER = CommandHandler('btc', btc)

dispatcher.add_handler(CONVERTER_HANDLER)
#dispatcher.add_handler(BTC_HANDLER)

__command_list__ = ["cash"]
__handlers__ = [CONVERTER_HANDLER]
