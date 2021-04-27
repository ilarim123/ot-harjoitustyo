from random import randint

from repositories.user_repository import (user_repository as default_user_repository)

class MathGenerator():
    def __init__(self, user_repository=default_user_repository):
        self._user_repository = user_repository
        self.loggedin = False

    def gen_addition_task(self):
        value1 = randint(10, 150)
        value2 = randint(10, 150)

        taskstr = str(f"{value1} + {value2}")
        answer = value1 + value2

        return (taskstr, answer)

    def gen_substraction_task(self):
        value1 = randint(10, 150)
        value2 = randint(10, 150)

        taskstr = str(f"{value1} - {value2}")
        answer = value1 - value2

        return (taskstr, answer)

    def gen_multiplication_task(self):
        value1 = randint(2, 20)
        value2 = randint(2, 20)

        taskstr = str(f"{value1} * {value2}")
        answer = value1*value2

        return (taskstr, answer)

    def enter_answer(self):
        answer = int(input("Syötä vastaus: "))
        return answer

    def check_answer(self, answer1: int, answer2: int):
        if answer1 == answer2:
            return True
        elif answer1 != answer2:
            return False

    def task_set(self, type: str):
        remaining = 5
        score = 0
        while remaining > 0:
            if type == "+":
                task = self.gen_addition_task()
            elif type == "-":
                task = self.gen_substraction_task()
            elif type == "*":
                task = self.gen_multiplication_task()
            print(task[0])
            useranswer = self.enter_answer()
            correct = self.check_answer(useranswer, task[1])
            if correct == True:
                print("Oikein!")
                score += 1
            else:
                print("Väärin!")
            remaining -= 1
        print(f"Oikeiden vastausten määrä: {score}")

    def select_action(self):
        action = int(input("Syötä toiminnon numero: "))
        if action == 1:
            if self.loggedin == False:
                self.enter_login_credentials()
            else:
                self.logout()
        elif action == 2:
            self.create_new_user()
        elif action == 3:
            self.task_set("+")
        elif action == 4:
            self.task_set("-")
        elif action == 5:
            self.task_set("*")
        elif action == 6:
            return "close"
        else:
            print("Syöttämäsi luku on virheellinen")


    def add_user_to_file(self, username, password):
        self._user_repository.create_user(username, password)

    def create_new_user(self):
        username = input("Syötä haluamasi käyttäjänimi: ")
        doesexist = self._user_repository.does_user_exist(username)
        if doesexist == True:
            raise Exception("Haluamasi käyttäjänimi on varattu")
        password = input("Syötä haluamasi salasana: ")
        self.add_user_to_file(username, password)

    def login(self, username, password):
        try:
            iscorrect = self._user_repository.check_password(username, password)
            return iscorrect
        except:
            pass

    def enter_login_credentials(self):
        username = input("Käyttäjänimi: ")
        password = input("Salasana: ")
        login = self.login(username, password)
        if login == True:
            self.loggedin = True
        else:
            print("Salasana on virheellinen tai käyttäjää ei ole")

    def print_actions(self):
        print("-------------------------------------")
        print("Matematiikan tehtäväsovellus")
        print("-------------------------------------")
        if self.loggedin == True:
            print(f"Olet kirjautunut sisään")
        else:
            print("Et ole kirjautunut sisään")
        print("Toiminnot:")
        if self.loggedin == False:
            print("1: Kirjaudu sisään")
        else:
            print("1: Kirjaudu ulos")
        print("2: Luo uusi käyttäjä")
        print("3: Yhteenlaskut")
        print("4: Erotukset")
        print("5: Kertolaskut")
        print("6: Sulje")

    def logout(self):
        self.loggedin = False


if __name__ == "__main__":
    Generator = MathGenerator()

    while True:
        Generator.print_actions()
        action = Generator.select_action()
        if action == "close":
            break



