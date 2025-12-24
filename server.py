from flask import Flask, render_template, request
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

app=Flask(__name__, template_folder='src/templates', static_folder= 'src/static')

@app.route("/")
def render_index_page():
    
    return render_template('index.html')

@app.route("/sentimentAnalyzer")
def sent_analyzer():
    
    text_to_be_analysed=request.args['textToAnalyze']
    text_to_be_sent= sentiment_analyzer(text_to_be_analysed)['label']

    return f'The given text is {text_to_be_sent}'
    



if __name__ == "__main__":
    ''' This functions executes the flask app and deploys it on localhost:5000
    '''#TODO
