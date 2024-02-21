import random
import time
import os
import sys

drawings = {
    0: """  +---+
      |
      |
      |
     ===""",
    1: """  +---+
  O   |
      |
      |
     ===""",
    2: """  +---+
  O   |
  |   |
      |
     ===""",
    3: """  +---+
  O   |
  |\  |
      |
     ===""",
    4: """  +---+
  O   |
 /|\  |
      |
     ===""",
    5: """  +---+
  O   |
 /|\  |
 /    |
     ===""",
    6: """  +---+
  O   |
 /|\  |
 / \  |
     ===""",
}

drawings_cm = {
  0: """   _|==|_
    ('')__/
>--(`^^`) 
  (`^'^'`)
   ======""",
  
  1: """
    ('')__/
>--(`^^`) 
  (`^'^'`)
   ======""",
  
  2: """
    ('')
>--(`^^`) 
  (`^'^'`)
   ======""",
  
  3: """
    
>--(`^^`) 
  (`^'^'`)
   ======""",

  4: """
    
   (`^^`) 
  (`^'^'`)
   ======""",
  
  5: """
    

  (`^'^'`)
   ======""",
  
  6: """
    

  
   ======""",
}

word_list = '''ant baboon badger bat bear beaver camel cat clam cobra cougar
       coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk
       lion lizard llama mole monkey moose mouse mule newt otter owl panda
       parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep
       skunk sloth snake spider stork swan tiger toad trout turkey turtle
       weasel whale wolf wombat zebra'''.split()

letter_list = "abcdefghijklmnopqrstuvwxyz"

def setup():
    os.system("clear")
    secret_word = word_list[random.randint(0, len(word_list))]
    if len(sys.argv) == 2:
      if sys.argv[1] == "dev":
        print("The secret word is:", secret_word, "\n")
    cm = True if input("Would you like to enable Child Mode? (Y/N): ") == "Y" else False
    
    print(f"Welcome to {'SNOWMAN' if cm else 'HANGMAN'} ONLINE!\nSponsored by Big Tech Ltd.\nPrototype v0.4\n")
    time.sleep(3)
    os.system("cls")
    name = input("What's your name? ").title()
    print(f"Hi, {name}! Let's play... HANGMAN!")
    print("The Objective: To guess an ANIMAL before you're out of turns!")
    time.sleep(4)
    in_game(secret_word, name, cm)


def in_game(secret_word, name, cm):
    os.system("cls")
    count = 0
    guessed = ["_"] * len(secret_word)
    letters_tried = []
    
    while count < 6:
      if "_" not in guessed:
        game_over(True, secret_word)
      print((drawings_cm[count] if cm else drawings[count]))
      print("WORD:", *guessed)
      print("TRIED:", *letters_tried)
      guess = input("Your Guess: ").lower().strip()

      if guess == secret_word:
        game_over(True, secret_word)
        return
      elif len(guess) > 1:
        count += 1
        print(f"That's not the word, {name}!\n")
        letters_tried.append(guess)
      elif guess not in letter_list:
        print(f"That's not a letter, {name}!\n")
      elif guess in letters_tried:
        print(f"You've already tried that, {name}!\n")
      elif guess not in secret_word or guess in guessed:
        print(f"Bad luck, {name}! That's not in the word.\n")
        letters_tried.append(guess)
        count += 1
      else:
        print(f"Go {name}! That's in the word.\n")
        for i in range(len(secret_word)):
          if guess == secret_word[i]:
            guessed[i] = guess
      print("...")
      time.sleep(2)
      os.system("cls")

    print((drawings_cm[count] if cm else drawings[count]))
    game_over(False, secret_word)

        
        

def game_over(win, secret_word):
    if not win:
      print("Oh no! Game over.")
      print("The word was", secret_word)
    else:
      print("Good job! You guessed it!")
    setup() if input("Play again? (Y/N): ") == "Y" else exit("Bye!")


setup()