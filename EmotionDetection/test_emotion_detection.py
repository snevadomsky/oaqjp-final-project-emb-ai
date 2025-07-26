"""
Unit tests for emotion detection package
"""
import unittest
from emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    """
    Test class for emotion detection
    """
    def equal_function(self,input_value:str, expected:str):
        """
        Check if input results in expected string
        """
        self.assertEqual(emotion_detector(input_value)["dominant_emotion"],expected)

    def test_joy_dominant_emotion(self):
        """
        Test to see if input is joy
        """
        self.equal_function("I am glad this happened","joy")

    def test_anger_dominat_emotion(self):
        """
        Test to see if input is anger
        """
        self.equal_function("I am really mad about this","anger")

    def test_disgust_emotion(self):
        """
        Test to see if input is disgust
        """
        self.equal_function("I feel disgusted just hearing about this","disgust")

    def test_sadness_emotion(self):
        """
        Test to see if input is sadness
        """
        self.equal_function("I am so sad about this","sadness")

    def test_fear_emotion(self):
        """
        Test to see if input is fear
        """
        self.equal_function("I am really afraid that this will happen","fear")

if __name__ == 'main':
    unittest.main()
