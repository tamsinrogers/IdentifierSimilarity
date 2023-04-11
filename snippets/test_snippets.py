import numpy as np
import random

from similar.phonological_1 import function as phono_1_sim
from different.phonological_1 import function as phono_1_dif

from similar.phonological_2 import function as phono_2_sim
from different.phonological_2 import function as phono_2_dif

from similar.phonological_3 import function as phono_3_sim
from different.phonological_3 import function as phono_3_dif

from similar.phonological_4 import function as phono_4_sim
from different.phonological_4 import function as phono_4_dif


def test_phono_1():

    test_data = [0, 1, 2, 3, 2, 1, 0]
    test_ker = [1, 1, 1]

    # test version with similar identifiers
    unpad_out_sim = phono_1_sim(test_data, test_ker)
    pad_out_sim = phono_1_sim(test_data, test_ker, pad=True)

    assert len(unpad_out_sim) == len(test_data) - (len(test_ker) - 1)
    assert len(pad_out_sim) == len(test_data)

    # test version with different identifiers
    unpad_out_dif = phono_1_dif(test_data, test_ker)
    pad_out_dif = phono_1_dif(test_data, test_ker, pad=True)

    assert unpad_out_sim == unpad_out_dif
    assert pad_out_sim == pad_out_dif


def test_phono_2():

    def f(x): return x**2

    x = np.arange(4)
    y = f(x)

    points = [(x[i], y[i]) for i in range(len(x))]

    error_sim = phono_2_sim(points, f)
    error_dif = phono_2_dif(points, f)

    assert np.isclose(error_sim, 0)
    assert np.isclose(error_dif, 0)


def test_phono_3():

    random.seed(0)

    n = 100
    rho = 0.5

    array_sim = np.array(phono_3_sim(n, rho))
    array_dif = np.array(phono_3_dif(n, rho))

    assert array_sim.shape == (n, n)
    assert array_dif.shape == (n, n)

    assert np.isclose(np.mean(array_sim), 0.5, rtol=0.05)
    assert np.isclose(np.mean(array_dif), 0.5, rtol=0.05)
