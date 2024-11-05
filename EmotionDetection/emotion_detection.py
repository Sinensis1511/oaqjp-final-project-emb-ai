import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    json_data = {"raw_document": {"text": text_to_analyse}}

    # Send POST request
    response = requests.post(url, headers=headers, json=json_data)

    # Check if the response is successful
    if response.status_code == 200:
        # Convert the response text to a dictionary
        response_data = response.json()
        
       

        # Extract scores for each required emotion
        emotions = {
            'anger': response_data.get('anger', 0),
            'disgust': response_data.get('disgust', 0),
            'fear': response_data.get('fear', 0),
            'joy': response_data.get('joy', 0),
            'sadness': response_data.get('sadness', 0)
        }

        # Find the dominant emotion based on the highest score
        dominant_emotion = max(emotions, key=emotions.get)
        emotions['dominant_emotion'] = dominant_emotion

        return emotions

    else:
        # Print the error if the request was unsuccessful
        print(f"Error: {response.status_code}, {response.text}")
        return {}

# Testing the function directly
if __name__ == "__main__":
    test_text = "I love this new technology."
    result = emotion_detector(test_text)
    print(result)
