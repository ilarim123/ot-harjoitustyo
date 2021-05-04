import unittest
from mathgenerator import MathGenerator
from repositories.user_repository import user_repository

class TestMathgenerator(unittest.TestCase):
    def setUp(self):
        self.generator = MathGenerator()

    def test_check_answer(self):
        task = self.generator.gen_addition_task()
        correctanswer  = task[1]
        useranswer = task[1]
        wronganswer = task[1] - 1
        check1 = self.generator.check_answer(correctanswer, useranswer)
        self.assertEqual(check1, True)
        check2 = self.generator.check_answer(wronganswer, useranswer)
        self.assertEqual(check2, False)

    def test_gen_addition_task(self):
        testlist = []
        task = self.generator.gen_addition_task()
        returnedanswer = task[1]

        for character in task[0]:
            if character == " " or character == "+":
                if len(testlist) != 0:
                    first = int("".join(testlist))
                    testlist = []
                else:
                    continue
            else:
                testlist.append(character)
        second = int("".join(testlist))
        correctanswer = first + second
        self.assertEqual(returnedanswer, correctanswer)

    def test_gen_substraction_task(self):
        testlist = []
        task = self.generator.gen_substraction_task()
        returnedanswer = task[1]

        for character in task[0]:
            if character == " " or character == "-":
                if len(testlist) != 0:
                    first = int("".join(testlist))
                    testlist = []
                else:
                    continue
            else:
                testlist.append(character)
        second = int("".join(testlist))
        correctanswer = first - second
        self.assertEqual(returnedanswer, correctanswer)

    def test_gen_multiplication_task(self):
        testlist = []
        task = self.generator.gen_multiplication_task()
        returnedanswer = task[1]

        for character in task[0]:
            if character == " " or character == "*":
                if len(testlist) != 0:
                    first = int("".join(testlist))
                    testlist = []
                else:
                    continue
            else:
                testlist.append(character)
        second = int("".join(testlist))
        correctanswer = first * second
        self.assertEqual(returnedanswer, correctanswer)
    
    def test_add_user_to_file(self):
        testuser = "user1"
        testpassword = "pswrd1"
        self.generator.add_user_to_file(testuser, testpassword)
        value = self.generator._user_repository.does_user_exist(testuser)

        self.assertEqual(value, True)

    def test_login(self):
        self.generator.add_user_to_file("user2", "password2")
        correct = self.generator.login("user2", "password2")
        doesntexist = self.generator.login("nouser", "nopass")

        self.assertEqual(correct, True)
        self.assertEqual(doesntexist, None)

    def test_logout(self):
        self.generator.loggedin = True
        self.generator.logout()

        self.assertEqual(self.generator.loggedin, False)
