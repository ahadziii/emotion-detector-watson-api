from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector


app = Flask("Emotion Detector")


@app.route('/emotionDetector')
def emot_detector():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using emotion_detector()
        function.
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    score_strings = [f"'{emotion}': {score}" for emotion, score in response.items() if emotion != "dominant_emotion"]
    response_string = ", ".join(score_strings)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again.", 400
    return f"For the given statement, the system response is {response_string}. The dominant emotion is {response['dominant_emotion']}."


@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
