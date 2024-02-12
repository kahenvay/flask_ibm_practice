''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer
# import json

app = Flask(__name__)

# @app.route("/sentimentAnalyzer")
# def sent_analyzer():
#     text_to_analyse = request.args.get("text_to_analyse")
#     if not text_to_analyse:
#         return {"message": "Invalid input parameter"}, 422
    
#     response = sentiment_analyzer(text_to_analyse)
#     # formatted_response = json.loads(response)
    
#     # return formatted_response, 422
#     return response, 422
#     # curl -X GET -i -w '\n' "http://localhost:5000/sentimentAnalyzer?text_to_analyse=I%20love%20watson"

@app.route("/sentimentAnalyzer")
def sent_analyzer():
    text_to_analyze = request.args.get('textToAnalyze')
    response = sentiment_analyzer(text_to_analyze)
    
    label = response.get('label', 'Unknown')
    score = response.get('score', 0.0)
    
    if '_' in label:
        label_parts = label.split('_')
        if len(label_parts) > 1:
            label = label_parts[1]
    
    return "The given text has been identified as {} with a score of {}.".format(label, score)


@app.route("/")
def render_index_page():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
    # app.run(host="0.0.0.0", port=5000)
