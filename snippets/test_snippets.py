import numpy as np
import random

from similar.orthographic_1 import function as ortho_1_sim
from similar.orthographic_2 import function as ortho_2_sim
from similar.orthographic_3 import function as ortho_3_sim
from similar.orthographic_4 import function as ortho_4_sim

from similar.semantic_1 import function as semantic_1_sim
from similar.semantic_2 import function as semantic_2_sim
from similar.semantic_3 import function as semantic_3_sim
from similar.semantic_4 import function as semantic_4_sim

from similar.phonological_1 import function as phono_1_sim
from similar.phonological_2 import function as phono_2_sim
from similar.phonological_3 import function as phono_3_sim
from similar.phonological_4 import function as phono_4_sim

from different.orthographic_1 import function as ortho_1_dif
from different.orthographic_2 import function as ortho_2_dif
from different.orthographic_3 import function as ortho_3_dif
from different.orthographic_4 import function as ortho_4_dif

from different.semantic_1 import function as semantic_1_dif
from different.semantic_2 import function as semantic_2_dif
from different.semantic_3 import function as semantic_3_dif
from different.semantic_4 import function as semantic_4_dif

from different.phonological_1 import function as phono_1_dif
from different.phonological_2 import function as phono_2_dif
from different.phonological_3 import function as phono_3_dif
from different.phonological_4 import function as phono_4_dif


def test_ortho_1():
    test_str = 'this is a test'

    dif_output = ortho_1_dif(test_str)
    sim_output = ortho_1_sim(test_str)

    assert dif_output == sim_output
    assert dif_output == 'THIS IS A TEST'


def test_ortho_2():
    test_list = [0, 1, 2, 3, 4, 5]

    dif_output = ortho_2_dif(test_list)
    sim_output = ortho_2_sim(test_list)

    assert dif_output == sim_output
    assert dif_output == ([0, 2, 4], [5, 3, 1])


def test_ortho_3():
    test_str = 'remove all the words starting with vowels!'

    dif_output = ortho_3_dif(test_str)
    sim_output = ortho_3_sim(test_str)

    assert dif_output == sim_output
    assert dif_output == ('all ', 'remove the words starting with vowels! ')


def test_ortho_4():
    test_players = ['Alex', 'Bella']
    test_scores = [[2, 2], [1, 1]]

    dif_output = ortho_4_dif(test_players, test_scores)
    sim_output = ortho_4_sim(test_players, test_scores)

    assert dif_output == sim_output
    assert dif_output == ('Bella', 'Alex')


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


def test_phono_4():

    test_y = [0, 1, 2, 3, 4]

    min_sim, max_sim = phono_4_sim(test_y)
    min_idx_sim, max_idx_sim = phono_4_sim(test_y, True)

    min_dif, max_dif = phono_4_dif(test_y)
    min_idx_dif, max_idx_dif = phono_4_dif(test_y, True)

    assert min_sim == 0 and max_sim == 4
    assert min_idx_sim == 0 and max_idx_sim == 4

    assert min_dif == 0 and max_dif == 4
    assert min_idx_dif == 0 and max_idx_dif == 4


def test_semantic_1():
    test_list_a = [2, "three", "four", 5, 6.7, "seven", "eight", 9, "ten"]
    test_list_b = ["zero", 1, "two", 4.5, 8, 16, "thirty-two", 64.0]

    dif_output = semantic_1_dif(test_list_a.copy(), test_list_b.copy())
    sim_output = semantic_1_sim(test_list_a.copy(), test_list_b.copy())
    print(dif_output)
    assert dif_output == sim_output
    assert dif_output == ([2, 5, 9, 1, 0, 8, 16, 0],
                          ['zero', 'two', 'thirty-two', 'three',
                           'four', '0', 'seven', 'eight', 'ten'])


def test_semantic_2():
    # function doesn't return anything
    pass


def test_semantic_3():
    test_list = ["string", "forget", "about", "i got strings", "whoz dat"]
    test_str = "strings are what i got strings are what i need"

    dif_output = semantic_3_dif(test_list, test_str)
    sim_output = semantic_3_sim(test_list, test_str)

    print(dif_output)
    assert dif_output == sim_output
    assert dif_output == ['o', 'r', 'g', 'e', 't', 'a', 'o', 't', 'w', 'h',
                          'o', ' ', 'd', 'a', 't']


def test_semantic_4():
    # function doesn't return anything
    pass
