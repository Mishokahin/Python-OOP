from project.second_hand_car import SecondHandCar

from unittest import TestCase, main


class TestSecondHandCar(TestCase):
    def test_successful_initialization(self):
        car = SecondHandCar("GTR", "supercar", 150, 150)
        self.assertEqual("GTR", car.model)
        self.assertEqual("supercar", car.car_type)
        self.assertEqual(150, car.mileage)
        self.assertEqual(150, car.price)
        self.assertEqual([], car.repairs)

    def test_price_is_zero(self):
        car = SecondHandCar("GTR", "supercar", 150, 100)
        with self.assertRaises(ValueError) as ve:
            car.price = 0
        self.assertEqual('Price should be greater than 1.0!', str(ve.exception))

    def test_mileage_is_less_than_one_hundred(self):
        car = SecondHandCar("GTR", "supercar", 150, 100)
        with self.assertRaises(ValueError) as ve:
            car.mileage = 50
        self.assertEqual('Please, second-hand cars only! Mileage must be greater than 100!', str(ve.exception))

    def test_promotion_is_successful(self):
        car = SecondHandCar("GTR", "supercar", 150, 150)
        self.assertEqual('The promotional price has been successfully set.', car.set_promotional_price(100))
        self.assertEqual(100, car.price)

    def test_promotion_price_is_incorrect(self):
        car = SecondHandCar("GTR", "supercar", 150, 100)
        with self.assertRaises(ValueError) as ve:
            car.set_promotional_price(150)
        self.assertEqual('You are supposed to decrease the price!', str(ve.exception))

    def test_car_is_repaired_successfully(self):
        car = SecondHandCar("GTR", "supercar", 150, 100)
        self.assertEqual(f'Price has been increased due to repair charges.', car.need_repair(25, "brakes"))
        self.assertEqual(125, car.price)
        self.assertEqual(["brakes"], car.repairs)

    def test_car_repairs_too_expensive(self):
        car = SecondHandCar("GTR", "supercar", 150, 100)
        self.assertEqual('Repair is impossible!', car.need_repair(200, "engine"))

    def test_gt_function_happy(self):
        car_1 = SecondHandCar("GTR", "supercar", 150, 100)
        car_2 = SecondHandCar("Supra", "supercar", 150, 150)

        self.assertFalse(car_1 > car_2)
        self.assertTrue(car_2 > car_1)

    def test_gt_function_unhappy(self):
        car_1 = SecondHandCar("GTR", "supercar", 150, 100)
        car_2 = SecondHandCar("350z", "sports", 150, 150)

        self.assertEqual('Cars cannot be compared. Type mismatch!', car_1 > car_2)

    def test_str_function_no_repairs(self):
        car = SecondHandCar("GTR", "supercar", 150, 100)
        expected = f"""Model {car.model} | Type {car.car_type} | Milage {car.mileage}km
Current price: {car.price:.2f} | Number of Repairs: {len(car.repairs)}"""
        self.assertEqual(expected, car.__str__())

if __name__ == "__main__":
    main()