class Flashcard:
    def __init__(self,word,meaning):
        self.word=word
        self.meaning=meaning
    
    def __str__(self):
        return self.word+'('+self.meaning+')'
print("Welcome to the Flashcard program!")

flash=[]

while True:
    word=input("Enter the word:")
    meaning=input("Enter the meaning:")
    flash.append(Flashcard(word,meaning))

    continue_playing=input("Enter 0 to enter another word or 1 to quit:")

    if(continue_playing):
        break
    
print("Your Flashcards:")
for i in (flash):
    print(">",i)
    


