from entities.user import User

from repositories.user_repository import (user_repository as default_user_repository)

class MathService:

    def __init__(self, user_repository=default_user_repository):

        self._user = None
        self._user_repository = user_repository

    def create_user(self, username, password, login=True):

        user = self._user_repository.create(User(username, password))

        if login:
            self._user = user

        return user

    def login(self, username, password):

        user = self._user_repository.find_by_username(username)

        self._user = user

        return user

    def logout(self):

        self._user = None
