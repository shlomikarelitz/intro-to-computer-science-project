# Recovered from the surviving July 2024 CPython cache; see RECOVERY.md.
import numpy as np


class Vocabulary:
    def __init__(self, sentences=None):
        if sentences is not None:
            self.__sentences = sentences
            self.create_vocabulary(self.__sentences)

    def __len__(self):
        return len(self.__sentences)

    def get_out_spaces(self, sentences):
        if not isinstance(sentences, list):
            sentences = [sentences]
        list_of_voc = []
        for sentence in sentences:
            temp = sentence.lower()
            temp = temp.split()
            temp2 = []
            for word in temp:
                temp3 = ""
                len_of_word = len(word) - 1
                i = 0
                for letter in word:
                    if letter.isalnum():
                        temp3 += letter
                    elif len_of_word > i:
                        temp2.append(temp3)
                        temp3 = ""
                    i += 1
                temp2.append(temp3)
            list_of_voc.extend(temp2)
        return list_of_voc

    def sorted_by_ascii(self, list):
        return sorted(list, key=ascii)

    def remove_double_words(self, list_of_voc):
        final_list = []
        for word in list_of_voc:
            if word not in final_list:
                final_list.append(word)
        return final_list

    def sorted_list_of_sentences_by_ascii(self, sentences):
        list_ok = self.get_out_spaces(sentences)
        list_of_voc = self.sorted_by_ascii(list_ok)
        final_list = self.remove_double_words(list_of_voc)
        return final_list

    def create_vocabulary(self, sentences):
        sorted_ls = self.sorted_list_of_sentences_by_ascii(sentences)
        self.__sentences = sorted_ls

    def extend_vocabulary(self, new_sentences):
        temp_list = []
        for i in range(len(new_sentences)):
            new_sentences = str(new_sentences[i].lower())
            new_sentences = new_sentences.split()
            for word in new_sentences:
                if word in self.__sentences:
                    continue
                else:
                    temp_list.append(word)
        self.__sentences.extend(temp_list)
        f = sorted(self.__sentences, key=ascii)
        self.__sentences = f

    def tokenize(self, sentence):
        sentence = self.get_out_spaces(sentence)
        temp_ls = []
        for sn in sentence:
            if sn in self.__sentences:
                temp_ls.append(sn)
            if sn not in self.__sentences:
                return None
        if len(temp_ls) > 0:
            return temp_ls
        else:
            return None

    def get_vocabulary(self):
        return self.__sentences

    def change_voc(self, sentence):
        self.__sentences = sentence

    def __getitem__(self, key):
        if isinstance(key, list):
            ls = []
            for ke in key:
                if isinstance(ke, int):
                    ls.append(self.__sentences[int(ke)])
                else:
                    ls.append(self.__sentences.index(ke))
        elif isinstance(key, int):
            return self.__sentences[key]
        else:
            return self.__sentences.index(key)
        return ls


class OneHotEncoder:
    def __init__(self, vocabulary):
        self.__vocabulary = vocabulary

    def encode(self, sentence):
        sentence = self.__vocabulary.tokenize(sentence)
        a = np.zeros((len(sentence), len(self.__vocabulary)), dtype=np.int8)
        sen = np.array(sentence)
        sen = np.tile(sen, (len(self.__vocabulary), 1))
        voc = np.array(self.__vocabulary)
        voc = np.tile(voc.T, (len(sentence), 1)).T
        s = (sen == voc).T * 1
        return s

    def decode(self, encoding):
        b = np.array(self.__vocabulary)
        coping = np.array(encoding.nonzero())
        a = b[coping[1]]
        re = " ".join(a)
        return re


class SumEncoder:
    def __init__(self, vocabulary):
        self.__vocabulary = vocabulary

    def encode(self, sentence):
        sentence = self.__vocabulary.tokenize(sentence)
        a = np.zeros((len(sentence), len(self.__vocabulary)), dtype=np.int8)
        sen = np.array(sentence)
        sen = np.tile(sen, (len(self.__vocabulary), 1))
        voc = np.array(self.__vocabulary)
        voc = np.tile(voc.T, (len(sentence), 1)).T
        s = (sen == voc).T * 1
        condi = np.argmax(s == 1, axis=1)
        mask = np.arange(a.shape[1]) < condi[:, None]
        s[mask] = 1
        return s

    def decode(self, encoding):
        b = np.array(self.__vocabulary)
        copy_encoding = encoding[:, ::-1]
        coping = np.argmax(copy_encoding == 1, axis=1)
        coping1 = len(self.__vocabulary) - coping - 1
        a = b[coping1]
        re = " ".join(a)
        return re


class BagOfWordsEncoder:
    def __init__(self, vocabulary):
        self.__vocabulary = vocabulary

    def sentence_to_bag_of_words(self, sentence):
        copy_vocabulary = list(self.__vocabulary)
        bag_of_word = [0] * len(self.__vocabulary)
        sentence = Vocabulary.get_out_spaces(self, sentence)
        for word in sentence:
            if word in copy_vocabulary:
                ind = copy_vocabulary.index(word)
                bag_of_word[ind] += 1
            else:
                raise ValueError("wrong sentence!!")
        bag_of_word = np.array(bag_of_word, dtype=np.int32)
        return bag_of_word

    def calculate_word_frequency(self, sentences):
        list_of_everage = np.zeros(len(self.__vocabulary))
        count_of_len = 0
        for sentence in sentences:
            list_of_everage += self.sentence_to_bag_of_words(sentence)
            count_of_len += len(sentence.split())
        list_of_everage = list_of_everage / count_of_len * 100
        list_of_everage = np.round(list_of_everage, decimals=4)
        return list_of_everage


def most_frequent_words(sentences):
    voc = Vocabulary(sentences)
    bag = BagOfWordsEncoder(voc)
    freq = bag.calculate_word_frequency(sentences)
    final_ls = np.where(freq == np.max(freq))[0]
    final_ls = final_ls.tolist()
    return voc[final_ls]


def cosine_similarity(sentence1, sentence2, vocabulary):
    bag = BagOfWordsEncoder(vocabulary)
    voc_1 = bag.sentence_to_bag_of_words(sentence1)
    voc_2 = bag.sentence_to_bag_of_words(sentence2)
    res = np.dot(voc_1, voc_2)
    norma1 = np.dot(voc_1, voc_1) ** 0.5
    norma2 = np.dot(voc_2, voc_2) ** 0.5
    final_res = res / (norma1 * norma2)
    final_res = np.round(final_res, decimals=4)
    return final_res


def closest_sentences(sentences, vocabulary):
    def func_(vec1, vec2):
        return cosine_similarity(vec1, vec2, vocabulary)

    array_of_sent = np.array(sentences)
    array_of_sent = np.tile(array_of_sent, (len(array_of_sent), 1))
    vec_t = array_of_sent.T
    vec_1 = array_of_sent[:, ::-1]
    vectorizing_cosine = np.frompyfunc(func_, 2, 1)
    vectorizing_cosine = vectorizing_cosine(vec_t, vec_1)
    vectorizing_cosine = vectorizing_cosine[:, ::-1]
    vectorizing_cosine = vectorizing_cosine.astype(float)
    indices = np.diag_indices_from(vectorizing_cosine)
    vectorizing_cosine[indices] = 0
    ind = np.argmax(vectorizing_cosine)
    ind = np.unravel_index(ind, vectorizing_cosine.shape)
    ind = list(map(int, ind))
    return ind
