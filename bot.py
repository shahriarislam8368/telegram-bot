{\rtf1\ansi\ansicpg1252\cocoartf2639
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;\f1\fnil\fcharset0 AppleColorEmoji;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import os\
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update\
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext\
\
# Set your token here (Replace with your own token)\
TOKEN = "7611855352:AAHbCleub29FzmEQpH7sBb7eRaMVnxjF7_Y"  # Replace with the token from BotFather\
\
def start(update: Update, context: CallbackContext) -> None:\
    update.message.reply_text("Send /copy <your text> to create a tap-to-copy button!")\
\
def copy(update: Update, context: CallbackContext) -> None:\
    if not context.args:\
        update.message.reply_text("Usage: /copy Your text here")\
        return\
\
    text_to_copy = " ".join(context.args)\
\
    keyboard = [[InlineKeyboardButton("
\f1 \uc0\u55357 \u56523 
\f0  Copy Text", callback_data=text_to_copy)]]\
    reply_markup = InlineKeyboardMarkup(keyboard)\
\
    update.message.reply_text(f"Tap the button to copy:\\n\\n\{text_to_copy\}", reply_markup=reply_markup)\
\
def button_callback(update: Update, context: CallbackContext) -> None:\
    query = update.callback_query\
    query.answer(text=f"Copied: \{query.data\}", show_alert=True)\
\
def main():\
    updater = Updater(TOKEN, use_context=True)\
    dp = updater.dispatcher\
\
    dp.add_handler(CommandHandler("start", start))\
    dp.add_handler(CommandHandler("copy", copy))\
    dp.add_handler(CallbackQueryHandler(button_callback))\
\
    updater.start_polling()\
    updater.idle()\
\
if __name__ == "__main__":\
    main()\
}