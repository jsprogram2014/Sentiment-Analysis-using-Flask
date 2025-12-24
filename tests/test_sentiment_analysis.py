from SentimentAnalysis.sentiment_analysis import sentiment_analyzer
import unittest

class TestSentimentAnalyzer(unittest.TestCase):
    def test_sentiment(self):
        self.assertEqual({'label': 'positive'},sentiment_analyzer('this is fun'))
        self.assertEqual({'label': 'negative'},sentiment_analyzer('I hate working with Python'))
        self.assertEqual({'label': 'neutral'},sentiment_analyzer('I am neutral on Python'))

if __name__=='__main__':
    unittest.main()
