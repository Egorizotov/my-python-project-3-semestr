import unittest

from Egor_izotov_sem3.РК2.main import RequestOne, RequestTwo, RequestThree, get_sample_data, ProgrammingLanguage, \
    Operator, OperatorLanguage
import unittest

# Ваши классы и функции тут

class TestOperatorFunctions(unittest.TestCase):
    def setUp(self):
        # Здесь создаем все данные, как раньше
        self.languages = [
            ProgrammingLanguage(1, "Go"),
            ProgrammingLanguage(2, "Rust"),
            ProgrammingLanguage(3, "Java")
        ]
        self.operators = [
            Operator(1, "break", 5, 1),
            Operator(2, "borrow", 6, 2),
            Operator(3, "object", 6, 3),
            Operator(4, "guard", 5, 2)
        ]
        self.operators_languages = [
            OperatorLanguage(1, 1, 1),
            OperatorLanguage(2, 2, 2),
            OperatorLanguage(3, 3, 3),
            OperatorLanguage(4, 4, 2),
            OperatorLanguage(5, 3, 2)
        ]

    def test_request_one(self):
        result = RequestOne(self.operators, self.languages)
        expected = [("break", "Go"), ("borrow", "Rust")]
        self.assertEqual(result, expected)

    def test_request_two(self):
        result = RequestTwo(self.operators)
        expected = [5, 5, 6, 6]
        self.assertEqual(result, expected)

    def test_request_three(self):
        result = RequestThree(self.operators, self.languages, self.operators_languages)
        expected = [
            (1, "break", "Go"),
            (2, "borrow", "Rust"),
            (3, "object", "Java"),
            (3, "object", "Rust"),
            (4, "guard", "Rust")
        ]
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()

