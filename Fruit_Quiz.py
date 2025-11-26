import random

class Fruit_Quiz:
    def __init__(self):
        self.fruits={"apple":"red",
                     "banana":"yellow",
                     "orange":"yellow",
                     "kiwi":"green"}
    def quiz(Self):
        while True:
            fruit,colour=random.choice(list(Self.fruits.items()))
            print(f"What is the color of {fruit}?")
            user_answer = input("Your answer: ")

            if user_answer.lower() == colour:
                print("Correct answer")
            else:
                print("Wrong answer")

            option = int(input("Enter 0 if you want to play again, otherwise enter 1: "))
            if option:
                break


print("Welcome to Fruit Quiz")
fq = Fruit_Quiz()
fq.quiz()
        
