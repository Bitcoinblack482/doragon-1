import html
import random
import time


import SaitamaRobot.modules.fun_strings as fun_strings
from SaitamaRobot import dispatcher
from SaitamaRobot.modules.disable import DisableAbleCommandHandler
from SaitamaRobot.modules.helper_funcs.chat_status import is_user_admin
from SaitamaRobot.modules.helper_funcs.extraction import extract_user
from telegram import ChatPermissions, ParseMode, Update
from telegram.error import BadRequest
from telegram.ext import CallbackContext, run_async

#GIF_ID = 'CgACAgQAAx0CSVUvGgAC7KpfWxMrgGyQs-GUUJgt-TSO8cOIDgACaAgAAlZD0VHT3Zynpr5nGxsE'
#THANOS = 'CgACAgQAAxkBAAI352DwBkbU4hfmR7Qdabtyp--DLTzsAAILAgACcEjNUmiK1Cwcpza4HgQ' 
auths = [163494588,883736955,1209090379,1218671329] 
list = ["administrator", "creator"] 


@run_async
def runs(update: Update, context: CallbackContext):
    update.effective_message.reply_text(random.choice(fun_strings.RUN_STRINGS))
    
def stones(update: Update, context: CallbackContext):
    update.effective_message.reply_text("🟣 : Power Stone \n🔵 : Space Stone \n🔴 : Reality Stone \n🟠 : Soul Stone \n🟢 : Time Stone \n🟡 : Mind Stone \n\n He Who Have All \n ---> @wancoins")

    

def post(update , context):
    msg = update.message.reply_to_message.caption
    id = update.effective_user.id 
    pic = update.message.reply_to_message.photo[-1]
    a = context.bot.get_chat_member(chat_id=update.effective_chat.id, user_id=update.effective_user.id).status
    if a in list:
     context.bot.send_photo(chat_id= -1001332689069, photo=pic, caption=msg)    
     return -1
    if id in auths:
     context.bot.send_photo(chat_id= -1001332689069, photo=pic, caption=msg)    
     return -1
    else:
     update.message.reply_text('<code>Not Authorized</code>', parse_mode = ParseMode.HTML)
     return -1
  
def auth(update, context):
    id = update.message.reply_to_message.from_user.id
    name = update.message.reply_to_message.from_user.first_name
    if update.effective_user.id!=163494588:
     update.message.reply_text("You're not my master") 
     return -1
    if id not in auths:
     auths.append(id)
     update.message.reply_text(f"{name} authorised to post in channel <ArtKayo>")
     return -1
    elif id in auths:
     update.message.reply_text("This person already authorised to post in channel <ArtKayo>") 
    

@run_async 
def feed(update, context):
    msg = update.message.text
    msg = msg.split()[1:]
    msg=(''.join(msg[0:]))

    user_name = update.message.from_user.first_name
    to = update.message.reply_to_message.from_user.first_name
    toid = update.message.reply_to_message.from_user.id
    pick = [f'but <b>{to}</b> refused to have it',
            f'and <b>{to}</b> enjoy it very much',
            f'but <b>{to}</b> want to share it with <b>{user_name}</b>',
            f'but <b>{to}</b> throw it back at <b>{user_name}</b>']
    if toid == context.bot.id:
        update.message.reply_text(f'{user_name} , you cant feed me , im the food. \n*pouty face')
        return -1
    if toid == 163494588:
        update.message.reply_text(f'Punny Human cant feed my Master Billy , he is God tier')
        return -1
    update.message.reply_text(f'<b>{user_name}</b> feed {msg} to <b>{to}</b> {random.choice(pick)}', parse_mode = ParseMode.HTML)
    
@run_async
def sanitize(update, context):
    user = update.message.reply_to_message.from_user.name
    context.bot.send_animation(
        chat_id=update.message.chat.id,
        animation='CgACAgUAAx0CWmwOBwACCVJhCMn5Gi8tY3NWD-KGPeAPOssJcQACqwADg_8wVYvQ_W_-v9RpIAQ',
        caption=f' 💨 💨 <i>sanitize</i> <b>{user}</b>', parse_mode=ParseMode.HTML)
    
    
@run_async
def giftest(update: Update, context : CallbackContext):
    """context.bot.sendDocument(chat_id=update.effective_chat.id, document="https://tenor.com/6U3c.gif")
    print("test")
    update.effective_message.reply_text("test")"""

    context.bot.send_animation(chat_id=update.message.chat.id,animation='https://tenor.com/6U3c.gif',caption='TEST') 
    
@run_async
def thanos(update, context):
    
    a = context.bot.send_animation(
        chat_id=update.message.chat.id,
        animation='CgACAgQAAxkBAAI352DwBkbU4hfmR7Qdabtyp--DLTzsAAILAgACcEjNUmiK1Cwcpza4HgQ')
    context.bot.delete_message(chat_id=update.effective_chat.id, message_id=update.effective_message.message_id)
        

'''@run_async
def sanitize(update: Update, context: CallbackContext):
    message = update.effective_message
    name = (
        message.reply_to_message.from_user.first_name
        if message.reply_to_message
        else message.from_user.first_name
    )
    reply_animation = (
        message.reply_to_message.reply_animation
        if message.reply_to_message
        else message.reply_animation
    )
    reply_animation(random.choice(fun_strings.GIFS), caption=f"*Sanitizess {name}*")'''



@run_async
def billy(update: Update, context: CallbackContext):
    bot, args = context.bot, context.args
    message = update.effective_message
    chat = update.effective_chat

    reply_text = message.reply_to_message.reply_text if message.reply_to_message else message.reply_text

    curr_user = html.escape(message.from_user.first_name)
    user_id = extract_user(message, args)

    if user_id == bot.id:
        temp = random.choice(fun_strings.SLAP_SAITAMA_TEMPLATES)

        if isinstance(temp, list):
            if temp[2] == "tmute":
                if is_user_admin(chat, message.from_user.id):
                    reply_text(temp[1])
                    return

                mutetime = int(time.time() + 60)
                bot.restrict_chat_member(
                    chat.id,
                    message.from_user.id,
                    until_date=mutetime,
                    permissions=ChatPermissions(can_send_messages=False))
            reply_text(temp[0])
        else:
            reply_text(temp)
        return

    if user_id:

        slapped_user = bot.get_chat(user_id)
        user1 = curr_user
        user2 = html.escape(slapped_user.first_name)

    else:
        user1 = curr_user
        user2 = "no one" 

    temp = random.choice(fun_strings.BILLY_TEMPLATES)

    if update.effective_user.id == 163494588:
        temp = "{user1} is already the king"

    reply = temp.format(
        user1=user1, user2=user2,)

    reply_text(reply, parse_mode=ParseMode.HTML)
    
    
@run_async
def slap(update: Update, context: CallbackContext):
    bot, args = context.bot, context.args
    message = update.effective_message
    chat = update.effective_chat

    reply_text = message.reply_to_message.reply_text if message.reply_to_message else message.reply_text

    curr_user = html.escape(message.from_user.first_name)
    user_id = extract_user(message, args)

    if user_id == bot.id:
        temp = random.choice(fun_strings.SLAP_SAITAMA_TEMPLATES)

        if isinstance(temp, list):
            if temp[2] == "tmute":
                if is_user_admin(chat, message.from_user.id):
                    reply_text(temp[1])
                    return

                mutetime = int(time.time() + 60)
                bot.restrict_chat_member(
                    chat.id,
                    message.from_user.id,
                    until_date=mutetime,
                    permissions=ChatPermissions(can_send_messages=False))
            reply_text(temp[0])
        else:
            reply_text(temp)
        return

    if user_id:

        slapped_user = bot.get_chat(user_id)
        user1 = curr_user
        user2 = html.escape(slapped_user.first_name)

    else:
        user1 = bot.first_name
        user2 = curr_user

    temp = random.choice(fun_strings.SLAP_TEMPLATES)
    item = random.choice(fun_strings.ITEMS)
    hit = random.choice(fun_strings.HIT)
    throw = random.choice(fun_strings.THROW)

    if update.effective_user.id == 1096215023:
        temp = "@NeoTheKitty scratches {user2}"

    reply = temp.format(
        user1=user1, user2=user2, item=item, hits=hit, throws=throw)

    reply_text(reply, parse_mode=ParseMode.HTML)
    
@run_async
def earth(update: Update, context: CallbackContext):
    bot, args = context.bot, context.args
    message = update.effective_message
    chat = update.effective_chat

    reply_text = message.reply_to_message.reply_text if message.reply_to_message else message.reply_text

    curr_user = html.escape(message.from_user.first_name)
    user_id = extract_user(message, args)

    if user_id == bot.id:
        temp = random.choice(fun_strings.GAME_TEMPLATES)

        if isinstance(temp, list):
            if temp[2] == "tmute":
                if is_user_admin(chat, message.from_user.id):
                    reply_text(temp[1])
                    return

                mutetime = int(time.time() + 60)
                bot.restrict_chat_member(
                    chat.id,
                    message.from_user.id,
                    until_date=mutetime,
                    permissions=ChatPermissions(can_send_messages=False))
            reply_text(temp[0])
        else:
            reply_text(temp)
        return

    if user_id:

        slapped_user = bot.get_chat(user_id)
        user1 = curr_user
        user2 = html.escape(slapped_user.first_name)

    else:
        user1 = curr_user
        user2 = "Nothing" 

    temp = random.choice(fun_strings.EARTH_GAME_TEMPLATES)
    hp = random.choice(fun_strings.HP)
    earth = random.choice(fun_strings.EARTH)

    if update.effective_user.id == 1096215023:
        temp = "@NeoTheKitty scratches {user2}"

    reply = temp.format(
        user1=user1, user2=user2, hp=hp, earth=earth)

    reply_text(reply, parse_mode=ParseMode.HTML)
    
@run_async
def heal(update: Update, context: CallbackContext):
    bot, args = context.bot, context.args
    message = update.effective_message
    chat = update.effective_chat

    reply_text = message.reply_to_message.reply_text if message.reply_to_message else message.reply_text

    curr_user = html.escape(message.from_user.first_name)
    user_id = extract_user(message, args)

    if user_id == bot.id:
        temp = random.choice(fun_strings.GAME_TEMPLATES)

        if isinstance(temp, list):
            if temp[2] == "tmute":
                if is_user_admin(chat, message.from_user.id):
                    reply_text(temp[1])
                    return

                mutetime = int(time.time() + 60)
                bot.restrict_chat_member(
                    chat.id,
                    message.from_user.id,
                    until_date=mutetime,
                    permissions=ChatPermissions(can_send_messages=False))
            reply_text(temp[0])
        else:
            reply_text(temp)
        return

    if user_id:

        slapped_user = bot.get_chat(user_id)
        user1 = curr_user
        user2 = html.escape(slapped_user.first_name)

    else:
        user1 = curr_user
        user2 = "none" 

    temp = random.choice(fun_strings.HEAL_TEMPLATES)
    healhp = random.choice(fun_strings.HEALHP)
    heal = random.choice(fun_strings.HEAL)

    if update.effective_user.id == 1096215023:
        temp = "@NeoTheKitty scratches {user2}"

    reply = temp.format(
        user1=user1, user2=user2, healhp=healhp, heal=heal)

    reply_text(reply, parse_mode=ParseMode.HTML)
    
@run_async
def fire(update: Update, context: CallbackContext):
    bot, args = context.bot, context.args
    message = update.effective_message
    chat = update.effective_chat

    reply_text = message.reply_to_message.reply_text if message.reply_to_message else message.reply_text

    curr_user = html.escape(message.from_user.first_name)
    user_id = extract_user(message, args)

    if user_id == bot.id:
        temp = random.choice(fun_strings.GAME_TEMPLATES)

        if isinstance(temp, list):
            if temp[2] == "tmute":
                if is_user_admin(chat, message.from_user.id):
                    reply_text(temp[1])
                    return

                mutetime = int(time.time() + 60)
                bot.restrict_chat_member(
                    chat.id,
                    message.from_user.id,
                    until_date=mutetime,
                    permissions=ChatPermissions(can_send_messages=False))
            reply_text(temp[0])
        else:
            reply_text(temp)
        return

    if user_id:

        slapped_user = bot.get_chat(user_id)
        user1 = curr_user
        user2 = html.escape(slapped_user.first_name)

    else:
        user1 = curr_user
        user2 = "nobody" 

    temp = random.choice(fun_strings.FIRE_GAME_TEMPLATES)
    hp = random.choice(fun_strings.HP)
    fire = random.choice(fun_strings.FIRE)

    if update.effective_user.id == 1096215023:
        temp = "@NeoTheKitty scratches {user2}"

    reply = temp.format(
        user1=user1, user2=user2, hp=hp, fire=fire)

    reply_text(reply, parse_mode=ParseMode.HTML)

@run_async
def water(update: Update, context: CallbackContext):
    bot, args = context.bot, context.args
    message = update.effective_message
    chat = update.effective_chat

    reply_text = message.reply_to_message.reply_text if message.reply_to_message else message.reply_text

    curr_user = html.escape(message.from_user.first_name)
    user_id = extract_user(message, args)

    if user_id == bot.id:
        temp = random.choice(fun_strings.GAME_TEMPLATES)

        if isinstance(temp, list):
            if temp[2] == "tmute":
                if is_user_admin(chat, message.from_user.id):
                    reply_text(temp[1])
                    return

                mutetime = int(time.time() + 60)
                bot.restrict_chat_member(
                    chat.id,
                    message.from_user.id,
                    until_date=mutetime,
                    permissions=ChatPermissions(can_send_messages=False))
            reply_text(temp[0])
        else:
            reply_text(temp)
        return

    if user_id:

        slapped_user = bot.get_chat(user_id)
        user1 = curr_user
        user2 = html.escape(slapped_user.first_name)

    else:
        user1 = curr_user
        user2 = "nobody" 

    temp = random.choice(fun_strings.WATER_GAME_TEMPLATES)
    hp = random.choice(fun_strings.HP)
    water = random.choice(fun_strings.WATER)

    if update.effective_user.id == 1096215023:
        temp = "@NeoTheKitty scratches {user2}"

    reply = temp.format(
        user1=user1, user2=user2, hp=hp, water=water)

    reply_text(reply, parse_mode=ParseMode.HTML)

@run_async
def meow(update: Update, context: CallbackContext):
    bot, args = context.bot, context.args
    message = update.effective_message
    chat = update.effective_chat

    reply_text = message.reply_to_message.reply_text if message.reply_to_message else message.reply_text

    curr_user = html.escape(message.from_user.first_name)
    user_id = extract_user(message, args)

    if user_id == bot.id:
        temp = random.choice(fun_strings.GAME_TEMPLATES)

        if isinstance(temp, list):
            if temp[2] == "tmute":
                if is_user_admin(chat, message.from_user.id):
                    reply_text(temp[1])
                    return

                mutetime = int(time.time() + 60)
                bot.restrict_chat_member(
                    chat.id,
                    message.from_user.id,
                    until_date=mutetime,
                    permissions=ChatPermissions(can_send_messages=False))
            reply_text(temp[0])
        else:
            reply_text(temp)
        return

    if user_id:

        slapped_user = bot.get_chat(user_id)
        user1 = curr_user
        user2 = html.escape(slapped_user.first_name)

    else:
        user1 = bot.first_name
        user2 = curr_user

    temp = random.choice(fun_strings.MEOW_TEMPLATES)
    lewd = random.choice(fun_strings.LEWD)
    meter = random.choice(fun_strings.METER)

    if update.effective_user.id == 1096215023:
        temp = "@NeoTheKitty scratches {user2}"

    reply = temp.format(
        user1=user1, user2=user2, lewd=lewd, meter=meter)

    reply_text(reply, parse_mode=ParseMode.HTML)    
    
@run_async
def pat(update: Update, context: CallbackContext):
    bot = context.bot
    args = context.args
    message = update.effective_message

    reply_to = message.reply_to_message if message.reply_to_message else message

    curr_user = html.escape(message.from_user.first_name)
    user_id = extract_user(message, args)

    if user_id:
        patted_user = bot.get_chat(user_id)
        user1 = curr_user
        user2 = html.escape(patted_user.first_name)

    else:
        user1 = bot.first_name
        user2 = curr_user

    pat_type = random.choice(("Text", "Gif", "Sticker"))
    if pat_type == "Gif":
        try:
            temp = random.choice(fun_strings.PAT_GIFS)
            reply_to.reply_animation(temp)
        except BadRequest:
            pat_type = "Text"

    if pat_type == "Sticker":
        try:
            temp = random.choice(fun_strings.PAT_STICKERS)
            reply_to.reply_sticker(temp)
        except BadRequest:
            pat_type = "Text"

    if pat_type == "Text":
        temp = random.choice(fun_strings.PAT_TEMPLATES)
        reply = temp.format(user1=user1, user2=user2)
        reply_to.reply_text(reply, parse_mode=ParseMode.HTML)


@run_async
def roll(update: Update, context: CallbackContext):
    update.message.reply_text(random.choice(range(1, 7)))


@run_async
def shout(update: Update, context: CallbackContext):
    args = context.args
    text = " ".join(args)
    result = []
    result.append(' '.join(list(text)))
    for pos, symbol in enumerate(text[1:]):
        result.append(symbol + ' ' + '  ' * pos + symbol)
    result = list("\n".join(result))
    result[0] = text[0]
    result = "".join(result)
    msg = "```\n" + result + "```"
    return update.effective_message.reply_text(msg, parse_mode="MARKDOWN")


@run_async
def toss(update: Update, context: CallbackContext):
    update.message.reply_text(random.choice(fun_strings.TOSS))


@run_async
def shrug(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    reply_text(r"¯\_(ツ)_/¯")


@run_async
def bluetext(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    reply_text(
        "/BLUE /TEXT\n/MUST /CLICK\n/I /AM /A /STUPID /ANIMAL /THAT /IS /ATTRACTED /TO /COLORS"
    )


@run_async
def rlg(update: Update, context: CallbackContext):
    eyes = random.choice(fun_strings.EYES)
    mouth = random.choice(fun_strings.MOUTHS)
    ears = random.choice(fun_strings.EARS)

    if len(eyes) == 2:
        repl = ears[0] + eyes[0] + mouth[0] + eyes[1] + ears[1]
    else:
        repl = ears[0] + eyes[0] + mouth[0] + eyes[0] + ears[1]
    update.message.reply_text(repl)


@run_async
def decide(update: Update, context: CallbackContext):
    reply_text = update.effective_message.reply_to_message.reply_text if update.effective_message.reply_to_message else update.effective_message.reply_text
    reply_text(random.choice(fun_strings.DECIDE))


@run_async
def eightball(update: Update, context: CallbackContext):
    reply_text = update.effective_message.reply_to_message.reply_text if update.effective_message.reply_to_message else update.effective_message.reply_text
    reply_text(random.choice(fun_strings.EIGHTBALL))


@run_async
def table(update: Update, context: CallbackContext):
    reply_text = update.effective_message.reply_to_message.reply_text if update.effective_message.reply_to_message else update.effective_message.reply_text
    reply_text(random.choice(fun_strings.TABLE))


normiefont = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
weebyfont = [
    '卂', '乃', '匚', '刀', '乇', '下', '厶', '卄', '工', '丁', '长', '乚', '从', '𠘨', '口',
    '尸', '㔿', '尺', '丂', '丅', '凵', 'リ', '山', '乂', '丫', '乙'
]


@run_async
def weebify(update: Update, context: CallbackContext):
    args = context.args
    message = update.effective_message
    string = ""

    if message.reply_to_message:
        string = message.reply_to_message.text.lower().replace(" ", "  ")

    if args:
        string = '  '.join(args).lower()

    if not string:
        message.reply_text(
            "Usage is `/weebify <text>`", parse_mode=ParseMode.MARKDOWN)
        return

    for normiecharacter in string:
        if normiecharacter in normiefont:
            weebycharacter = weebyfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, weebycharacter)

    if message.reply_to_message:
        message.reply_to_message.reply_text(string)
    else:
        message.reply_text(string)


__help__ = """
 • `/runs`*:* reply a random string from an array of replies
 • `/slap`*:* slap a user, or get slapped if not a reply
 • `/billy`*:*  custom made by billy
 • `/heal`*:*  custom made by billy
 • `/earth`*:*  custom made by billy
 • `/meow`*:*  custom made by billy
 • `/water`*:*  custom made by billy
 • `/fire`*:*   custom made by billy
 • `/shrug`*:* get shrug XD
 • `/table`*:* get flip/unflip :v
 • `/decide`*:* Randomly answers yes/no/maybe
 • `/toss`*:* Tosses A coin
 • `/bluetext`*:* check urself :V
 • `/roll`*:* Roll a dice
 • `/rlg`*:* Join ears,nose,mouth and create an emo ;-;
 • `/shout <keyword>`*:* write anything you want to give loud shout
 • `/weebify <text>`*:* returns a weebified text
 • `/sanitize`*:* always use this before /pat or any contact
 • `/pat`*:* pats a user, or get patted
 • `/8ball`*:* predicts using 8ball method 
"""
GIFTEST_HANDLER = DisableAbleCommandHandler("giftest", giftest)
SANITIZE_HANDLER = DisableAbleCommandHandler("sanitize", sanitize)
EARTH_HANDLER = DisableAbleCommandHandler("earth", earth)
HEAL_HANDLER = DisableAbleCommandHandler("heal", heal)
WATER_HANDLER = DisableAbleCommandHandler("water", water)
MEOW_HANDLER = DisableAbleCommandHandler("meow", meow)
FIRE_HANDLER = DisableAbleCommandHandler("fire", fire)
RUNS_HANDLER = DisableAbleCommandHandler("runs", runs)
SLAP_HANDLER = DisableAbleCommandHandler("slap", slap)
BILLY_HANDLER = DisableAbleCommandHandler("billy", billy)
PAT_HANDLER = DisableAbleCommandHandler("pat", pat)
ROLL_HANDLER = DisableAbleCommandHandler("roll", roll)
TOSS_HANDLER = DisableAbleCommandHandler("toss", toss)
SHRUG_HANDLER = DisableAbleCommandHandler("shrug", shrug)
BLUETEXT_HANDLER = DisableAbleCommandHandler("bluetext", bluetext)
RLG_HANDLER = DisableAbleCommandHandler("rlg", rlg)
DECIDE_HANDLER = DisableAbleCommandHandler("decide", decide)
EIGHTBALL_HANDLER = DisableAbleCommandHandler("8ball", eightball)
TABLE_HANDLER = DisableAbleCommandHandler("table", table)
SHOUT_HANDLER = DisableAbleCommandHandler("shout", shout)
WEEBIFY_HANDLER = DisableAbleCommandHandler("weebify", weebify)
STONES_HANDLER = DisableAbleCommandHandler("stones", stones)
THANOS_HANDLER = DisableAbleCommandHandler("thanos", thanos)
FEED_HANDLER = DisableAbleCommandHandler("feed", feed)
POST_HANDLER = DisableAbleCommandHandler("post", post)
AUTH_HANDLER = DisableAbleCommandHandler("auth", auth)
 
dispatcher.add_handler(AUTH_HANDLER)
dispatcher.add_handler(POST_HANDLER)
dispatcher.add_handler(WEEBIFY_HANDLER)
dispatcher.add_handler(THANOS_HANDLER)
dispatcher.add_handler(GIFTEST_HANDLER)
dispatcher.add_handler(SHOUT_HANDLER)
dispatcher.add_handler(SANITIZE_HANDLER)
dispatcher.add_handler(EARTH_HANDLER)
dispatcher.add_handler(HEAL_HANDLER)
dispatcher.add_handler(WATER_HANDLER)
dispatcher.add_handler(MEOW_HANDLER)
dispatcher.add_handler(FIRE_HANDLER)
dispatcher.add_handler(RUNS_HANDLER)
dispatcher.add_handler(SLAP_HANDLER)
dispatcher.add_handler(BILLY_HANDLER)
dispatcher.add_handler(PAT_HANDLER)
dispatcher.add_handler(ROLL_HANDLER)
dispatcher.add_handler(TOSS_HANDLER)
dispatcher.add_handler(SHRUG_HANDLER)
dispatcher.add_handler(BLUETEXT_HANDLER)
dispatcher.add_handler(RLG_HANDLER)
dispatcher.add_handler(DECIDE_HANDLER)
dispatcher.add_handler(EIGHTBALL_HANDLER)
dispatcher.add_handler(TABLE_HANDLER)
dispatcher.add_handler(STONES_HANDLER)
dispatcher.add_handler(FEED_HANDLER)

__mod_name__ = "Fun"
__command_list__ = [
    "runs",
    "auth", 
    "post",
    'feed',
    "slap", 
    "billy" ,
    "stones" ,
    "roll", 
    "fire",
    "water",
    "meow", 
    "toss", 
    "shrug",
    "heal",
    "earth",
    "bluetext",
    "rlg", 
    "decide",
    "table",
    "pat",
    "sanitize", 
    "giftest", 
    "shout",
    "weebify",
    "thanos",
    "8ball"
]
__handlers__ = [
    RUNS_HANDLER,
    AUTH_HANDLER, 
    POST_HANDLER,
    FEED_HANDLER,
    THANOS_HANDLER,
    SLAP_HANDLER, 
    BILLY_HANDLER, 
    FIRE_HANDLER, 
    WATER_HANDLER, 
    MEOW_HANDLER, 
    EARTH_HANDLER, 
    HEAL_HANDLER , 
    PAT_HANDLER, 
    ROLL_HANDLER, 
    TOSS_HANDLER,
    SHRUG_HANDLER, 
    BLUETEXT_HANDLER, 
    RLG_HANDLER, 
    DECIDE_HANDLER, 
    TABLE_HANDLER,
    SANITIZE_HANDLER, 
    GIFTEST_HANDLER, 
    SHOUT_HANDLER, 
    WEEBIFY_HANDLER, 
    EIGHTBALL_HANDLER, 
    STONES_HANDLER
]
