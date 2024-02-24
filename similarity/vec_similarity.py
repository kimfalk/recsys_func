import numpy as np
from numpy.linalg import norm

epsilon = 0.00001

def cosine_sim(a: list[float], b: list[float]) -> float:

    a = np.array(a)
    b = np.array(b)
    return np.dot(a,b)/(norm(a)*norm(b))

def cosine_sim(a: list[float], b: list[float]) -> float:

    a = np.array(a)
    b = np.array(b)
    return np.dot(a,b)/(norm(a)*norm(b))
