import requests
import sys
import json

def sentiment_analyzer(text_to_analyse):
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    myobj = {"raw_document": {"text": text_to_analyse}}
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    response = requests.post(url, json=myobj, headers=header)
    
    try:
        formatted_response = response.json()
        document_sentiment = formatted_response.get('documentSentiment', {})
        label = document_sentiment.get('label', 'Unknown')
        score = document_sentiment.get('score', 0.0)
        return {'label': label, 'score': score}
    except Exception as e:
        print(f"Error parsing sentiment analysis response: {e}")
        return {'label': 'Unknown', 'score': 0.0}


def print_sentiment_analyzer(text_to_analyse):
    print(sentiment_analyzer(text_to_analyse))

if __name__ == '__main__':
    globals()[sys.argv[1]](sys.argv[2])