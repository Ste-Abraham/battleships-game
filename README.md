# Battleships Game

The Battleships-Game project is based on the classic board game battleships. The Battleships-Game is written and coded in Python, and is designed to be run in a terminal powered by Heroku. The game allows the user to pick where their vessels are placed on the board, while the computers’ vessels are randomly placed and assigned using Python functions. The winner of the game is determined when all of the opponents’ vessels have been destroyed and hit.

![Responsive site on different devices](/assets/images/am-i-responsive.png)

The above screen shot was generated in https://ui.dev/amiresponsive which shows the responsiveness of the site. 

## Scope – Data Model

My scope for this project was to design and develop a simplistic and functional battleship game, which also gave a real-time visual display so that the user would be able to get timely and affective input and feedback.

There were several data models I came across whilst researching the project:

-	Single board: One board where the computer will randomly place your chosen amount of ships, then the player races against an attempt countdown to destroy all computers ships before they run out of attempts.

-	Two boards: this is where there are two boards, one for the player one for the computer. Player will place ships on their board and computer will do the same. Then you will take it in turns to try and hit each other’s ships.

-	Four boards: this is where there are four overlapping boards in play, one each for the player and computer to place their ships/vessels, and then one each for the player and computer to make their guesses.

The data model I selected was the four board option. This is because, for a new coder using Python, it is the best way to check for overlaps when placing the ships. Using the two-board approach some of the code became complex and would’ve caused issues in the later stages of the project.

I also went for an approach where a newly updated board was printed after every attempt, I found this to be the cleanest and most user friendly approach.

## Features: existing

### Home Screen:

This is the home screen where you are greeted with a welcome message, I used ASCII art sourced from the internet to add some visual appeal to the game. It made the name of the game stand out and draws your eye to it.

![Screenshot of the homescreen](/assets/images/home-screen.png)

### Rules and GO button:

This is where the rules appear defining how to play the game and some of the different variables of the game i.e. ship sizes.

The user is then prompted to enter the game. They must input the word GO. Any variation of this will bring up an invalid message and allow the user to try again.


![Screenshot of the rules and go](/assets/images/rules.png)

### Vessel placement:

This is where the user will choose where their ships are on the board. The game will prompt the user to select whether the vessel is to be placed upright or sideways by inputting S or U. any other characters won’t work.

Once the orientation of the ships is chosen, the user is then prompted to select location by inputting 1-7 – firstly to choose the row then again for the column. Any input other than 1-7 will incur an error message and ask to retry. If the placement is successful, it will be represented by an ‘@’ on the board.

Throughout this process, error messages will appear if information is entered incorrectly, asking the user to input again.


![Screenshot of ship placements](/assets/images/ship-placements.png)

### Player 1 and Computer choices:

This is where player 1 is asked to choose where they think the computers’ vessels are. They make their guess by inputting a number between 1-7, once for a row and again for a column. If they are successful with their guess and it’s a hit, an ‘X’ will appear on the board. This is the same for when it is the computers’ turn to guess. 

If the player tries to guess outside of the parameters, the frame will say invalid input and prompt them to make another guess that is within the game play area.

![Screenshot of player and computer guesses](/assets/images/hit-and-miss.png)

### End of the game:

The game will continue until either player 1 or the computer destroy all of the opponents’ ships. Once this happens, a message will come up announcing the winner, with the option to play again and how to go about that.

![Screenshot of end of game](/assets/images/end-of-game.png)

## Features: future

### Features for future developments include:

Adding colour to the site. The black and white design is simple and clean, however the site may benefit from some colour to make it more aesthetically exciting. This may also help to break the site up into more digestible and easier to read sections.

Adding a PLAY AGAIN button. This would restart the game without having to go back to the home screen again which will create a more seamless user experience.

Adding a name personalisation instead of entering go to begin. In a future development the player will enter their name and this will appear in the game. Then throughout the game, instead of seeing ‘player 1’ the player would experience a more personalised game play.

Finally, adding a leader board would incorporate the user’s inputted name, and would create a reason to come back to the app and game.

## Testing and Bugs/solutions:

### Manual testing:

Manual testing was carried out on the deployed app in several browsers, chrome, Microsoft edge and safari. All the features displayed as designed across all the browsers. 

The testing was carried out by four people. All players played and cycled through the game three times, making sure all functions acted as they were designed. Also, I needed to make sure the code was working correctly, and all invalid inputs were showing error messages as designed. Any issues and errors were reported and fixed.

One error was ‘X’ not showing when a successful hit was made. This was due to an error in one of the if statements missing an = “X” from the end of the function. 

One of the other errors reported was that a number could be inputted out of the game area section as commas were missed off that line of code. To correct this, I had to change 1234567 to 1, 2, 3, 4, 5, 6, 7. This corrected the problem and now a digit outside of these parameters can’t be entered without it returning an invalid input message.

## Validator testing:

The assignment asks you to run the code through pep8 Python Linter to check for any significant issues. When I first entered the code, it came up with many errors. These were then corrected and formatted to remove the errors as shown in the below screen shots. The remaining errors showing are in the ASCII art that reads battleships. These are not significant issues and they do not affect the running of the app. This is the site used to check the code. https://pep8ci.herokuapp.com/

![Screenshot of end of game](/assets/images/ci-linter-before.png)

![Screenshot of end of game](/assets/images/ci-linther-after.png)

## Unfixed Bugs

As far as I am aware, there are no unfixed bugs.

## Deployment:

The steps to achieve this were: 

-	Firstly, fork or clone the repository.
-	Create a new app on Heroku.
-	Ensure you have added a new Config Var in the Heroku settings tab. Key PORT Value 8000.
-	Ensure you have added the correct build packs. Python and NodeJS. In that specific order as this will allow you to run the template provided by Code Institute.
-	In the deployment tab on Heroku link your GitHub repository to the app.
-	Clock ‘Deploy’ and then the app will build.
-  The link to my live site can be found here [Battleships-game](https://battleships-game-sa-0ceebfcaebc3.herokuapp.com/)

## CREDITS

In this section I will make note of all the libraries frameworks, websites and languages used.

The credits are as follows:
-	Python Language used.
-	Inspiration for the form code was taken from Code Institute learning content.
-	A lot of inspiration from love sandwiches walkthrough project and was using course materials.
-	Art taken from ASCII website: https://patorjk.com/software/taag/#p=testall&f=Zodi&t=Battleships
-	YouTube video of one method of battleship code in python language: https://www.youtube.com/watch?v=tF1WRCrd_HQ 
-	YouTube video of one method of battleship code in python language:
https://www.youtube.com/watch?v=Ej7I8BPw7Gk&list=PLpeS0xTwoWAsn3SwQbSsOZ26pqZ-0CG6i
-	Information about the docstring code that I had to add:
https://www.programiz.com/python-programming/docstrings
-	Information about the if name main code that I had to add: 
https://realpython.com/if-name-main-python/
-	A lot of help from Slack community used to help me correct and code my work.
-	The four boards idea and the code for the four game area was taken from slack community
-	My mentor Spencer