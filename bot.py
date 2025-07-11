
from telegram import Update
from telegram.ext import *


#Bot user_name and API token to connect the program to the code

bot_user_name ="SentimentTracker529_bot"
API_token="8129880551:AAFTmwamjgYbHs7xHPRP1p9mfK6QqJN_vic" 


async def start_cmd_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello mahn! Letz Go...')

def responses(update):
    id=update.message.chat.id

    return "Sorry I dont understand"

    # if id=="":
    #     return "Nee Poda Patti"
    # elif id=="":
    #     return "Nee Sooper aada"
    # else:
    #     return "aradaaa Nee aynnu"
    

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg_typ = update.message.chat.type
    text = update.message.text

    # Log users
    print(f'User ({update.message.chat.id}) in {msg_typ}: "{text}"')

    # Handle message type
    if msg_typ == 'group':
        if bot_user_name in text:
            #new_text: str = text.replace(bot_user_name, '').strip()
            response = responses(update)
        else:
            return
    else:
        response = responses(update)

    # Reply
    print('Bot:', response)
    await update.message.reply_text(response)



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
