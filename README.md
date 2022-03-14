# Hangman Game
## 1. Purpose of the project
Hangman is a Python terminal game, wich runs in the Code Institute mock terminal on Heroku.

Users guess the right word by entering the right letters. They only have six lives, so if they guess six times wrong, they are executed! 
![Am I Responsive](docs/Naamloos.png)
for the live site click
[here](https://hangman-game-ms.herokuapp.com/)

## 2. How to play
 The user can play this game by entering commands into the terminal. They must guess the letters correctly and have six guesses. The word will appear as "----", but if the user guesses the right letter, then the letter will appear instead of "-.". When the user enters a letter they have already guessed before, or puts a character that is invalid, they get a warning and must guess again. The user must guess all the letters in the word to win.

 ## 3. features
 ### existing features
 - Name input screen 
   - the user must input his name
 ![name input](docs/name.png)
 
 - Welcome screen
   - The user can choose either "P" for "Play game" or "H" for "How to play" here.
![welcome screen](docs/menu.png)

- How to play
  - In this section, the user can see how the game is played and can press enter to return to the previous page
![How to play](docs/how-to-play.png)

- The game
  - The computer selects a random word
  - A letter must be guessed by the user
  - If the user guesses correctly, the letter will be displayed
  - They will lose a life if they guess the wrong letter, and   the hangman will start to appear
  ![the game](docs/game.png)
  - The user can see how many lives they have left and what letters they have already used
  - After guessing the word, the user can move on to the next
  -  The user can choose to play again if they die

### future features
- set difficulty levels
- add highscores 

## 4. Technology
These are the Technology I used for this project.
- Python
- Git
- Gitpod
- Github
- Heroku
- Tinypng
- Lucid
![lucid](docs/lucid.png)

## 5. Testing
I have manually tested this project by doing the following:

- Passed the code through a PEP8 linter and confirmed there are no problems.
![pep8](docs/pep8.png)
- Given invalid inputs: strings when numbers are excepted, out of bounds inputs, same input twice.
- Tested in my local terminal and the Code Institute Heroku terminal.
- Name validation
![testing](docs/name-validation.png)
- Press enter validation
![testing](docs/hvalidator.png)
- letter input validation
![testing](docs/game-validator.png)
- Letter is in the word
![testing](docs/letter-in-word.png)
- Letter is not in the word
![testing](docs/letter-not-in-word.png)
- Win
![testing](docs/win.png)
- Died
![testing](docs/died.png)
- Continue validation
![testing](docs/validation.png)

## 6. Bugs
### Solved bugs

### Remaining bugs
it is not working on iphone, and the Code Institute tutor told me this :

Im looking into it, yes on iphone it is not working but in the browser the deployed version will work.

So it appears that it is not designed to be run on a mobile at all, it is not responsive and therefore I don't believe that testing on a mobile will go ahead.

This is nothing you have done, it is the liblary used to create the console "emulator", its just not compatible.

I would document this in your readme if you like, but the outcome is that all projects using this template, which is a requirement of pp3 will have the same issue.
## 7. Deployment
This game was deployed to GitHub pages :

### Gitpod

1. In gitpod workspaces
2. I choose the right workspace/repo
3. Now i can write my code and readme
4. To save my code I Type in the terminal : git add .
5. I type git commit -m "comment"
6. I type git push to push it to github

### Heroku

1. Fork or clone this repository
2. Create a new Heroku app
3. Set the buildbacks to Pyhton and NodeJS in that order
4. Link the Heroku app to repository
5. Click on Deploy

## 8. Credits
My mentor Rohit Sharma
Code institute slack community
Stackoverflow
w3schools
youtube tutorials