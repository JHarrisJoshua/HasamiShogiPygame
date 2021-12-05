# Hasami Shogi with Pygame

## Table of Contents

1. [Video Demo](#Video-Demo)
2. [Overview](#Overview)
3. [Program Spec](#Program-Spec)

## Video Demo

<https://youtu.be/Bw8cKjVIezw>

![Shogi](https://user-images.githubusercontent.com/81477294/144761684-fb2cda7a-b853-4296-9425-abcd7c0c6414.gif)

## Overview
### Description
The program represents an abstract board game called Hasami Shogi. The players start with
nine pieces on the first and last rank(row) of a 9x9 board. Black moves first, followed by Red. A
player wins by capturing all or all but one of their opponents pieces. Pieces can move to any empty space on
the same rank or file(no jumping). You can capture enemy pieces (one or multiple) by blocking them on
 opposite sides with two of your pieces( corner pieces must be blocked orthogonally). Win condition is
#assumed to be all or all but one piece captured.

### Program Evaluation
- **Category** Gaming
- **Platform** This program was developed primarily for Desktop. Future consideration may be given to a mobile version.
- **Story** Board game implemented in Python using Pygame. The game is Hasami Shogi (varient 1), a description of which is available at https://en.wikipedia.org/wiki/Hasami_shogi
- **Scope** The current scope of the project is to implement a board game in Python using Pygame. The game is not currently set up to play online via networking, but consideration may be given to adding this feature.

## Program Spec

### 1. User Stories

**User Stories**
* User can play a game of Hasami Shogi via Pygame.
* Players can view the number of pieces captured by each player, as well as whose turn it is.
* The game announces when a player has won visually.
* When a player has won, the user has the option of playing again.

### 2. Application Details

**App Files**
* Main.py loads Pygame and display the board.
* Game.py contains the game mechanics, such as moving and capturing pieces.
* Board.py stores and updates the Board.
* Sprites.py stores the sprite associated with each square on the board. Images are loaded from a subfolder in the directory.

### 3. References

**References**
* https://www.pygame.org/docs/
* https://inventwithpython.com/makinggames.pdf
