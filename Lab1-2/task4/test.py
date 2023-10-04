import unittest
from task4 import create_html

class ProgramTestCaseGenerate(unittest.TestCase):
    def test_generate_html_with_n_3(self):
        n = 3
        result = create_html(n)
        expected_html = "<!DOCTYPE html>\n<html>\n<body>\n<table cellspacing=\"0\" cellpadding=\"0\" style=\"width: 700px;\">\n<tr style=\"height: 10px; border: none; background-color: rgb(255, 255, 255)\"><td></td></tr>\n<tr style=\"height: 10px; border: none; background-color: rgb(170, 170, 170)\"><td></td></tr>\n<tr style=\"height: 10px; border: none; background-color: rgb(85, 85, 85)\"><td></td></tr>\n</table>\n</body>\n</html>"
        self.assertEqual(result, expected_html)

    def test_generate_html_with_n_5(self):
        n = 5
        result = create_html(n)
        expected_html = "<!DOCTYPE html>\n<html>\n<body>\n<table cellspacing=\"0\" cellpadding=\"0\" style=\"width: 700px;\">\n<tr style=\"height: 10px; border: none; background-color: rgb(255, 255, 255)\"><td></td></tr>\n<tr style=\"height: 10px; border: none; background-color: rgb(204, 204, 204)\"><td></td></tr>\n<tr style=\"height: 10px; border: none; background-color: rgb(153, 153, 153)\"><td></td></tr>\n<tr style=\"height: 10px; border: none; background-color: rgb(102, 102, 102)\"><td></td></tr>\n<tr style=\"height: 10px; border: none; background-color: rgb(51, 51, 51)\"><td></td></tr>\n</table>\n</body>\n</html>"
        self.assertEqual(result, expected_html)

if __name__ == "__main__":
    unittest.main()