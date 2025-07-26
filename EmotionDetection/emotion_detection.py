"""
Emotion Detector module using Watson NLP to predict the given emotion of the input string
"""
import json
import operator
import requests

def emotion_detector(text_to_analyze:str):
    """
    Analyzes the emotional attribute of given string
    """
    request_url= "https://sn-watson-emotion.labs.skills.network\
/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    request_headers= {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    request_json = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(request_url, json= request_json, headers= request_headers, timeout=120)
    emotions = dict()
    if(response.status_code == 200):
        emotions = json.loads(response.text)['emotionPredictions'][0]['emotion']
        #Get emotion with the highest value
        emotions["dominant_emotion"] = max(emotions.items(),key=operator.itemgetter(1))[0]
    #Handle all other status codes including response.status_code == 400
    else:
        emotions["dominant_emotion"] = "None"
    return emotions
