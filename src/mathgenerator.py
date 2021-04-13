from random import randint, choice

class MathGenerator():
    def gen_task(self):
        value1 = randint(1,20)
        value2 = randint(1,20)
        operation = choice(["+", "-", "*"])

        taskstr = str(f"{value1} {operation} {value2}")

        if operation == "+":
            answer = value1 + value2
        elif operation == "-":
            answer = value1 - value2
        elif operation == "*":
            answer = value1 * value2

        return (taskstr, answer)

    def enteranswer(self):
        answer = int(input("Syötä vastaus: "))
        return answer

    def checkanswer(self, answer1: int, answer2: int):
        if answer1 == answer2:
            return True
        elif answer1 != answer2:
            return False

if __name__ == "__main__":
    generator = MathGenerator()
    task = generator.gen_task()
    correctans = task[1]
    print(task[0])
    useranswer = MathGenerator().enteranswer()
    if generator.checkanswer(correctans, useranswer) == True:
        print("Oikein!")
    else:
        print("Väärin!")
    
