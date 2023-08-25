from projects.cat import Cat

import unittest


class CatTests(unittest.TestCase):
    def setUp(self):
        self.cat = Cat("Pesho")

    def test_cat_size_is_increased_after_eating(self):
        expected_size = self.cat.size + 1
        self.cat.eat()
        self.assertEqual(expected_size, self.cat.size)

    def test_cat_is_fed_after_eating(self):
        self.cat.eat()
        self.assertTrue(self.cat.fed)

    def test_cat_cannot_eat_if_already_fed_raises_an_error(self):
        self.cat.eat()
        with self.assertRaises(Exception) as ex:
            self.cat.eat()
        self.assertEqual('Already fed.', str(ex.exception.args[0]))

    def test_cat_cannot_fall_asleep_if_not_fed_raises_an_error(self):
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()
        self.assertEqual('Cannot sleep while hungry', str(ex.exception.args[0]))

    def test_cat_is_not_sleepy_after_sleeping(self):
        self.cat.eat()
        self.assertTrue(self.cat.sleepy)
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)


if __name__ == "__main__":
    unittest.main()
