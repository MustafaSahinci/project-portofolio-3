# Hangman Game
## 1. Purpose of the project
Hangman is a Python terminal game, wich runs in the Code Institute mock terminal on Heroku.

users must guess the right word by inputting the  right letters. The users have 6 lives, if the guess 6 times wrong they die and the man will be hanged! 
![Am I Responsive](docs/............)
for the live site click
[here](https://hangman-game-ms.herokuapp.com/)

## 2. How to play
The user can play this game by inputting commands into the terminal. They must guess the right letters. First the word is displayed like this "----" if the user  guesses the rigt letter, then the letter wil replace the "-". If the user puts a letter they already guessed before they get a warning and must guess again  

The user can play by inputting commands into the mock terminal. The user must guess the hidden word, represented with "_ _ _ _" to show the user how many letters are in the word. As the player corrrectly guesses letters, the "_" are replaced with the correct letter. If a player puts in an incorrect command, an error message displays and the player is asked to resubmit their choice. The game is over either when the player has correctly guessed the word or they have run out of lives.