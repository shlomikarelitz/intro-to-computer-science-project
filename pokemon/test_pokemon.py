import contextlib
import io
import runpy
import unittest
from pathlib import Path

from Battle import Battle
from Blastoise import Blastoise
from Pikachu import Pikachu
from Trainer import Trainer


class PokemonRegressionTests(unittest.TestCase):
    def test_original_duel_and_final_hit_points(self):
        pika = Pikachu("pika", 40, "electric", 26, 90, 63, 85, 2)
        blasty = Blastoise("blasty", 43, "water", 37, 82, 93, 113)
        ash = Trainer("ash", 18, 6.0, [pika])
        misty = Trainer("misty", 18, 5.5, [blasty])
        with contextlib.redirect_stdout(io.StringIO()):
            outcome = Battle(ash, misty).dual_battle(0, 0)
        self.assertEqual(outcome, (4, 1))
        self.assertEqual(ash.get_pokemon_lst()[0].get_hit_points(), 33)
        self.assertEqual(misty.get_pokemon_lst()[0].get_hit_points(), -2)

    def test_original_four_pokemon_team_battle(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            runpy.run_path(str(Path(__file__).with_name("example3.py")), run_name="__main__")
        self.assertIn("Trainer misty won the battle in 15 rounds", output.getvalue())

    def test_mutating_a_returned_pokemon_does_not_change_trainer(self):
        ash = Trainer("ash", 18, 6.0, [Pikachu("pika", 40, "electric", 26, 90, 63, 85, 2)])
        returned = ash.get_pokemon_lst()
        returned[0].absorb(10)
        returned.clear()
        self.assertEqual(len(ash), 1)
        self.assertEqual(ash.get_pokemon_lst()[0].get_hit_points(), 90)


if __name__ == "__main__":
    unittest.main()
