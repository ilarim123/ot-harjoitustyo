import unittest
from mathgenerator import MathGenerator

class TestMathgenerator(unittest.TestCase):
    def setUp(self):
	    self.generator = MathGenerator()

    def test_recognises_correct_answer(self):
        self.task = self.generator.gen_task()
        self.answer  = self.task[1]
        self.useranswer = self.task[1]
        self.check = self.generator.checkanswer(self.answer, self.useranswer)
        self.assertEqual(self.check, True)


