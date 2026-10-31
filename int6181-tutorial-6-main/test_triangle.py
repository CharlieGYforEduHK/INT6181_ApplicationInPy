import unittest

from triangle import Triangle, TriangleType


class TestTriangle(unittest.TestCase):

    def test_valid_triangle(self):
        triangle = Triangle(3, 4, 5)

        self.assertTrue(triangle.is_valid())

    def test_non_numeric_sides_are_invalid(self):
        invalid_inputs = [
            ("3", 4, 5),
            (3, "4", 5),
            (3, 4, "5"),
            (None, 4, 5),
            (3, None, 5),
            (3, 4, None),
        ]

        for sides in invalid_inputs:
            with self.subTest(sides=sides):
                triangle = Triangle(*sides)
                self.assertFalse(triangle.is_valid())

    def test_boolean_sides_are_invalid(self):
        invalid_inputs = [
            (True, 4, 5),
            (3, False, 5),
            (3, 4, True),
        ]

        for sides in invalid_inputs:
            with self.subTest(sides=sides):
                triangle = Triangle(*sides)
                self.assertFalse(triangle.is_valid())

    def test_zero_side_is_invalid(self):
        triangle = Triangle(0, 4, 5)

        self.assertFalse(triangle.is_valid())

    def test_negative_side_is_invalid(self):
        triangle = Triangle(-3, 4, 5)

        self.assertFalse(triangle.is_valid())

    def test_triangle_inequality_is_required(self):
        invalid_triangles = [
            (1, 2, 3),
            (2, 3, 5),
            (3, 5, 2),
        ]

        for sides in invalid_triangles:
            with self.subTest(sides=sides):
                triangle = Triangle(*sides)
                self.assertFalse(triangle.is_valid())

    def test_equilateral_triangle_type(self):
        triangle = Triangle(3, 3, 3)

        self.assertEqual(
            triangle.get_type(),
            TriangleType.EQUILATERAL
        )

    def test_isosceles_triangle_type(self):
        triangle = Triangle(5, 5, 6)

        self.assertEqual(
            triangle.get_type(),
            TriangleType.ISOSCELES
        )

    def test_scalene_triangle_type(self):
        triangle = Triangle(3, 4, 5)

        self.assertEqual(
            triangle.get_type(),
            TriangleType.SCALENE
        )

    def test_invalid_triangle_type_is_none(self):
        triangle = Triangle(1, 2, 3)

        self.assertIsNone(triangle.get_type())

    def test_equilateral_triangle_area(self):
        triangle = Triangle(3, 3, 3)

        self.assertEqual(triangle.get_area(), 3.8971)

    def test_isosceles_triangle_area(self):
        triangle = Triangle(5, 5, 6)

        self.assertEqual(triangle.get_area(), 12.0)

    def test_scalene_triangle_area(self):
        triangle = Triangle(3, 4, 5)

        self.assertEqual(triangle.get_area(), 6.0)

    def test_invalid_triangle_area_is_none(self):
        triangle = Triangle(1, 2, 3)

        self.assertIsNone(triangle.get_area())


if __name__ == "__main__":
    unittest.main()