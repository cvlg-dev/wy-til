import sys
sys.path.append('..')

import numpy as np
from common.layers import MatMul
from common.functions import softmax
from common.util import preprocess

if __name__ == "__main__":

    # Sample inputs
    c0 = np.array([[1, 0, 0, 0, 0, 0, 0]])
    c1 = np.array([[0, 0, 1, 0, 0, 0, 0]])

    # Initialize weight
    W_in = np.random.randn(7, 3)
    W_out = np.random.randn(3, 7)

    # Create layers
    in_layer0 = MatMul(W_in)
    in_layer1 = MatMul(W_in)
    out_layer = MatMul(W_out)

    # Foward propagation
    h0 = in_layer0.forward(c0)
    h1 = in_layer1.forward(c1)

    h = (h0 + h1) * 0.5
    s = out_layer.forward(h)

    output = softmax(s)
    print(s)
    print(output)
