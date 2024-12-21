from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route('/')
#def render_homepage():
def render_index_page():
   #Render homepage
    return render_template("index.html")

@app.route('/emotionDetector', methods=["GET"])
def emo_analyzer():
    ##Analyze text and return emotion detection (result) """
    text_to_analyze = request.args["textToAnalyze"]

    result= emotion_detector(text_to_analyze)
    response = "For the given statement, the system response is"

    for key, value in result.items():
        # dominant emotion is put last
        if key != "dominant_emotion":
            response += f" '{key}': {value},"

    # Replace last comma with point.
    last_comma= response.rfind(",")
    if last_comma != -1:
        response = response[:last_comma] + '.' + response[last_comma + 1:]

    response += f" The dominant emotion is {result['dominant_emotion']}."

    return response


if __name__ == "__main__":
     app.run(host="0.0.0.0", port=5000)