import timeit

import numpy as np


def solve_monty_hall_version_2_numpy():
    repeats = 1_000_000
    doors = np.zeros((repeats, 3))
    doors[:, 0] = 1  # place the car behind door 0

    rng = np.random.default_rng()
    rng.permuted(doors, axis=1, out=doors)

    doors[:, 1:].sort()
    means = doors.mean(axis=0)

    print(f"The success rate when switching is " f"{means[2]:.3%}")

    print(f"The success rate when keeping is " f"{means[0]:.3%}")


print(
    timeit.timeit(
        "solve_monty_hall_version_2_numpy()",
        globals=globals(),
        number=10,
    )
)
