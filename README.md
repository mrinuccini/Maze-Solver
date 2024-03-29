# Maze Solver
![Language](http://ForTheBadge.com/images/badges/made-with-python.svg)

<br/>

![Open Source](https://badges.frapsoft.com/os/v2/open-source.svg?v=103)

# About the project

<br/>

This repository contains the source code of a python application that allow you to generate mazes and solve them. You can also draw your own walls.

<br/>

<p align="center">
    <img src="https://i.imgur.com/cozklUP.png">
</p>

# Features

* You can choose different pathfinding algorithms : Breadth-First algorithm, A* algorithm

<br/>

* You can choose different maze generation algorithms : Kruskal's Algorithm, Depth Search First algorithm

<br/>

* You can draw your own walls :

<p align="center">
    <img src="https://i.imgur.com/LPFG4KE.png", width=500>
</p>

<br/>

* The `Clear` button allow you to clear the canvas and the `Solve` button launch the pathfinding algorithm

# Solving & Generation Algorithms
### Generation Algorithms

* **Kruskal's Algorithm :**

<p align="center">
    <img src="https://i.imgur.com/ILhObAL.png", width="45%">
    <span>&nbsp;&nbsp;&nbsp;</span>
    <img src="https://i.imgur.com/H8Oz26f.png", width="45%">
</p>

<br/>

* **Depth Search First Algorithm :**

<p align="center">
    <img src="https://i.imgur.com/pVCFdBX.png", width="45%">
    <span>&nbsp;&nbsp;&nbsp;</span>
    <img src="https://i.imgur.com/OjREQAl.png", width="45%">
</p>

<br/>

### Solving Algorithms
* **Breadth-First (slow but gives the shortest path) :**

<p align="center">
    <img src="https://i.imgur.com/BhqKbdV.png", width="45%">
    <span>&nbsp;&nbsp;&nbsp;</span>
    <img src="https://i.imgur.com/A5fmtZs.png", width="45%">
</p>

* **A star Algorithm (fast and gives the shortest path) :**

<p align="center">
    <img src="https://i.imgur.com/jkZc1fI.png", width="45%">
    <span>&nbsp;&nbsp;&nbsp;</span>
    <img src="https://i.imgur.com/Ij5OKdO.png", width="45%">
</p>

# Roadmap
### GUI
- [x] Allow the user to draw walls
- [ ] Allow the user to move the start and finish

## Generation algorithms
- [x] Add support for Kruskal's algorithm
- [x] Add support for Depth First Search algorithm 

### Solving algorithms
- [x] Add support for Breadth-First algorithm
- [x] Add support for A* pathfinding algorithm

# Getting started
### Prerequisites
This project uses several differents library to work

<br/>

* [**Python**](https://www.python.org/) : Python 3.10 or later

<br/>

Run the file `scripts/prerequisites.bat` to install all dependencies or install them individually.

<br/>

* **Numpy** :
```sh
pip install numpy
```

<br/>

* **Colour** :
```sh
pip install colour
```

### Running
To run the project open and run `src/main.py` in the IDE of your choice
