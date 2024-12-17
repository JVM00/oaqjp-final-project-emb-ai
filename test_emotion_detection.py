import unittest
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetection(unittest.TestCase):

    def test_emotion_detector(self):
        # Test case :joy """
        emotions_1 = emotion_detector("I am glad this happened")
        self.assertEqual(emotions_1["dominant_emotion"], "joy")
        # Test case :anger
        emotions_2 = emotion_detector("I am really mad about this")
        self.assertEqual(emotions_2["dominant_emotion"], "anger")
       # Test case : disgust 
        emotions_3 = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(emotions_3["dominant_emotion"], "disgust")
       # Test case : sadness
        emotions_4 = emotion_detector("I am so sad about this")
        self.assertEqual(emotions_4["dominant_emotion"], "sadness")
       # Test case :  fear 
        emotions_5 = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(emotions_5["dominant_emotion"], "fear")

if __name__ == '__main__':
    unittest.main()