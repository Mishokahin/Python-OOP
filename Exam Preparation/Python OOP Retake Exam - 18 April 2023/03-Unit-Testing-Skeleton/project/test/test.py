from project.tennis_player import TennisPlayer

from unittest import TestCase, main


class TestTennisPlayer(TestCase):
    def setUp(self) -> None:
        self.tennis_player = TennisPlayer("Marina", 20, 1.0)

    def test_correct_initialization(self):
        self.assertEqual("Marina", self.tennis_player.name)
        self.assertEqual(20, self.tennis_player.age)
        self.assertEqual(1.0, self.tennis_player.points)
        self.assertEqual([], self.tennis_player.wins)

    def test_name_is_less_than_two_symbols(self):
        with self.assertRaises(ValueError) as ve:
            self.tennis_player.name = "Y"
        self.assertEqual("Name should be more than 2 symbols!", str(ve.exception))

    def test_name_is_two_symbols_long(self):
        with self.assertRaises(ValueError) as ve:
            self.tennis_player.name = "Ye"
        self.assertEqual("Name should be more than 2 symbols!", str(ve.exception))

    def test_tennis_player_is_underage(self):
        with self.assertRaises(ValueError) as ve:
            self.tennis_player.age = 17
        self.assertEqual("Players must be at least 18 years of age!", str(ve.exception))

    def test_adding_a_new_win(self):
        self.tennis_player.add_new_win("Rolex Open")
        self.assertEqual(["Rolex Open"], self.tennis_player.wins)

    def test_adding_already_existing_win_again(self):
        self.tennis_player.add_new_win("Rolex Open")
        self.assertEqual(f"Rolex Open has been already added to the list of wins!",
                         self.tennis_player.add_new_win("Rolex Open"))

    def test_lt_function_if_first_player_is_better(self):
        other_player = TennisPlayer("Maria", 21, 0.0)
        self.assertEqual("Marina is a better player than Maria", self.tennis_player < other_player)

    def test_lt_function_if_other_player_is_better(self):
        other_player = TennisPlayer("Maria", 21, 12.0)
        self.assertEqual("Maria is a top seeded player and he/she is better than Marina",
                         self.tennis_player < other_player)

    def test_str_function_no_wins(self):
        expected = f"Tennis Player: {self.tennis_player.name}\n" \
               f"Age: {self.tennis_player.age}\n" \
               f"Points: {self.tennis_player.points:.1f}\n" \
               f"Tournaments won: {', '.join(self.tennis_player.wins)}"

        self.assertEqual(expected, str(self.tennis_player))

    def test_str_function_no_one_win(self):
        self.tennis_player.wins = ["Rolex Open"]
        expected = f"Tennis Player: {self.tennis_player.name}\n" \
               f"Age: {self.tennis_player.age}\n" \
               f"Points: {self.tennis_player.points:.1f}\n" \
               f"Tournaments won: {', '.join(self.tennis_player.wins)}"

        self.assertEqual(expected, str(self.tennis_player))


if __name__ == "__main__":
    main()