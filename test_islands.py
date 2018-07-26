from random import randint
import islands


def test_is_island():
    n = 10
    size = randint(0, n)
    visited = [[0 for r in range(size)] for r in range(size)]

    assert isinstance(islands.is_island(
                      randint(0, n), randint(0, n), visited), int)

    return islands.is_island(randint(0, n), randint(0, n), visited)


if __name__ == "__main__":
    x = test_is_island()
    print(type(x))
