import sys
sys.path.append('..')
import numpy as np

import argparse
import pickle
from common.trainer import Trainer
from common.optimizer import Adam
from cbow import CBOW
from skipgram import SkipGram
from common.util import create_contexts_target
from dataset import ptb

parser = argparse.ArgumentParser()
parser.add_argument('--model_name', type=str, help='name of model CBOW/Skipgram')
parser.add_argument('--epochs', type=int, help='number of epochs', default=10)
parser.add_argument('--batch_size', type=int, help='batch size', default=100)
parser.add_argument('--window_size', type=int, help='window size', default=5)
parser.add_argument('--hidden_size', type=int, help='hidden layer size', default=100)
args = parser.parse_args()

# 데이터 읽기
corpus, word_to_id, id_to_word = ptb.load_data('train')
vocab_size = len(word_to_id)

contexts, target = create_contexts_target(corpus, args.window_size)

# 모델 등 생성
if args.model_name == 'CBOW':
    model = CBOW(vocab_size, args.hidden_size, args.window_size, corpus)
elif args.model_name == 'Skipgram':
    model = SkipGram(vocab_size, args.hidden_size, args.window_size, corpus)

optimizer = Adam()
trainer = Trainer(model, optimizer)

# 학습 시작
trainer.fit(contexts, target, args.epochs, args.batch_size)
trainer.plot()

# 나중에 사용할 수 있도록 필요한 데이터 저장
word_vecs = model.word_vecs
params = {}
params['word_vecs'] = word_vecs.astype(np.float16)
params['word_to_id'] = word_to_id
params['id_to_word'] = id_to_word
pkl_file = 'model-{}-params.pkl'.format(args.model_name)
with open(pkl_file, 'wb') as f:
    pickle.dump(params, f, -1)