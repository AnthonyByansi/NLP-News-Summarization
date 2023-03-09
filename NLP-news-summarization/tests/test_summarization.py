import unittest
from summarization.extractive import summarize_extractive
from summarization.abstractive import summarize_abstractive

class TestSummarization(unittest.TestCase):
    def test_summarize_extractive(self):
        text = "This is a test sentence. This is another test sentence."
        expected_summary = "This is a test sentence."
        self.assertEqual(summarize_extractive(text), expected_summary)

    def test_summarize_abstractive(self):
        text = "This is a test sentence. This is another test sentence."
        expected_summary = "This is a test."
        self.assertEqual(summarize_abstractive(text), expected_summary)

if __name__ == '__main__':
    unittest.main()
