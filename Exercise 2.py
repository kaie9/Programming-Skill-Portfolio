import random

#function to load jokes from file
def loadJokes(filename):
    with open(filename, 'r') as file:
        jokes = file.readlines()
    return [joke.strip().split('?') for joke in jokes if '?' in joke]

#funstion to tell a random joke
def tellJoke(jokes):
    setup, punchline = random.choice(jokes)
    print("\n" + setup + "?")
    input("Press Enter to hear the punchline...")
    print(punchline + "\n")

#the function to handle user interaction
def jokeProgram():
    jokes = loadJokes("C:\\Users\\batac\\Advanced Programming\\randomJokes.txt")
    
    print("Welcome! Ask me to tell you a joke by typing 'Alexa tell me a joke'.")
    while True:
        user_input = input("You: ").strip().lower()
        if user_input == "alexa tell me a joke":
            tellJoke(jokes)
        elif user_input in ["quit", "exit"]:
            print("Goodbye! Hope you enjoyed the jokes!")
            break
        else:
            print("Try saying 'Alexa tell me a joke' or type 'quit' to exit.")

#start the joke code
jokeProgram()
