# NumPy Text Processing - Recovered HW4

A small text-processing library from July 2024. It turns sentences into vocabulary-indexed matrices and vectors, then uses those representations to count words and compare sentences.

## Components

| Component | Purpose |
| --- | --- |
| `Vocabulary` | Lowercase/punctuation handling, sorted unique words, tokenization, and word/index lookup |
| `OneHotEncoder` | A one-hot matrix with one row per word in the sentence |
| `SumEncoder` | Cumulative/thermometer encoding and decoding |
| `BagOfWordsEncoder` | Per-word counts and corpus frequency percentages |
| `most_frequent_words` | All words tied for the highest frequency |
| `cosine_similarity` | Similarity of two bag-of-words vectors |
| `closest_sentences` | Pairwise similarity matrix and the closest sentence indices |

## Run

Install the repository's requirements using Python 3.12, then run from the repository root:

```text
python numpy_text_processing/demo.py
python -m unittest discover -s numpy_text_processing -p "test_*.py" -v
```

The demo prints a vocabulary, encoding matrices, decoded sentences, frequency percentages, and the closest pair of sentences. No dataset download or API key is required.

## Example

When running inside this directory:

```python
from Vocabulary import Vocabulary, OneHotEncoder, cosine_similarity

vocabulary = Vocabulary(["red green blue"])
encoder = OneHotEncoder(vocabulary)
matrix = encoder.encode("red blue red")
print(matrix)
# [[0 0 1]
#  [1 0 0]
#  [0 0 1]]
print(encoder.decode(matrix))
# red blue red
print(cosine_similarity("red blue", "blue red", vocabulary))
# 1.0
```

The encoders expect words from the vocabulary. The original implementation's edge-case behavior is retained, including returning `None` for unsuccessful tokenization and raising an error for unknown words in bag-of-words conversion. It is historical coursework, not a redesigned production NLP package.

## Recovery provenance

The on-disk source had been overwritten. `Vocabulary.py` was reconstructed from the surviving **CPython 3.12 cache dated 17 July 2024**, and all 30 code objects were verified against it. The recovered executable code matches; comments and formatting are reconstructed. See [RECOVERY.md](RECOVERY.md) and [recovery_manifest.json](recovery_manifest.json).
