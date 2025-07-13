
from telegram import Update
from telegram.ext import *
from senti_model import senti_test
import os
import json

#Bot user_name and API token to connect the program to the code

bot_user_name ="SentimentTracker529_bot"
API_token="8129880551:AAFTmwamjgYbHs7xHPRP1p9mfK6QqJN_vic" 


async def start_cmd_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello mahn! Letz Go...')



def msg_save(update,msg_file):
    name = update.message.from_user.first_name
    msg=update.message.text
    data = {}
    if os.path.exists(msg_file):
        try:
            with open(msg_file, "r") as f:
                data = json.load(f)
        except json.JSONDecodeError:
            data = {} 
    if name not in data:
        data[name] = []
    data[name].append(msg)
    with open(msg_file, "w") as f:
        json.dump(data, f)

    

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
   # print(f'User ({update.message.chat.id}) in {msg_typ}: "{text}"')
    msg_file = "msg.json"
    msg_save(update,msg_file)



# Error handler
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error: {context.error}')


def main():
    print('Starting up bot...')
    app = Application.builder().token(API_token).build()

    # Commands
    app.add_handler(CommandHandler('start', start_cmd_reply))
  
    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Errors
    app.add_error_handler(error)

    # Define a poll interval
    print('Polling...')
    app.run_polling(poll_interval=5)


main()
