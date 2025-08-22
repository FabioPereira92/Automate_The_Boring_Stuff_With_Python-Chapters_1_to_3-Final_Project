# Function to take guesses, validate if its right or not and give hints
def takeAGuess():
    global lives
    i = 0
    while lives != 0:

        # Hint
        if i == 3 and number % 2 == 0:
            print('Hint: The number is even!')
        elif i == 3 and number % 2 == 1:
            print('Hint: The number is odd!')

        # Informs number of lives left, asks for guess and counts attempts    
        print('You have ' + str(lives) + ' lives left.')
        print('Take a guess.')
        i = i + 1

        # Validates if the guess is right, informs if it is too high or too low
        try:
            guess = int(input())
            
            if guess > number and guess <= 100:
                print('Your guess is too high.')
                lives = lives - 1
            elif guess < number and guess >= 1:
                print('Your guess is too low.')
                lives = lives - 1
            elif guess < 1 or guess > 100:
                print('The number is >= 1 and <= 100!')
                lives = lives - 1
            else:
                print('You are right!')
                break

        # Handles non integer input error    
        except ValueError:
            print('The number is an integer!')
            lives = lives - 1



# Main function / setting the difficulty level
def guessingGame():
    global lives
    global number
    import random
    number = random.randint(1, 100)

    while True:
        print('Choose difficulty level: (Easy / Hard)')
        level = input()

        # Defines number of lives, calls takeAGuess function and calculates score
        if level == 'Easy':
            lives = 10
            takeAGuess()
            print('The correct number is ' + str(number) + '.')
            score = lives * 10
            break
        elif level == 'Hard':
            lives = 5
            takeAGuess()
            print('The correct number is ' + str(number) + '.')
            score = lives * 20
            break

        # Handles invalid input
        else:
            print('That is not a valid difficulty level!')

    print('Score = ' + str(int(score)) + '%')



# Explains to the user how to play the game and calls main function
print('Hi! This is a number guessing game.')
print('Set the difficulty level and guess an integer between 1 and 100.')
guessingGame()



# Replay / exit condition
while True:
    print('Do you want to play again? (y/n)')
    playAgain = input()
    if playAgain == 'y':
        guessingGame()
    elif playAgain == 'n':
        import sys
        sys.exit()
