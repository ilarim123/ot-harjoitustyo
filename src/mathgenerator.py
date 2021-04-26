from random import randint

class MathGenerator():

    def gen_addition_task(self):
        value1 = randint(10,150)
        value2 = randint(10,150)

        taskstr = str(f"{value1} + {value2}")
        answer = value1 + value2

        return (taskstr, answer)

    def gen_substraction_task(self):
        value1 = randint(10,150)
        value2 = randint(10,150)

        taskstr = str(f"{value1} - {value2}")
        answer = value1 - value2

        return (taskstr, answer)

    def gen_multiplication_task(self):
        value1 = randint(2,20)
        value2 = randint(2,20)

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
        try:
            action = int(input("Syötä toiminnon numero: "))
            if action == 1:
                self.task_set("+")
            elif action == 2:
                self.task_set("-")
            elif action == 3:
                self.task_set("*")
            elif action == 4:
                return True
            else:
                print("Syöttämäsi luku on virheellinen")
        except:
            print("Syöttämäsi luku on virheellinen")


    def show_actions(self):
        print("-------------------------------------")
        print("Matematiikan tehtäväsovellus")
        print("-------------------------------------")
        print("Toiminnot:")
        print("1: Yhteenlaskut")
        print("2: Erotukset")
        print("3: Kertolaskut")
        print("4: Sulje")


if __name__ == "__main__":
    generator = MathGenerator()

    while True:
        generator.show_actions()
        action = generator.select_action()
        if action == True:
            break



