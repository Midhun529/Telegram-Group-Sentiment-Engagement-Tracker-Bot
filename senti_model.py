from transformers import AutoTokenizer, AutoModelForSequenceClassification
from transformers import pipeline
import json 
import os


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

for name  in data.keys():
    positive =0
    negative =0
    neutral =0
    for msg in data[name]:
        result = senti_pred(msg)
        rating=result[0]['label']
        if rating in ["1 star","2 stars"]:
            negative+=1
        elif rating == "3 stars":
             neutral+=1
        else:
             positive+=1

    senti_dist
        

         
     
