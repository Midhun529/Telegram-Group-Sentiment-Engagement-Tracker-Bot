from transformers import AutoTokenizer, AutoModelForSequenceClassification
from transformers import pipeline
import json 
import os
import telegram
import asyncio



bot_user_name ="SentimentTracker529_bot"
API_token="8129880551:AAFTmwamjgYbHs7xHPRP1p9mfK6QqJN_vic" 

def senti_pred(text):

    # Load tokenizer and model
    mdl= "nlptown/bert-base-multilingual-uncased-sentiment"
    pred = pipeline("sentiment-analysis", model=mdl)
    # Run sentiment analysis
    result = pred(text)

    return result[0]['label']



msg_file = "msg.json"

if os.path.exists(msg_file):
        try:
            with open(msg_file, "r") as f:
                data = json.load(f)
        except json.JSONDecodeError:
            data = {} 
message="Group Sentiment Insight"
for name  in data.keys():
    
    positive =0
    negative =0
    neutral =0
    overall_msg=0
    for msg in data[name]:
        overall_msg+=1
        result = senti_pred(msg)
        rating=result
        if rating in ["1 star","2 stars"]:
            negative+=1
        elif rating == "3 stars":
             neutral+=1
        else:
             positive+=1

    # senti_dist={}
    # senti_dist[name]=[positive,neutral,negative]

    user_sent = (
        f"\n{'*' * 25}\n"
        f"User Name     :    {name}\n"
        f"😊 Positive   :    {positive/overall_msg : .2f} %\n"
        f"😐 Neutral    :    {neutral/overall_msg : .2f} %\n"
        f"😠 Negative   :    {negative/overall_msg : .2f} %\n"
        f"Message Count :    {overall_msg}"
         f"\n{'*' * 25}\n"
    )
    
    message += user_sent + "\n"

async def send_telegram_message():
    with open("chat_id.txt", "r") as f1:
        lines = f1.readlines()

    if len(lines) == 1:
        chat_id = lines[0].strip()
        chat_id = int(chat_id)
        print(chat_id)
        bot = telegram.Bot(token=API_token)
        await bot.send_message(chat_id=chat_id, text=message)


asyncio.run(send_telegram_message())

        

         
     
