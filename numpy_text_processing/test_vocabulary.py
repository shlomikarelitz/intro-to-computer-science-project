import unittest

import numpy as np

from Vocabulary import (
    BagOfWordsEncoder,
    OneHotEncoder,
    SumEncoder,
    Vocabulary,
    closest_sentences,
    cosine_similarity,
    most_frequent_words,
)


class VocabularyRegressionTests(unittest.TestCase):
    def test_normalization_deduplication_and_lookup(self):
        vocabulary = Vocabulary(["Hello, NUMPY! hello"])
        self.assertEqual(vocabulary.get_vocabulary(), ["hello", "numpy"])
        self.assertEqual(vocabulary.tokenize("NUMPY hello"), ["numpy", "hello"])
        self.assertIsNone(vocabulary.tokenize("unknown"))
        self.assertEqual(vocabulary[["hello", 1]], [0, "numpy"])

    def test_one_hot_shape_values_and_round_trip(self):
        encoder = OneHotEncoder(Vocabulary(["red green blue"]))
        encoded = encoder.encode("red blue red")
        np.testing.assert_array_equal(encoded, [[0, 0, 1], [1, 0, 0], [0, 0, 1]])
        self.assertEqual(encoder.decode(encoded), "red blue red")

    def test_cumulative_encoding_and_round_trip(self):
        encoder = SumEncoder(Vocabulary(["red green blue"]))
        encoded = encoder.encode("red blue green")
        np.testing.assert_array_equal(encoded, [[1, 1, 1], [1, 0, 0], [1, 1, 0]])
        self.assertEqual(encoder.decode(encoded), "red blue green")

    def test_counts_frequencies_and_tied_most_frequent_words(self):
        sentences = ["red red blue", "blue green"]
        encoder = BagOfWordsEncoder(Vocabulary(sentences))
        np.testing.assert_array_equal(encoder.sentence_to_bag_of_words(sentences[0]), [1, 0, 2])
        np.testing.assert_array_equal(encoder.calculate_word_frequency(sentences), [40, 20, 40])
        self.assertEqual(most_frequent_words(sentences), ["blue", "red"])

    def test_out_of_vocabulary_bag_raises_original_error(self):
        with self.assertRaisesRegex(ValueError, "wrong sentence"):
            BagOfWordsEncoder(Vocabulary(["red blue"])).sentence_to_bag_of_words("green")

    def test_cosine_similarity(self):
        vocabulary = Vocabulary(["red green blue"])
        self.assertEqual(cosine_similarity("red blue", "blue red", vocabulary), 1.0)
        self.assertEqual(cosine_similarity("red", "green", vocabulary), 0.0)

    def test_closest_sentences_ignores_self_similarity(self):
        sentences = [
            "Python makes matrices useful",
            "Matrices make text useful",
            "Python makes text useful",
        ]
        self.assertEqual(closest_sentences(sentences, Vocabulary(sentences)), [0, 2])


if __name__ == "__main__":
    unittest.main()
