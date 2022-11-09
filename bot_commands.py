from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime


async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    
    await update.message.reply_text(f'Hi {update.effective_user.first_name}')

async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    
    await update.message.reply_text(f'time {datetime.datetime.now().time()}')

async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    
    msg = update.message.text
    print(msg)

    items = msg.split() # /sum 123 213123
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} + {y} = {x + y}')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    
    await update.message.reply_text(f'/hi\n/time\n/sum\n/help')