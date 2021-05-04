from random import randint

from repositories.user_repository import (user_repository as default_user_repository)

class MathGenerator():
    """Luokka, jolla tehtäviä luodaan ja niihin vastataan.

    Attributes:
        _user_repository: Luokka jolla käsitellään käyttäjiä.
        loggedin: Kertoo onko kukaan kirjautunut sisään.
        loggeduser: Kertoo kuka on kirjautunut sisään.
    """

    def __init__(self, user_repository=default_user_repository):
        """Luokan konstruktori, joka alustaa generaattorin.

        Args:
            user_repository: Luokka jolla käsitellään käyttäjiä.
        """

        self._user_repository = user_repository
        self.loggedin = False
        self.loggeduser = None

    def gen_addition_task(self):
        """Luo uuden yhteenlaskutehtävän.

        Returns:
            Tuple, jossa on ratkaistava tehtävä merkkijonona sekä tehtävän vastaus lukuna.
        """

        value1 = randint(10, 150)
        value2 = randint(10, 150)

        taskstr = str(f"{value1} + {value2}")
        answer = value1 + value2

        return (taskstr, answer)

    def gen_substraction_task(self):
        """Luo uuden erotustehtävän.

        Returns:
            Tuple, jossa on ratkaistava tehtävä merkkijonona sekä tehtävän vastaus lukuna.
        """

        value1 = randint(10, 150)
        value2 = randint(10, 150)

        taskstr = str(f"{value1} - {value2}")
        answer = value1 - value2

        return (taskstr, answer)

    def gen_multiplication_task(self):
        """Luo uuden kertolaskutehtävän.

        Returns:
            Tuple, jossa on ratkaistava tehtävä merkkijonona sekä tehtävän vastaus lukuna.
        """

        value1 = randint(2, 20)
        value2 = randint(2, 20)

        taskstr = str(f"{value1} * {value2}")
        answer = value1*value2

        return (taskstr, answer)

    def enter_answer(self):
        """Mahdollistaa käyttäjää syöttämään vastauksen.

        Returns:
            Käyttäjän syöttämä kokonaisluku.
        """

        answer = int(input("Syötä vastaus: "))
        return answer

    def check_answer(self, answer1: int, answer2: int):
        """Tarkistaa onko käyttäjän syöttämä luku oikea vastaus.

        Args:
            answer1: Käyttäjän vastaus kokonaislukuna.
            answer2: Oikea vastaus kokonaislukuna.

        Returns:
            True jos käyttäjän vastaus ja oikea vastaus ovat yhtäsuuret, muuten False.
        """

        if answer1 == answer2:
            return True

        return False

    def task_set(self, type: str):
        """Luo halutun tyyppisen tehtäväsarjan jossa on viisi tehtävää.

        Args:
            type: Tehtäväsarjan tyyppi:
            yhteenlasku on "add", erotus "sub" ja kertolasku "multi"
        """

        remaining = 5
        score = 0
        while remaining > 0:
            if type == 'add':
                task = self.gen_addition_task()
            elif type == 'sub':
                task = self.gen_substraction_task()
            elif type == 'multi':
                task = self.gen_multiplication_task()
            print(task[0])
            useranswer = self.enter_answer()
            correct = self.check_answer(useranswer, task[1])
            if correct:
                print("Oikein!")
                score += 1
            else:
                print("Väärin!")
            remaining -= 1
        print(f"Oikeiden vastausten määrä: {score}")
        if score == 5:
            self._user_repository.mark_as_completed(self.loggeduser, type)


    def select_action(self):
        """Mahdollistaa halutun toiminnon valitsemisen valikossa

        Returns:
            "close", mikäli haluttu toiminto on 0 eli ohjelman sulkeminen
        """

        action = int(input("Syötä toiminnon numero: "))
        if action == 1:
            if not self.loggedin:
                self.enter_login_credentials()
            else:
                self.logout()
        elif action == 2:
            self.create_new_user()
        elif action == 3:
            if self.loggedin:
                self.task_set('add')
            else:
                print("Syöttämäsi luku on virheellinen")
        elif action == 4:
            if self.loggedin:
                self.task_set('sub')
            else:
                print("Syöttämäsi luku on virheellinen")
        elif action == 5:
            if self.loggedin:
                self.task_set('multi')
            else:
                print("Syöttämäsi luku on virheellinen")
        elif action == 0:
            return "close"
        else:
            print("Syöttämäsi luku on virheellinen")


    def add_user_to_file(self, username, password):
        """Lisää luodun käyttäjän .csv-tiedostoon

        Args:
            username: Käyttäjän käyttäjänimi
            password: Käyttäjän salasana
        """

        self._user_repository.create_user(username, password)

    def create_new_user(self):
        """Pyytää käyttäjältä nimeä ja salasanaa ja luo näillä uuden käyttäjän.

        """

        username = input("Syötä haluamasi käyttäjänimi: ")
        doesexist = self._user_repository.does_user_exist(username)
        if doesexist:
            print("Haluamasi käyttäjänimi on varattu")
        else:
            password = input("Syötä haluamasi salasana: ")
            self.add_user_to_file(username, password)
            self.loggedin = True
            self.loggeduser = str(username)

    def login(self, username, password):
        """Tarkistaa täsmääkö annettu salasana käyttäjään.

        Jos käyttäjää ei ole olemassa niin metodi ei tee mitään.

        Args:
            username: Käyttäjänimi
            password: Salasana

        Returns:
            Totuusarvo iscorrect, jos käyttäjä on olemassa.
            Salasanan ollessa oikein arvo on True, muutoin False.
        """

        try:
            iscorrect = self._user_repository.check_password(username, password)
            return iscorrect
        except:
            pass

    def enter_login_credentials(self):
        """Mahdollistaa käyttäjänimen ja salasanan syöttämisen.

        """

        username = input("Käyttäjänimi: ")
        password = input("Salasana: ")
        login = self.login(username, password)
        if login:
            self.loggedin = True
            self.loggeduser = str(username)
        else:
            print("Salasana on virheellinen tai käyttäjää ei ole")

    def print_actions(self):
        """Tulostaa valikon jossa kerrotaan eri toiminnot

        """

        print("-------------------------------------")
        print("Matematiikan tehtäväsovellus")
        print("-------------------------------------")

        if self.loggedin:
            print(f"Olet kirjautunut sisään käyttäjänä {self.loggeduser}")
        else:
            print("Et ole kirjautunut sisään")

        print("Toiminnot:")

        if not self.loggedin:
            print("1: Kirjaudu sisään")
        else:
            print("1: Kirjaudu ulos")

        print("2: Luo uusi käyttäjä")

        if self.loggedin:
            if self._user_repository.check_completion(self.loggeduser, 'add'):
                print("3: Yhteenlaskut - Suoritettu!")
            else:
                print("3: Yhteenlaskut - Ei suoritettu")

            if self._user_repository.check_completion(self.loggeduser, 'sub'):
                print("4: Erotukset - Suoritettu!")
            else:
                print("4: Erotukset - Ei suoritettu")

            if self._user_repository.check_completion(self.loggeduser, 'multi'):
                print("5: Kertolaskut - Suoritettu!")
            else:
                print("5: Kertolaskut - Ei suoritettu")

        print("0: Sulje")

    def logout(self):
        """Kirjaa käyttäjän ulos vaihtamalla self.loggedin:in arvoksi False

        """

        self.loggedin = False


if __name__ == "__main__":
    Generator = MathGenerator()

    while True:
        Generator.print_actions()
        try:
            SELECT = Generator.select_action()
        except:
            print("Syöttämäsi luku on virheellinen")
            SELECT = None
        if SELECT == "close":
            break



