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
    test_str = "in 2 years, i will get three new pets!"

    dif_output = ortho_1_dif(test_str)
    sim_output = ortho_1_sim(test_str)

    assert dif_output == sim_output
    assert dif_output == 'IN 2 YEARS, I WILL GET THREE NEW PETS!'


def test_ortho_2():
    test_list = [6, 8, 35, 17, 0, 9, 45]

    dif_output = ortho_2_dif(test_list)
    sim_output = ortho_2_sim(test_list)

    assert dif_output == sim_output
    assert dif_output == ([0, 6, 8], [45, 35, 17, 9])


def test_ortho_3():
    test_str = "the inclination angle of some galaxy will affect the component of the"

    dif_output = ortho_3_dif(test_str)
    sim_output = ortho_3_sim(test_str)

    assert dif_output == sim_output
    assert dif_output == ('inclination angle of affect of ', 'the some galaxy will the component the ')


def test_ortho_4():
    test_players = ["Jerry", "George", "Newman"]
    test_scores = [
                [1, 2, 4, 3, 1, 1, 3],
                [4, 2, 1, 1, 1, 3, 1],
                [6, 2, 1, 3, 4, 3, 2]
            ]

    dif_output = ortho_4_dif(test_players, test_scores)
    sim_output = ortho_4_sim(test_players, test_scores)

    assert dif_output == sim_output
    assert dif_output == ('George', 'Newman')


def test_phono_1():

    # Test/Survey Function Parameters:
    # --------------------------------
    test_data = [0, 1, 2, 3, 2, 1, 0]
    test_ker = [1, 1, 1]

    # Expected Output/Answer:
    # -----------------------
    correct_pad = np.array([1, 3, 6, 7, 6, 3, 1])
    correct_no_pad = np.array([3, 6, 7, 6, 3])

    # test both versions of the function with padding
    pad_sim = np.array(phono_1_sim(test_data, test_ker, pad=True))
    pad_dif = np.array(phono_1_dif(test_data, test_ker, pad=True))

    assert pad_sim.all() == correct_pad.all()
    assert pad_dif.all() == correct_pad.all()

    # test both versions of the function without padding
    no_pad_sim = np.array(phono_1_sim(test_data, test_ker))
    no_pad_dif = np.array(phono_1_dif(test_data, test_ker))

    assert no_pad_sim.all() == correct_no_pad.all()
    assert no_pad_dif.all() == correct_no_pad.all()


def test_phono_2():

    # Test/Survey Function Parameters:
    # --------------------------------
    def f(x): return 2*x

    points = [(0, 1),
              (1, 1),
              (2, 3),
              (3, 6),
              (4, 10)]

    # Expected Output/Answer:
    # -----------------------
    correct_result = 1.4

    # test both versions of the function
    error_sim = phono_2_sim(points, f)
    error_dif = phono_2_dif(points, f)

    assert error_sim == correct_result
    assert error_dif == correct_result


def test_phono_3():

    # phonological_3.py uses random, so the survey question can't ask
    # what the EXACT output will be. I think the best way to phrase
    # it is something along the lines of: "Which of the following is a
    # plausible output of the function?"
    random.seed(0)

    # Test/Survey Function Parameters:
    # --------------------------------
    n = 3
    rho = 0.5

    # Expected Output/Answer:
    # -----------------------
    correct_result = np.array([
        [0, 0, 1],
        [1, 0, 1],
        [0, 1, 1]])

    # test both versions of the function
    array_sim = np.array(phono_3_sim(n, rho))
    array_dif = np.array(phono_3_dif(n, rho))

    assert array_sim.all() == correct_result.all()
    assert array_dif.all() == correct_result.all()


def test_phono_4():

    # Test/Survey Function Parameters:
    # --------------------------------
    n = 3
    s = 2

    # Expected Output/Answer:
    # -----------------------
    correct_result = np.array([
        [2, 0, 0],
        [0, 2, 0],
        [0, 0, 2]])

    mat_sim = np.array(phono_4_sim(n, s))
    mat_dif = np.array(phono_4_dif(n, s))

    assert mat_sim.all() == correct_result.all()
    assert mat_dif.all() == correct_result.all()


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
    # printed output:

    # False
    # b
    # i
    # False
    # False
    # False
    # False

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

    # printed output:
    # 0
    # 5
    # 1
    # 0

    pass
