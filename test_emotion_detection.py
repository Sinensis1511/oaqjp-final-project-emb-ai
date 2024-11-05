import unittest
from EmotionDetection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test_joy(self):
        statement = "I am glad this happened"
        result = emotion_detector(statement)
        self.assertEqual(result['dominant_emotion'], 'joy', "Expected dominant emotion to be 'joy'.")

    def test_anger(self):
        statement = "I am really mad about this"
        result = emotion_detector(statement)
        self.assertEqual(result['dominant_emotion'], 'anger', "Expected dominant emotion to be 'anger'.")

    def test_disgust(self):
        statement = "I feel disgusted just hearing about this"
        result = emotion_detector(statement)
        self.assertEqual(result['dominant_emotion'], 'disgust', "Expected dominant emotion to be 'disgust'.")

    def test_sadness(self):
        statement = "I am so sad about this"
        result = emotion_detector(statement)
        self.assertEqual(result['dominant_emotion'], 'sadness', "Expected dominant emotion to be 'sadness'.")

    def test_fear(self):
        statement = "I am really afraid that this will happen"
        result = emotion_detector(statement)
        self.assertEqual(result['dominant_emotion'], 'fear', "Expected dominant emotion to be 'fear'.")

if __name__ == "__main__":
    unittest.main()
