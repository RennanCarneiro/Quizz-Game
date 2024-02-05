def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1
    
    for key in questions : #loop to display the questions
        print()
        print(key)
        for i in options [question_num-1]: #nested loop to associate only the answers to the right questions
            print (i)
        guess = input("Enter (A, B, C, D) :")
        guess = guess.upper() #case sensitivity to avoid any problems with the user answer. Upper because i capitalized the answers.
        guesses.append(guess)
        
        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1
        
    display_score(correct_guesses, guesses)
        
def check_answer(answer, guess):
    if answer == guess:
        print ("Correct!")
        return 1
    else:
        print("Wrong!")
        return 0

def display_score(correct_guesses, guesses):
    print()
    print("RESULTS BELOW")
    print()
    print("Answers: ", end=" ") #end="" will make it not go to the next line
    for i in questions:
        print(questions.get(i), end=" ")
    print()
    print("Guesses: ", end="") #end="" will make it not go to the next line
    for i in guesses:
        print(i, end=" ")
    print()
    
    score = int((correct_guesses/len(questions))) * 100
    print(f"Your Score is: " + str(score) + "%")

def play_again():
    
    response = input("Do you want to try again? (Yes or No)")
    response = response.upper()
    
    if response == "YES":
        return True
    else:
        return False

questions = {
    "What was the first feature-length animated movie ever released?" : "B", #Snow white and the sever dwarfs
    "In The Matrix, does Neo take the blue pill or the red pill?" : "A", #red pill
    "What was the top-grossing movie of 2014?" : "D", #Guardians of the Galaxy
    "Which movie has the phrase if you are a bird, I am a bird?" : "C" #The Notebook
}
#2d list/tuple list for the answers. 
# questions line : answers line (qeustion 1 : answer line 1)
options = [["A. 101 Dalmatas", "B. Snow white and the seven dwarfs", "C. Pinocchio", "D. Cinderela"],
           ["A. Red pill", "B. Black pill", "C. Blue pill", "D. Yellow pill"],
           ["A. Transformers 4", "B. Nightcrawler", "C. Godzilla", "D. Guardians of the Galaxy"],
           ["A. La La Land", "B. Grease", "C. The Notebook", "D. Titanic"]]

new_game()

while play_again():
    new_game()
    
print("Bye!")