import random

countries = [
    "pakistan",
    "canada",
    "brazil",
    "japan",
    "australia",
    "egypt",
    "germany",
    "argentina",
    "norway",
    "mexico",
    "south korea",
    "new zealand",
    "south africa",
    "united states",
    "saudi arabia",
    "france",
    "italy",
    "kenya",
    "turkey",
    "indonesia"
]

hangman_pictures = [
    """
     +---+
         |
         |
         |
        ===
    """,
    """
     +---+
     O   |
         |
         |
        ===
    """,
    """
     +---+
     O   |
     |   |
         |
        ===
    """,
    """
     +---+
     O   |
    /|   |
         |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
         |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
    /    |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
    / \\  |
        ===
    """
]


def play_game():
    country = random.choice(countries)
    guessed_letters = []
    wrong_guesses = 0
    max_wrong_guesses = 6

    print("\nWelcome to World Hangman!")
    print("Guess the country one letter at a time.")
    print("You have 6 wrong guesses allowed.")

    while wrong_guesses < max_wrong_guesses:
        print(hangman_pictures[wrong_guesses])

        hidden_word = ""

        for letter in country:
            if letter == " ":
                hidden_word += "  "
            elif letter in guessed_letters:
                hidden_word += letter + " "
            else:
                hidden_word += "_ "

        print("Country:", hidden_word)
        print("Guessed letters:", ", ".join(sorted(guessed_letters))
              if guessed_letters else "None")
        print("Wrong guesses:", wrong_guesses, "/", max_wrong_guesses)

        if all(letter in guessed_letters for letter in country
               if letter != " "):
            print("\nCongratulations! You guessed the country!")
            print("The country was:", country.title())
            return True

        guess = input("\nEnter a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter one letter only.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try another one.")
            continue

        guessed_letters.append(guess)

        if guess in country:
            print("Correct guess!")
        else:
            wrong_guesses += 1
            print("Wrong guess!")

    print(hangman_pictures[wrong_guesses])
    print("\nGame over! You ran out of guesses.")
    print("The country was:", country.title())

    return False


wins = 0
losses = 0

while True:
    result = play_game()

    if result:
        wins += 1
    else:
        losses += 1

    print("\nYour score:")
    print("Wins:", wins)
    print("Losses:", losses)

    play_again = input("\nDo you want to play again? (yes/no): ").lower().strip()

    if play_again != "yes":
        print("\nThanks for playing World Hangman!")
        print("Final wins:", wins)
        print("Final losses:", losses)
        break