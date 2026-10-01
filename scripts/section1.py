#!/usr/bin/env python3

import numpy as np

# add import and other helper functions here

if __name__ == "__main__":

    # code goes here

    np.random.seed(42)
    A = np.random.normal(size=(4, 4))
    B = np.random.normal(size=(4, 2))
    # print(A @ B)

    np.random.seed(42)
    X = np.random.normal(size=(4, 10))

    a = X[:, None, :]
    b = X[None, :, :]

    # c = np.sum(a - b, axis=2)
    c = np.square(a - b)
    c = np.sum(c, axis=2)
    # print(c)
