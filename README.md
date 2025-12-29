#This is  for my Ai Lab report-4

# Genetic Algorithm – N Queens Problem

## Introduction
This project solves the **N-Queens problem** using a **Genetic Algorithm**.  
The N-Queens problem asks us to place N queens on an N×N chessboard so that no two queens attack each other. It’s a classic example in Artificial Intelligence and combinatorial optimization.

Instead of using traditional backtracking, I applied a Genetic Algorithm approach, which mimics natural selection. The idea is to evolve a population of candidate solutions until one of them satisfies the constraints.


## How the Algorithm Works
1. **Chromosome Representation**  
   Each chromosome represents a possible arrangement of queens on the board.
2. **Fitness Function**  
   Counts the number of conflicts (queens attacking each other). A solution has fitness = 0.
3. **Population Initialization**  
   Starts with a random population of possible solutions.
4. **Selection**  
   Chooses the best candidates (lowest conflicts).
5. **Crossover**  
   Combines two parents to produce a child solution.
6. **Mutation**  
   Randomly swaps positions to introduce diversity.
7. **Termination**  
   Stops when a solution with zero conflicts is found or after a fixed number of generations.
