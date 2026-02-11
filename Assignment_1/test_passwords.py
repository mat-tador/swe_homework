import unittest
from passwords import password_strength

class PasswordStrengthTest(unittest.TestCase):
     
    def test_empty_is_weak(self):
        self.assertEqual(password_strength(""), "weak")
    
    def test_letters_only(self):
        password = "hello"
        self.assertEqual(password_strength(password), "weak")

    def test_digits_letters_medium(self):
        password = "abc12345"
        self.assertEqual(password_strength(password), "medium")

    def test_digits_letters_symbols_strong(self):
        password = "abc12345!!xx"
        self.assertEqual(password_strength(password), "strong")

    def test_small_symbols(self): 
        password = "!@#$%^&*()"
        self.assertEqual(password_strength(password), "weak")

    def test_non_string_input(self):
        password = 123
        self.assertRaises(TypeError, password_strength, password)


if __name__ == "__main__":
    unittest.main()
