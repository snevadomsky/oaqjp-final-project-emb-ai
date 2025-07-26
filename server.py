"""
Flask server for running emotion detection application
"""
from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def get_emotion_detector():
    """
    Get request to call emotion detector
    """
    input_value = request.args.get("textToAnalyze")
    result = emotion_detector(input_value)
    return_value = str()
    if result["dominant_emotion"] != "None":
        return_value = f"For the given statement, the system response is \
'anger': {result['anger']}, \
'disgust': {result['disgust']}, 'fear': {result['fear']}, \
'joy': {result['joy']} and 'sadness': {result['sadness']}. \
The dominant emotion is {result['dominant_emotion']}."
    else:
        return_value ="Invalid Text! Please try again!"
    return return_value

@app.route("/")
def index():
    """
    Get request to render the index.html template
    """
    return render_template("index.html")

if __name__ == "__main__":
    app.run()
