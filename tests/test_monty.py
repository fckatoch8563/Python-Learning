import unittest

from my_file import compute_final_choice, simulate_round


class TestMontyLogic(unittest.TestCase):
    def test_compute_final_choice_switch(self):
        # if player switches, the final choice must be the door that's neither the first nor the goat
        self.assertEqual(compute_final_choice(0, 1, True), 2)
        self.assertEqual(compute_final_choice(1, 2, True), 0)
        self.assertEqual(compute_final_choice(2, 0, True), 1)

    def test_compute_final_choice_stay(self):
        # if player stays, final choice == first_choice
        self.assertEqual(compute_final_choice(0, 1, False), 0)
        self.assertEqual(compute_final_choice(1, 2, False), 1)

    def test_simulate_round_win_lose(self):
        # car at 0, first picks 1, goat revealed 2
        final, won = simulate_round(0, 1, 2, True)
        self.assertEqual(final, 0)
        self.assertTrue(won)

        final, won = simulate_round(1, 1, 2, False)
        self.assertEqual(final, 1)
        self.assertTrue(won)


if __name__ == "__main__":
    unittest.main()
