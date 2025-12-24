import requests
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


# the below code uses ibm api which can onl
# def sentiment_analyzer():
#     TEXT_TO_ANALYSE='stock market is going down'

#     URL = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
#     HEADERS = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
#     INPUT_OBJ= { "raw_document": { "text": TEXT_TO_ANALYSE } }

#     RESPONSE = requests.post(URL, json=INPUT_OBJ, headers=HEADERS)

#     print(RESPONSE.text)


def sentiment_analyzer(text_to_analyse):
    
    sid = SentimentIntensityAnalyzer()
    score = sid.polarity_scores(text_to_analyse)
    
    if score['compound'] > 0.05:
        label='positive'
    elif score['compound'] <= -0.05:
        label='negative'
    else:
        label= 'neutral'

    # return {'label':label,'score':score['compound'] }
    return {'label':label}
    

# response=sentiment_analyzer(input("Enter ur phrase : "))
# print(response)

