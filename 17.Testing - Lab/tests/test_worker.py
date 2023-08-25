from projects.worker import Worker

import unittest


class WorkerTests(unittest.TestCase):
    def test_correct_worker_initialization(self):
        worker = Worker("Pesho", 100, 5)
        self.assertEqual("Pesho", worker.name)
        self.assertEqual(100, worker.salary)
        self.assertEqual(5, worker.energy)
        self.assertEqual(0, worker.money)

    def test_worker_is_resting(self):
        worker = Worker("Pesho", 100, 0)
        expected_energy = worker.energy + 1
        worker.rest()
        self.assertEqual(expected_energy, worker.energy)

    def test_worker_salary_is_increased_after_working(self):
        worker = Worker("Pesho", 100, 5)
        expected_money = worker.money + worker.salary
        worker.work()
        self.assertEqual(expected_money, worker.money)

    def test_worker_energy_is_decreased_after_working(self):
        worker = Worker("Pesho", 100, 5)
        expected_energy = worker.energy - 1
        worker.work()
        self.assertEqual(expected_energy, worker.energy)

    def test_worker_is_tired_cannot_work(self):
        worker = Worker("Pesho", 100, 0)
        with self.assertRaises(Exception) as ex:
            worker.work()
        self.assertEqual("Not enough energy.", ex.exception.args[0])

    def test_worker_is_too_tired_cannot_work(self):
        worker = Worker("Pesho", 100, -1)
        with self.assertRaises(Exception) as ex:
            worker.work()
        self.assertEqual("Not enough energy.", ex.exception.args[0])

    def test_worker_info(self):
        worker = Worker("Pesho", 100, 5)
        expected = "Pesho has saved 0 money."
        actual = worker.get_info()
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()