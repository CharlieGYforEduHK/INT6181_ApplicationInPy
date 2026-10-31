import unittest

from parking_fee import ParkingFeeCalculator


class TestParkingFeeCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = ParkingFeeCalculator()

    def test_one_hour_is_free(self):
        self.assertEqual(
            self.calculator.calculate_fee(1),
            0.00
        )

    def test_less_than_one_hour_is_free(self):
        self.assertEqual(
            self.calculator.calculate_fee(0.5),
            0.00
        )

    def test_partial_hour_is_rounded_up(self):
        self.assertEqual(
            self.calculator.calculate_fee(1.5),
            10.00
        )

    def test_two_hours_cost_ten_dollars(self):
        self.assertEqual(
            self.calculator.calculate_fee(2),
            10.00
        )

    def test_nine_hours_reach_daily_cap(self):
        self.assertEqual(
            self.calculator.calculate_fee(9),
            80.00
        )

    def test_twenty_four_hours_cost_daily_cap(self):
        self.assertEqual(
            self.calculator.calculate_fee(24),
            80.00
        )

    def test_twenty_five_hours(self):
        self.assertEqual(
            self.calculator.calculate_fee(25),
            80.00
        )

    def test_twenty_six_hours(self):
        self.assertEqual(
            self.calculator.calculate_fee(26),
            90.00
        )

    def test_multiple_full_days(self):
        self.assertEqual(
            self.calculator.calculate_fee(48),
            160.00
        )

    def test_multiple_days_with_remaining_hours(self):
        self.assertEqual(
            self.calculator.calculate_fee(50),
            170.00
        )

    def test_invalid_non_numeric_inputs(self):
        invalid_values = [
            None,
            "2",
            [],
            {},
            object(),
        ]

        for value in invalid_values:
            with self.subTest(value=value):
                self.assertIsNone(
                    self.calculator.calculate_fee(value)
                )

    def test_boolean_inputs_are_invalid(self):
        self.assertIsNone(
            self.calculator.calculate_fee(True)
        )
        self.assertIsNone(
            self.calculator.calculate_fee(False)
        )

    def test_zero_hours_are_invalid(self):
        self.assertIsNone(
            self.calculator.calculate_fee(0)
        )

    def test_negative_hours_are_invalid(self):
        self.assertIsNone(
            self.calculator.calculate_fee(-1)
        )
        self.assertIsNone(
            self.calculator.calculate_fee(-0.5)
        )

    def test_fee_is_rounded_to_two_decimal_places(self):
        fee = self.calculator.calculate_fee(2.01)

        self.assertEqual(fee, 20.00)
        self.assertEqual(round(fee, 2), fee)


if __name__ == "__main__":
    unittest.main()