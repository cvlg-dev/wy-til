import sys
sys.path.append('..')

import argparse
from common.trainer import Trainer
from common.optimizer import Adam
from model_simple_cbow import SimpleCBOW
from model_simple_skipgram import SimpleSkipGram
from common.util import preprocess, create_contexts_target, convert_one_hot

parser = argparse.ArgumentParser()
parser.add_argument('--model_name', type=str, help='name of model CBOW/Skipgram')
args = parser.parse_args()

text = 'You say goodbye and I say hello.'

WINDOW_SIZE = 1
HIDDEN_SIZE = 5
BATCH_SIZE = 3
MAX_EPOCH = 1000

corpus, word2id, id2word = preprocess(text)

vocab_size = len(word2id)
contexts, target = create_contexts_target(corpus, WINDOW_SIZE)
target = convert_one_hot(target, vocab_size)
contexts = convert_one_hot(contexts, vocab_size)

if args.model_name == 'CBOW':
    model = SimpleCBOW(vocab_size, HIDDEN_SIZE)
elif args.model_name == 'Skipgram':
    model = SimpleSkipGram(vocab_size, HIDDEN_SIZE)
optimizer = Adam()
trainer = Trainer(model, optimizer)


trainer.fit(contexts, target, MAX_EPOCH, BATCH_SIZE)
trainer.plot()

word_vecs = model.word_vecs
for word_id, word in id2word.items():
    print(word, word_vecs[word_id])