import pytest

def average(values):
    """calcule la moyenne des éléments de `values`.

    lève ValueError si la liste est vide.
    """
    vals = list(values)
    if not vals:
        raise ValueError("liste vide")
    return sum(vals) / len(vals)

def test_average_simple():
    assert average([1, 2, 3, 4]) == 2.5

def test_average_floats_and_negatives():
    assert average([1.5, -0.5, 2.0]) == 1.0

def test_average_single_element():
    assert average([42]) == 42

def test_average_empty_raises():
    with pytest.raises(ValueError):
        average([])

if __name__ == "__main__":
    #exemple
    print("exemple: moyenne de [1, 2, 3] ->", average([1, 2, 3]))