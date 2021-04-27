from pathlib import Path
from config import USERS_FILE_PATH

class UserRepository:
    def __init__(self, file_path):
        self._file_path = file_path

    def _ensure_file_exists(self):
        Path(self._file_path).touch()

    def does_user_exist(self, username):
        self._ensure_file_exists()

        with open(self._file_path) as file:
            for row in file:
                row = row.replace('\n', '')
                parts = row.split(';')

                user = parts[0]

                if user == username:
                    return True

            return False

    def create_user(self, username, password):
        self._ensure_file_exists()

        with open(self._file_path, 'a') as file:
            row = f'{username};{password}'

            file.write(row+'\n')

    def check_password(self, username, password):
        with open(self._file_path) as file:
            for row in file:
                row = row.replace('\n', '')
                parts = row.split(';')

                user = parts[0]

                if user == username:
                    correctpassword = parts[1]
                    if password == correctpassword:
                        return True

                    return False



user_repository = UserRepository(USERS_FILE_PATH)
