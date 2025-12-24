from SentimentAnalysis.sentiment_analysis import sentiment_analyzer
import unittest

class UnitTest(unittest.TestCase):
    def test_sentiment(self):
        self.assertEqual({'label':'positive','score':0.5106},sentiment_analyzer('this is fun'))

if __name__=='__main__':
    unittest.main()
