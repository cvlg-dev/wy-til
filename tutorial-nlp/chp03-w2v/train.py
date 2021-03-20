import sys
sys.path.append('..')

from common.trainer import Trainer
from common.optimizer import Adam
from model_simple_cbow import SimpleCBOW
from common.util import preprocess, create_contexts_target, convert_one_hot


text = "You say goodbye and I say hello"

WINDOW_SIZE = 1
HIDDEN_SIZE = 5
BATCH_SIZE = 3
MAX_EPOCH = 1000

corpus, word2id, id2word = preprocess(text)

vocab_size = len(word2id)
contexts, target = create_contexts_target(corpus, WINDOW_SIZE)
target = convert_one_hot(target, vocab_size)
contexts = convert_one_hot(contexts, vocab_size)

model = SimpleCBOW(vocab_size, HIDDEN_SIZE)
optimizer = Adam()
trainer = Trainer(model, optimizer)


trainer.fit(contexts, target, MAX_EPOCH, BATCH_SIZE)
trainer.plot()
