import unittest
from password_validator import validate_password


class TestValidatePassword(unittest.TestCase):

    def test_valid_password(self):
        self.assertTrue(validate_password("Abcdef1!"))

    def test_password_with_exactly_8_characters(self):
        self.assertEqual(len("Abcdef1!"), 8)
        self.assertTrue(validate_password("Abcdef1!"))

    def test_password_with_exactly_20_characters(self):
        password = "Abcdefghijklmnopqr1!"
        self.assertEqual(len(password), 20)
        self.assertTrue(validate_password(password))

    def test_non_string_input(self):
        self.assertFalse(validate_password(None))
        self.assertFalse(validate_password(12345678))
        self.assertFalse(validate_password(["Abcdef1!"]))

    def test_password_too_short(self):
        self.assertFalse(validate_password("Abcde1!"))

    def test_password_too_long(self):
        self.assertFalse(validate_password("Abcdefghijklmnopqrs1!"))

    def test_password_without_uppercase(self):
        self.assertFalse(validate_password("abcdef1!"))

    def test_password_without_lowercase(self):
        self.assertFalse(validate_password("ABCDEF1!"))

    def test_password_without_digit(self):
        self.assertFalse(validate_password("Abcdefg!"))

    def test_password_without_special_character(self):
        self.assertFalse(validate_password("Abcdefg1"))

    def test_password_with_space(self):
        self.assertFalse(validate_password("Abc def1!"))

    def test_password_with_tab(self):
        self.assertFalse(validate_password("Abcdef\t1!"))

    def test_password_with_newline(self):
        self.assertFalse(validate_password("Abcdef\n1!"))


if __name__ == "__main__":
    unittest.main()