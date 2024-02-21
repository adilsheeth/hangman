import random, time, os

drawings = {
    "hangman": [
    """
  +---+
      |
      |
      |
     ===""",

    """  
  +---+
  O   |
      |
      |
     ===""",
    
    """  
  +---+
  O   |
  |   |
      |
     ===""",

    """  
  +---+
  O   |
  |\  |
      |
     ===""",

    """  
  +---+
  O   |
 /|\  |
      |
     ===""",

    """  
  +---+
  O   |
 /|\  |
 /    |
     ===""",

    """  
  +---+
  O   |
 /|\  |
 / \  |
     ===""",

    ],
    "snowman": [
        """   
   _|==|_
    ('')__/
>--(`^^`) 
  (`^'^'`)
   ======""",

        """

    ('')__/
>--(`^^`) 
  (`^'^'`)
   ======""",

        """

    ('')
>--(`^^`) 
  (`^'^'`)
   ======""",

        """
    

>--(`^^`) 
  (`^'^'`)
   ======""",

        """
    

   (`^^`) 
  (`^'^'`)
   ======""",

        """
    

        
  (`^'^'`)
   ======""",

        """
    

        
  
   ======""",
    ]
}

word_list = {
    "E": ["cat", "dog", "fish", "bird", "cow", "lion", "tiger", "bear", "wolf", "fox", "horse", "sheep", "pig", "mouse", "rat", "duck", "deer", "monkey", "goat", "chicken", "rabbit", "elephant", "frog", "turtle", "bee"],
    "M": ["penguin", "giraffe", "dolphin", "shark", "zebra", "whale", "kangaroo", "leopard", "octopus", "hippo", "camel", "donkey", "peacock", "squirrel", "rhino", "buffalo", "gorilla", "koala", "flamingo", "platypus", "walrus", "beaver", "otter", "badger", "parrot"],
    "H": ["aardvark", "albatross", "armadillo", "baboon", "barracuda", "capybara", "chameleon", "dingo", "echidna", "ferret", "gazelle", "hedgehog", "ibex", "jaguar", "kookaburra", "lemur", "meerkat", "narwhal", "opossum", "porcupine", "quokka", "raccoon", "tapir", "vulture", "wombat"]
}

letter_list = "abcdefghijklmnopqrstuvwxyz"

def clear_screen():
    if os.name == "nt":
        os.system("cls")

def setup():
    clear_screen()

    print("Welcome to HANGMAN ONLINE!\nSponsored by Big Tech Ltd.\nPrototype v0.5.1")
    print("The Objective: To guess an ANIMAL before you're out of turns!\n")
    time.sleep(2)

    name = input("What's your Name? ").title()
    snowman_mode = input("Would you like to play with a SNOWMAN? (Y/N): ").upper() == "Y"
    difficulty = input("Choose your difficulty (E/M/H):").upper()
    if difficulty not in "EMH":
        exit("Invalid Input.")
    
    secret_word = random.choice(word_list[difficulty])
    
    print("\nLet's Play! Good Luck!\n")
    time.sleep(2)
    game(secret_word, name, snowman_mode)

def game(secret_word, name, snowman_mode):
    clear_screen()

    count = 0
    draw_type = "snowman" if snowman_mode else "hangman" 
    uncovered = ["_"] * len(secret_word)
    incorrect_attempts = []

    while count < 6:
        if "_" not in uncovered:
            game_over(True, secret_word)

        print(drawings[draw_type][count])
        print("WORD:", *uncovered)
        print("GUESSED:", *incorrect_attempts)
        guess = input("Your Guess: ").lower().strip()

        if guess == secret_word:
            game_over(True, secret_word)
            return

        elif len(guess) > 1:
            print(f"That's not the word, {name}!\n")
            incorrect_attempts.append(guess)

        elif guess not in letter_list:
            print(f"That's not a letter, {name}!\n")

        elif guess in incorrect_attempts or guess in uncovered:
            print(f"You've already tried that, {name}!\n")

        elif guess not in secret_word or guess in incorrect_attempts:
            print(f"Bad luck, {name}! That's not in the word.\n")
            incorrect_attempts.append(guess)
            count += 1

        else:
            print(f"Go {name}! That's in the word.\n")
            for i in range(len(secret_word)):
                if guess == secret_word[i]:
                    uncovered[i] = guess

        print("...")
        time.sleep(2)
        clear_screen()

    print(drawings[draw_type][count])
    game_over(False, secret_word)

def game_over(win, secret_word):
    if win:
        print("Good job! You guessed it!")
    else:
        print(f"Oh no! Game over.\nThe word was {secret_word}.")
    
    setup() if input("Play again? (Y/N): ").upper() == "Y" else exit("Bye!")

if __name__ == "__main__":
    setup()