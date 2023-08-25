from unittest import TestCase, main

from project.trip import Trip


class TestTrip(TestCase):
    def test_correct_initialization(self):
        single_traveler = Trip(10000.0, 1, False)
        self.assertEqual(single_traveler.budget, 10000.0)
        self.assertEqual(single_traveler.travelers, 1)
        self.assertEqual(single_traveler.is_family, False)
        self.assertEqual(single_traveler.booked_destinations_paid_amounts, {})

    def test_not_enough_travelers(self):
        no_traveler = Trip(10000.0, 1, False)
        with self.assertRaises(ValueError) as ve:
            no_traveler.travelers = 0
        self.assertEqual('At least one traveler is required!', str(ve.exception))

    def test_single_traveler_posing_as_a_family(self):
        single_traveler = Trip(10000.0, 1, True)
        self.assertFalse(single_traveler.is_family)

    def test_family_happy_case(self):
        family = Trip(10000.0, 2, True)
        self.assertTrue(family.is_family)

    def test_destination_not_available(self):
        single_traveler = Trip(10000.0, 1, False)
        destination = "China"
        self.assertEqual('This destination is not in our offers, please choose a new one!',
                         single_traveler.book_a_trip(destination))

    def test_not_enough_budget_single_traveler(self):
        single_traveler = Trip(5000.0, 1, False)
        destination = 'New Zealand'
        self.assertEqual('Your budget is not enough!', single_traveler.book_a_trip(destination))

    def test_not_enough_budget_family(self):
        family = Trip(10000.0, 2, True)
        destination = 'New Zealand'
        self.assertEqual('Your budget is not enough!', family.book_a_trip(destination))

    def test_enough_budget_single_traveler(self):
        single_traveler = Trip(10000.0, 1, False)
        destination = 'New Zealand'
        budget = 10000.0 - 7500.0
        self.assertEqual(f'Successfully booked destination {destination}! Your budget left is {budget:.2f}',
                         single_traveler.book_a_trip(destination))

    def test_enough_budget_family(self):
        family = Trip(30000.0, 2, True)
        destination = 'New Zealand'
        budget = 30000.0 - ((7500.0 * 2) * 0.9)
        self.assertEqual(f'Successfully booked destination {destination}! Your budget left is {budget:.2f}',
                         family.book_a_trip(destination))

    def test_no_trips_booked(self):
        single_traveler = Trip(10000.0, 1, False)
        self.assertEqual("No bookings yet. Budget: 10000.00", single_traveler.booking_status())

    def test_one_trip_booked_single_traveler(self):
        single_traveler = Trip(10000.0, 1, False)
        destination = 'New Zealand'
        single_traveler.book_a_trip(destination)
        expected = "\n".join(["Booked Destination: New Zealand", "Paid Amount: 7500.00",
                              "Number of Travelers: 1", "Budget Left: 2500.00"])

        self.assertEqual(expected, single_traveler.booking_status())

    def test_one_trip_booked_family(self):
        family = Trip(30000.0, 2, True)
        destination = 'New Zealand'
        paid_amount = (7500 * 2) * 0.9
        family.book_a_trip(destination)
        expected = "\n".join(["Booked Destination: New Zealand", f"Paid Amount: {paid_amount:.2f}",
                              "Number of Travelers: 2", f"Budget Left: {30000 - paid_amount:.2f}"])

        self.assertEqual(expected, family.booking_status())


if __name__ == "__main__":
    main()
