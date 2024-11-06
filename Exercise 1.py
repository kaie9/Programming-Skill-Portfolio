import random

#displays difficulty menu and get user's choice
def displayMenu():
    print("DIFFICULTY LEVEL")
    print("1. Easy")
    print("2. Moderate")
    print("3. Advanced")
    while True:
        try:
            choice = int(input("Choose a difficulty level (1-3): "))
            if choice in [1, 2, 3]:
                return choice
            else:
                print("Please enter a number between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

#generates random integer based on difficulty level
def randomInt(difficulty):
    if difficulty == 1:       
        return random.randint(1, 9)
    elif difficulty == 2:     
        return random.randint(10, 99)
    elif difficulty == 3:     
        return random.randint(1000, 9999)

#function to randomly decide addition or subtraction
def decideOperation():
    return random.choice(['+', '-'])

#displays the problem and get user's answer
def displayProblem(num1, num2, operation):
    problem = f"{num1} {operation} {num2} = "
    try:
        return int(input(problem))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return displayProblem(num1, num2, operation)

#checks if the answer is correct and prints the message
def isCorrect(user_answer, correct_answer):
    if user_answer == correct_answer:
        print("Correct!")
        return True
    else:
        print("Incorrect. Try again.")
        return False

#displays the final results
def displayResults(score):
    print(f"Your final score is: {score}/100")
    if score > 90:
        print("Rank: A+")
    elif score > 80:
        print("Rank: A")
    elif score > 70:
        print("Rank: B")
    elif score > 60:
        print("Rank: C")
    else:
        print("Rank: F")

#the function to handle quiz logic
def mathQuiz():
    while True:
        difficulty = displayMenu()
        score = 0

        for _ in range(10):
            num1 = randomInt(difficulty)
            num2 = randomInt(difficulty)
            operation = decideOperation()
            correct_answer = num1 + num2 if operation == '+' else num1 - num2

            
            user_answer = displayProblem(num1, num2, operation)
            if isCorrect(user_answer, correct_answer):
                score += 10
            else:
                
                user_answer = displayProblem(num1, num2, operation)
                if isCorrect(user_answer, correct_answer):
                    score += 5

        displayResults(score)

        #asks if the user wants to play again
        play_again = input("Would you like to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

#starts the quiz
mathQuiz()
