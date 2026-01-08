# tests pour la fonction average, commentaires sympa et minuscules

import pytest
from job import average


def test_average_simple():
    assert average([1, 2, 3, 4]) == 2.5


def test_average_floats_and_negatives():
    assert average([1.5, -0.5, 2.0]) == pytest.approx(1.0)


def test_average_single_element():
    assert average([42]) == 42


def test_average_empty_raises():
    with pytest.raises(ValueError):
        average([])
