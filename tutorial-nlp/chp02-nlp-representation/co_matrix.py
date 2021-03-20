import numpy as np
import argparse

from utils.read_text import read_text
from build_corpus import TokenBuilder


def create_co_matrix(corpus, vocab_size, window_size=1):
    corpus_size = len(corpus)

    co_matrix = np.zeros((vocab_size, vocab_size), dtype=np.int32)

    for idx, word_id in enumerate(corpus):
        for i in range(1, window_size+1):
            left_idx = idx-1
            right_idx = idx+1

            if left_idx > 0:

                left_word_id = corpus[left_idx]
                co_matrix[word_id, left_word_id] += 1

            if right_idx < corpus_size:
                right_word_id = corpus[right_idx]
                co_matrix[word_id, right_word_id] += 1

    return co_matrix


def cos_similarity(x, y, eps=1e-8):
    nx = x / np.sqrt(np.sum(x ** 2))
    ny = y / np.sqrt(np.sum(y ** 2))
    return np.dot(nx, ny)


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--path", type=str, help="path to text file")
    args = parser.parse_args()


    text = read_text(args.path)


    text_processor = TokenBuilder(text)
    text_processor.clean_text()
    text_processor.build_idx()


    co_matrix = create_co_matrix(corpus=text_processor.corpus, vocab_size=len(text_processor.id2word), window_size=1)

    t1 = co_matrix[text_processor.word2id["you"]]
    t2 = co_matrix[text_processor.word2id["i"]]

    print(cos_similarity(t1, t2))

    print(co_matrix)

