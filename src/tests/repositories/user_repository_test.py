import unittest
from repositories.user_repository import user_repository


class TestUserRepository(unittest.TestCase):
    def setUp(self):
        self.testusername = "Tester"
        self.testpassword = "abc123"
        user_repository.create_user(self.testusername, self.testpassword)
    
    def test_does_user_exist(self):
        value = user_repository.does_user_exist(self.testusername)

        self.assertEqual(value, True)
    
    def test_create_user(self):
        user_repository.create_user("Tester2", "xyz321")
        value = user_repository.does_user_exist("Tester2")

        self.assertEqual(value, True)
    
    def test_check_password(self):
        value = user_repository.check_password(self.testusername, self.testpassword)

        self.assertEqual(value, True)

    def test_check_completion(self):
        user_repository.mark_as_completed(self.testusername, "add")
        value = user_repository.check_completion(self.testusername, "add")

        self.assertEqual(value, True)
    
    def test_mark_as_completed(self):
        user_repository.mark_as_completed(self.testusername, "sub")
        value = user_repository.check_completion(self.testusername, "sub")

        self.assertEqual(value, True)
