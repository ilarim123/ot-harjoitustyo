import unittest
from mathgenerator import MathGenerator

class TestMathgenerator(unittest.TestCase):
    def setUp(self):
	    self.generator = MathGenerator()

    def test_recognises_correct_answer(self):
        self.task = self.generator.gen_addition_task()
        self.answer  = self.task[1]
        self.useranswer = self.task[1]
        self.check = self.generator.check_answer(self.answer, self.useranswer)
        self.assertEqual(self.check, True)

    def test_addition_task_returns_correct_answer(self):
        self.list = []
        self.task = self.generator.gen_addition_task()
        self.returnedanswer = self.task[1]

        for character in self.task[0]:
            if character == " " or character == "+":
                if len(self.list) != 0:
                    self.first = int("".join(self.list))
                    self.list = []
                else:
                    continue
            else:
                self.list.append(character)
        self.second = int("".join(self.list))
        self.correctanswer = self.first + self.second
        self.assertEqual(self.returnedanswer, self.correctanswer)

    def test_substraction_task_returns_correct_answer(self):
        self.list = []
        self.task = self.generator.gen_substraction_task()
        self.returnedanswer = self.task[1]

        for character in self.task[0]:
            if character == " " or character == "-":
                if len(self.list) != 0:
                    self.first = int("".join(self.list))
                    self.list = []
                else:
                    continue
            else:
                self.list.append(character)
        self.second = int("".join(self.list))
        self.correctanswer = self.first - self.second
        self.assertEqual(self.returnedanswer, self.correctanswer)

    def test_multiplication_task_returns_correct_answer(self):
        self.list = []
        self.task = self.generator.gen_multiplication_task()
        self.returnedanswer = self.task[1]

        for character in self.task[0]:
            if character == " " or character == "*":
                if len(self.list) != 0:
                    self.first = int("".join(self.list))
                    self.list = []
                else:
                    continue
            else:
                self.list.append(character)
        self.second = int("".join(self.list))
        self.correctanswer = self.first * self.second
        self.assertEqual(self.returnedanswer, self.correctanswer)
