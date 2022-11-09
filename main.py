from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import bot_commands as bc




app = ApplicationBuilder().token("5737558385:AAGqPy7_U7wes-lqKO9aHgxZtCC2x2zX0oE").build()

app.add_handler(CommandHandler("hi", bc.hi_command))
app.add_handler(CommandHandler("time", bc.time_command))
app.add_handler(CommandHandler("help", bc.help_command))
app.add_handler(CommandHandler("sum", bc.sum_command))

print('server start')

app.run_polling()