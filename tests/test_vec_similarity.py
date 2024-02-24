import similarity.vec_similarity

import pytest




class TestCosine:

    def test_equal_vecs(self):
        a = [0.1, 0.2, 0.3]
        assert similarity.vec_similarity.cosine_sim(a, a) == 1

    def test_orthogonal(self):
        a = [1.0, 0.0, 0.0]
        b = [0.0, 0.0, 1.0]
        assert similarity.vec_similarity.cosine_sim(a, b) == 0