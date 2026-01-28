# FreeCodeCamp Python Practice

This repository contains Python exercises completed as part of **FreeCodeCamp's curriculum and certificate programs**. The focus is on **practical learning**, applying Python concepts, and developing problem-solving skills through small projects and exercises.

---

## About This Repository

Exercises in this repository were completed while following FreeCodeCamp's Python curriculum. The goal is to **practice Python concepts in real exercises**, rather than just theory.  
 
Projects and scripts demonstrate **learning in action** and reflect my **early journey in Python programming**. Each exercise is self-contained, includes comments and docstrings explaining the purpose, and can be run independently.

---

## Curriculum Overview

The FreeCodeCamp Python course teaches the fundamentals of Python programming. To earn the Python certification, learners must:

- Complete the required projects to qualify for the certification exam  
- Pass the Python Certification exam  

Core topics in the course include:

- Python Basics  
- Loops and Sequences  
- Dictionaries and Sets  
- Error Handling  
- Classes and Objects / OOP  
- Linear Data Structures  
- Algorithms  
- Graphs and Trees  
- Dynamic Programming  

---

## Purpose of This Repository

This repository serves as a **learning journal**. It shows the exercises and small projects I completed while following the FreeCodeCamp Python curriculum.  

It is **primarily for learning and experimentation**, so code may not always be polished. Larger, refined projects will be separated into their own repositories.

---

## Projects

### 1. **PIN Extractor** (`pin_extractor.py`)
A beginner-friendly exercise focused on string manipulation.  
- Extracts numeric PIN codes from strings  
- Practices loops, conditionals, and basic data processing  

---

### 2. **ISBN Validator** (`isbn_validator.py`)
Validates ISBN-10 and ISBN-13 codes.  
- Checks proper format  
- Calculates checksums to ensure validity  
- Introduces basic algorithmic thinking  

---

### 3. **Planet Class OOP Exercise** (`planet_class.py`)
Implements a Planet class to model celestial objects.  
- Demonstrates class attributes and instance methods  
- Introduces `__str__` and basic object modeling  

---

### 4. **Musical Instrument OOP Example** (`musical_instrument_oop.py`)
Demonstrates object-oriented programming with musical instruments.  
- Shows inheritance  
- Method overriding  
- Reinforces class relationships  

---

### 5. **User Settings Manager** (`user_settings_manager.py`)
Manages user preferences for appearance, personality, and accent colors.  
- Uses structured getter and setter functions  
- Reinforces dictionaries and state management  

---

### 6. **Game Character Stats Tracker** (`game_character_stats_tracker.py`)
Tracks stats for a game character.  
- Attributes include name, health, mana, and level  
- Uses validation logic  
- Introduces encapsulation and controlled state updates  

---

### 7. **Employee Salary Tracker** (`employee_salary_tracker.py`)
Manages employee data with promotions and salary tracking.  
- Uses validation rules  
- Implements `__str__` and `__repr__` properly  
- Strengthens real-world OOP modeling  

---

### 8. **Medical Records Validator** (`validate_medical_records.py`)
Performs validation checks on medical record data.  
- Practical data validation  
- Combines conditionals, loops, and defensive programming  

---

### 9. **Email Simulator** (`email_simulator.py`)
Simulates sending and receiving emails between users.  
- Users have inboxes  
- Can send, read, and delete emails  
- Introduces interaction between multiple classes  

---

### 10. **Budget App** (`budget_app.py`)
A more complex project combining logic and presentation.  
- Tracks deposits, withdrawals, and transfers  
- Generates a spending chart  
- Requires careful state tracking and calculations  

---

### 11. **Media Catalogue** (`media_catalogue_oop.py`)
An object-oriented media catalogue for movies and TV series.  

- Uses inheritance (`Movie` → `TVSeries`)  
- Implements custom exceptions  
- Separates parent vs child classes using `type()`  
- Clean `__str__` formatting  

Focuses on OOP design, validation, and polymorphism awareness.

---

### 12. **Player Movement OOP** (`player_movement_oop.py`)
An object-oriented exercise using abstract base classes.  

- Uses `ABC` and `@abstractmethod`  
- Tracks movement on a 2D grid  
- Demonstrates leveling up by extending behavior  

Introduces enforced interfaces and abstract design.

---

### 13. **Discount Engine OOP** (`discount_engine_oop.py`)
The most advanced exercise in the repository.  

- Implements multiple discount strategies  
- Uses abstract base classes and polymorphism  
- Calculates optimal outcomes dynamically  
- Models a real-world strategy pattern  

Demonstrates clean architecture, extensibility, and advanced OOP thinking.

---

### 14. **Linked List OOP** (`linked_list_oop.py`)
A basic implementation of a singly linked list.  

- Uses a nested `Node` class  
- Supports adding and removing elements  
- Tracks list length manually  
- Demonstrates pointer-based data structures  

Introduces linked data structures and low-level memory-style thinking.

---

### 15. **Hash Table OOP** (`hash_table_oop.py`)
A simple implementation of a hash table data structure.  

- Uses a custom hash function  
- Handles collisions using nested dictionaries  
- Supports add, remove, and lookup operations  
- Demonstrates key concepts behind hash-based data structures  

Introduces hashing, collision handling, and efficient key-based access.

---

### 16. **Binary Search Algorithm** (`binary_search_algorithm.py`)
An implementation of the binary search algorithm on a sorted list.

- Efficiently searches for a value in logarithmic time (O(log n))
- Tracks and returns the path of inspected elements
- Demonstrates divide-and-conquer problem solving

Introduces algorithmic thinking and performance-aware searching.

---

### 17. **Square Root Bisection Method** (`square_root_bisection.py`)

Approximates the square root of a number using the bisection algorithm.

- Uses iterative narrowing with configurable tolerance
- Handles edge cases (0, 1, negative numbers)
- Demonstrates numerical methods and convergence control

---

### 18. **Merge Sort Algorithm** (`merge_sort.py`)

Implements the merge sort algorithm using recursion.

- Uses divide-and-conquer strategy
- Sorts the list in place
- Demonstrates recursion and array merging logic
- Time complexity: O(n log n)

---

### 19. **Quick Sort Algorithm** (`quick_sort.py`)

Implements the quick sort algorithm using a functional approach.

- Uses a pivot-based divide-and-conquer strategy
- Returns a new sorted list (not in-place)
- Demonstrates recursion and list comprehensions
- Average time complexity: O(n log n)
- Worst case: O(n²)

---

### 20. **Selection Sort** (`selection_sort.py`)

Implements the selection sort algorithm to sort a list of items in ascending order.  

- Iteratively selects the smallest remaining element and moves it to the sorted portion.  
- Demonstrates basic sorting logic and in-place swapping.

---

### 21. **Luhn Card Validator** (`luhn_card_validator.py`)

Validates credit and debit card numbers using the **Luhn algorithm**.  

- Cleans input by removing spaces and dashes.  
- Doubles every second digit from the right, subtracts 9 if result > 9.  
- Sums all digits and checks if divisible by 10 to determine validity.  
- Demonstrates basic algorithm implementation, loops, and input validation.

---

### 22. **Tower of Hanoi Solver** (`hanoi_solver.py`)

An object-oriented Python exercise that demonstrates recursion and problem-solving:

- Solves the classic Tower of Hanoi puzzle for `n` disks
- Tracks the state of rods after each move
- Returns a visual step-by-step progression of all moves
- Demonstrates recursion and stack-based thinking

---

### 23. **Dijkstra Shortest Path Algorithm** (`dijkstra_shortest_path.py`)

A Python implementation of **Dijkstra's algorithm** using an adjacency matrix:

- Finds the shortest paths from a start node to all other nodes
- Supports optional single-target shortest-path queries
- Returns both distances and actual paths
- Demonstrates greedy algorithm design and graph traversal

---

### 24. **Adjacency List to Matrix Converter** (`adj_list_to_matrix.py`)

A Python script to convert a graph from **adjacency list** to **adjacency matrix**:

- Accepts a dictionary representing the adjacency list
- Generates a 2D adjacency matrix
- Prints the matrix row by row
- Useful for transitioning between different graph representations

---

### 25. **Generate Parentheses (BFS)** (`generate_parentheses.py`)

Generates all valid combinations of parentheses for a given number of pairs.

- Uses a queue-based **Breadth-First Search (BFS)** approach
- Ensures correctness by tracking open and closed parentheses counts
- Demonstrates constraints-based generation
- Common algorithmic interview problem

---

### 26. **Depth-First Search (DFS)** (`dfs_matrix.py`)

Implements Depth-First Search on a graph represented as an adjacency matrix.

- Uses an explicit stack (iterative DFS)
- Tracks visited nodes to avoid cycles
- Demonstrates graph traversal fundamentals
- Useful for understanding paths, connectivity, and graph exploration

---

### 27. **N-Queens (DFS & Backtracking)** (`dfs_n_queens.py`)

Solves the classic N-Queens problem using depth-first search with backtracking.

- Places queens row by row while enforcing constraints
- Prevents column and diagonal conflicts
- Demonstrates recursive DFS and pruning
- Returns all valid board configurations

A core backtracking problem commonly used in technical interviews.

---

