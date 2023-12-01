# Dance Dance Revolution Game
This is the python programing project for the 15-112 course 

* The name of the project is “EXO-Revolution”, which is an adaptation of “Dance Dance Revolution”. This is mainly designed for EXO-L, the fan of EXO. The game rule is, by pressing the keyboard, you have to hit the music note coherent to the music as precisely as you can. In addition to the basic game feature, you can also play games with EXO in the battle mode and then access detailed score information. 

* How to run the project.
  Before running the project, you need to download the folder called *TP*, which includes all needed files for the project. To run the project, simply run *EXO-Revo.py* which is inside the folder *TP*. 
  The project uses beatmap which is generated from *beatLst.py*. This file is already imported in *EXO-Revo.py*, so just make sure you download *TP* folder to access all required files. 

* Which libraries you're using that need to be installed.
  You need to install aubio and pygame, which is used for onset detection for any given music and play music in Python. For the rest python-imported libraries or cmu_112_graphics.py used for this project, it’s already imported in *EXO-Revo.py* and included in the *TP* folder, so you don’t need to do anything else. 
  To install aubio, you can check the official website of aubio.
  To install pygame, you can check CMU 15-112 official website or the official website of pygame.

* A list of any shortcut commands that exist. Shortcut commands can be used to demonstrate specific features by skipping forward in a game or loading sample data. 
   * Select Your Song
      * For example, copy and paste this song file name: Peter Pan.mp3
      * Press e: back to main page
      * Press l: see the song list and decide which song to play
      * In this case, press 0 to choose the song called “Peter Pan”
      * Press s: return to the page where you select the song
      * Press e: back to main page
   * Play Game 
      * Piece introduction
      * “Free-hit”: use mouse to hit (the white circle surrounded by a red rectangle)
   * Multiplier: press the keyboard to hit (The red circle centered by the text ‘2X’)
   * Normal piece: press the keyboard to hit [regular circle with color; the color of normal pieces may vary]
   * Mouse Press: simply use mouse
   * Key Press: there are 5 trackers at the bottom of the screen. From left to right, “q”, “w”, “e”, “o”, “p”. So press the piece falling to each tracker by the given key.
   * After play game, press f: back to main page; and play again
   * For any song, finish *intro* and *practice* first, then you can access *battle*
     * Note: you must play the game instead of simply running the game and do nothing during the game. Otherwise, the fake game experience makes you unable to access detailed score information, since you didn’t play the game at all!
   * History
      * Press f: back to main page
      * Click mouse to type in song file name, such as “Peter Pan.mp3”, and press l to access detailed information
      Note: you must play the game instead of simply running the game and do nothing during the game. Otherwise, although you ‘finished’ intro, practice, battle and type in the correct file name, you still cannot access detailed score information, since you didn’t play the game at all!
