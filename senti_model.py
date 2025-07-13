from transformers import AutoTokenizer, AutoModelForSequenceClassification
from transformers import pipeline


def senti_test(text):

    # Load tokenizer and model
    mdl= "nlptown/bert-base-multilingual-uncased-sentiment"
    pred = pipeline("sentiment-analysis", model=mdl)

    # Run sentiment analysis
    result = pred(text)

    return result[0]['label']


