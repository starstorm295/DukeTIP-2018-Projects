import random

##big hangman
print("  _    _          _   _  _____   __  __          _   _ ")
print(" | |  | |   /\   | \ | |/ ____| |  \/  |   /\   | \ | |")
print(" | |__| |  /  \  |  \| | |  __  | \  / |  /  \  |  \| |")
print(" |  __  | / /\ \ | . ` | | |_ | | |\/| | / /\ \ | . ` |")
print(" | |  | |/ ____ \| |\  | |__| | | |  | |/ ____ \| |\  |")
print(" |_|  |_/_/    \_\_| \_|\_____| |_|  |_/_/    \_\_| \_|")
print("Taylor Farley, Kathryn Zavadil, Myles Crockem, Colby DuHamel")
print("")
easyWords = ["shadowofthecolossus","leagueoflegends","grandtheftauto","supersmashbros","legendofzelda","supermarioodyssey","sonicthehedgehog","streetfighter","residentevil","undertale"]
hardWords = ["fortnite","minecraft","pubg","cuphead","octodad","godofwar","titanfall","fallout","overwatch","darksouls","skyrim","splatoon","callofduty","pokemon","thesims","pacman","tetris","doom"]

def isAlpha(char):
  if(char == "a" or char == "b" or char == "c" or char == "d" or char == "e" or char == "f" or char == "g" or char == "h" or char == "i" or char == "j" or char == "k" or char == "l" or char == "m" or char == "n" or char == "o" or char == "p" or char == "q" or char == "r" or char == "s" or char == "t" or char == "u" or char == "v" or char == "w" or char == "x" or char == "y" or char == "z"):
    return True


uwuMode = False
cheatMode = False
difficulty = 0
selectedDifficulty = False
lives = 6
victory = False

def drawMan():
  boiNum = 0
  boiNum = random.randint(0,3)
  if(lives > 6 and boiNum <= 1):
    print("____.    ") 
    print("|_(._.)_ ") 
    print("| \_|_/  ") 
    print("|   |    ") 
    print("|  / \   ") 
    print("|        ")
    print("|_______ ")
  if(lives > 6 and boiNum == 2):
    print("____.    ") 
    print("| (._.)  ") 
    print("|___|___ ") 
    print("|   |    ") 
    print("|  / \   ") 
    print("|        ")
    print("|_______ ")
  if(lives == 6):
    print("____.    ") 
    print("|        ")
    print("|        ") 
    print("|        ") 
    print("|        ") 
    print("|        ")
    print("|_______ ")
  if(lives == 5):
    print("____.    ") 
    print("|  ( )   ") 
    print("|        ") 
    print("|        ") 
    print("|        ") 
    print("|        ")
    print("|_______ ")
  if(lives == 4):
    print("____.    ") 
    print("|  ( )   ") 
    print("|   |    ") 
    print("|   |    ") 
    print("|        ") 
    print("|        ")
    print("|_______ ")
  if(lives == 3):
    print("____.    ") 
    print("|  ( )   ") 
    print("|  /|    ") 
    print("|   |    ") 
    print("|        ")
    print("|        ")
    print("|_______ ") 
  if(lives == 2):
    print("____.    ") 
    print("|  ( )   ") 
    print("|  /|\   ") 
    print("|   |    ") 
    print("|        ") 
    print("|        ")
    print("|_______ ")
  if(lives == 1):
    print("____.    ") 
    print("|  ( )   ") 
    print("|  /|\   ") 
    print("|   |    ") 
    print("|  /     ") 
    print("|        ")
    print("|_______ ")
  if(lives == 0):
    print("____.    ") 
    print("|  ( )   ") 
    print("|  /|\   ") 
    print("|   |    ") 
    print("|  / \   ")
    print("|_______ ")
 


while(selectedDifficulty != True):
  press = input("Choose a difficulty. Type '0' for easy or '1' for hard ")
  if(press == "0"):
    difficulty = 0
    print("Easy Mode Selected!")
    selectedDifficulty = True
  if(press == "1"):
    difficulty = 1
    print("Hard Mode Selected!")
    selectedDifficulty = True
  if(press == "uwu"):
    print("what's this?")
    uwuMode = True
  if(press == "i am a cheater"):
    print("If it makes you happy, I guess.")
    difficulty = 0
    cheatMode = True
    selectedDifficulty = True
  if(press == "upupdowndownleftrightleftrightba"):
    print("cool cool fam")
    difficulty = 1
    lives = 999
    selectedDifficulty = True

currentWord = ""
if(difficulty == 0):
  currentWord = easyWords[random.randint(0,9)]
if(difficulty == 1):
  currentWord = hardWords[random.randint(0,17)]
letters = list(currentWord)
length = len(currentWord)

usedLetters = []
wordBlank = []
for a in range(length):
  wordBlank.append("_")
lettersguessed = 0
guessCorrect = False
blanks = "_ "


while(lives == 0 or victory != True):
  drawMan()
  if(cheatMode == True):
    print(currentWord)
  guessCorrect = False
  print("The word is " + str(length) + " letters long. [" + str(lives) + " lives left]")
  print(*wordBlank)
  text = input("Guess a letter!")
  text = text.lower()
  usedAgain = False
  #check if the letter is valid
  if(isAlpha(text) and len(text) == 1):
    for e in range(len(usedLetters)):
      if(text == usedLetters[e]):
        usedAgain = True
    for b in range(length): #correct guess
      if(text == letters[b-1]): 
        wordBlank[b-1] = (str(text))
        guessCorrect = True
        if(usedAgain != True):
          lettersguessed += 1
        
    for c in range(length): #testing for a win
      if(lettersguessed == length):
        victory = True
    if(usedAgain != True):
      usedLetters.append(text)
  else:
    print('\033[1m' + "Invalid Response. Be sure your input is a letter and only one character long")
    guessCorrect = True
  if(victory == True):
    print("Victory!!! The word was \'" + currentWord + "\'!!")
    break
  print("Already used:" + str(list(usedLetters)))
  if(guessCorrect == False):
    if(usedAgain != True):
      lives -= 1
      print('\033[1m' + "There are no " + text + "\'s in the word. Try again [-1 life]")
  if(lives == 0):
    print('\033[1m' + "Game Over. The word was \'" + currentWord + "\'")
    print("| ||")
    print("|||_")
    break
  if(usedAgain == True):
    print("already used that letter!")
 
if(victory == True): 
  if(uwuMode == False):
    print("  (:D)/  ") 
    print("   /|    ") 
    print("    |    ") 
    print("   / \   ")
  if(uwuMode == True):
    print("  (uwu)/ ") 
    print("   /|    ") 
    print("    |    ") 
    print("   / \   ")
print("Thanks for playing!")
pressedExit = False
while(pressedExit == False):
  bloop = input("press any key to exit")
  if(len(bloop) > -1):
    pressedExit = True

