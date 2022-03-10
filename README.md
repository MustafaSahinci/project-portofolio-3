# Hangman Game
## 1. Purpose of the project
Hangman is a Python terminal game, wich runs in the Code Institute mock terminal on Heroku.

Users guess the right word by entering the right letters. They only have six lives, so if they guess six times wrong, they are executed! 
![Am I Responsive](docs/............)
for the live site click
[here](https://hangman-game-ms.herokuapp.com/)

## 2. How to play
 The user can play this game by entering commands into the terminal. They must guess the letters correctly and have six guesses. The word will appear as "----", but if the user guesses the right letter, then the letter will appear instead of "-.". When the user enters a letter they have already guessed before, or puts a character that is invalid, they get a warning and must guess again. The user must guess all the letters in the word to win.

 ## 3. features
 ### existing features
 - Name input screen 
   - the user must input his name
 ![name input](docs/............)
 
 - Welcome screen
   - The user can choose either "P" for "Play game" or "H" for "How to play" here.
![welcome screen](docs/............)

- How to play
  - In this section, the user can see how the game is played and can press enter to return to the previous page
![How to play](docs/............)

- The game
  - The computer selects a random word
  - A letter must be guessed by the user
  - If the user guesses correctly, the letter will be displayed
  - They will lose a life if they guess the wrong letter, and   the hangman will start to appear
  - When a user inputs an invalid character, a warning appears
  - The user can see how many lives they have left and what letters they have already used
  - After guessing the word, the user can move on to the next
  -  The user can choose to play again if they die

### future features
- set difficulty levels
- add highscores 

## 4. Data models

## 5. Testing
I have manually tested this project by doing the following:

- Passed the code through a PEP8 linter and confirmed there are no problems.
- Given invalid inputs: strings when numbers are excepted, out of bounds inputs, same input twice.
- Tested in my local terminal and the Code Institute Heroku terminal.

## 6. Bugs
### Solved bugs

### Remaining bugs
- No bugs remaining
## 7. Deployment
- Steps for deployment
  - Fork or clone this repository
  - Create a new Heroku app
  - Set the buildbacks to Pyhton and NodeJS in that order
  - Link the Heroku app to repository
  - Click on Deploy

## 8. Credits
