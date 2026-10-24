"""A small runnable example added to demonstrate the recovered 2024 library."""

from Vocabulary import (
    BagOfWordsEncoder,
    OneHotEncoder,
    SumEncoder,
    Vocabulary,
    closest_sentences,
    cosine_similarity,
    most_frequent_words,
)


def main():
    sentences = [
        "Python makes matrices useful",
        "Matrices make text useful",
        "Python makes text useful",
    ]
    vocabulary = Vocabulary(sentences)
    sentence = sentences[2]
    print("Vocabulary:", vocabulary.get_vocabulary())

    for encoder_type in (OneHotEncoder, SumEncoder):
        encoder = encoder_type(vocabulary)
        encoded = encoder.encode(sentence)
        print(f"\n{encoder_type.__name__} ({encoded.shape[0]} x {encoded.shape[1]}):")
        print(encoded)
        print("Decoded:", encoder.decode(encoded))

    bag = BagOfWordsEncoder(vocabulary)
    print("\nBag of words:", bag.sentence_to_bag_of_words(sentence))
    print("Word frequencies (%):", bag.calculate_word_frequency(sentences))
    print("Most frequent words:", most_frequent_words(sentences))
    print("Similarity of sentences 0 and 2:", cosine_similarity(sentences[0], sentences[2], vocabulary))
    first, second = closest_sentences(sentences, vocabulary)
    print(f"Closest sentences: {first} and {second}")
    print(" ", sentences[first])
    print(" ", sentences[second])


if __name__ == "__main__":
    main()
