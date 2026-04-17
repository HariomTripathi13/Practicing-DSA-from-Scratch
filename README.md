# Practicing DSA from Scratch 🚀

A structured Python workspace designed for practicing fundamental Data Structures, Algorithms (DSA), and logical pattern problems. This repository includes a custom VS Code build environment to handle competitive-programming-style standard I/O locally without cluttering the terminal.

## 📌 Project Overview

When practicing algorithms, manually typing inputs into the terminal repeatedly slows down the learning process. This mini-project solves that by using a custom `.vscode/tasks.json` configuration. It automatically pipes data from an `input.txt` file into your Python scripts and writes the results directly to an `output.txt` file.

### Key Features
* **Automated I/O Piping:** Run scripts using `Ctrl+Shift+B`. It reads `input.txt` and overwrites `output.txt` instantly.
* **Basic Math Implementations:** Standard logic problems to build a strong mathematical foundation (Digit Counting, Number Reversal, Palindromes, Euclidean HCF/GCD, Armstrong Numbers).
* **Pattern Problem Library:** 22 unique ASCII art pattern problems (stars, numbers, and alphabetical grids) mapped mathematically to nested loops.

## 📂 Directory Structure

```text
Practicing-DSA-from-Scratch/
│
├── .vscode/
│   └── tasks.json                # Centralized Logic for the Build Task
│
├── Basic Math Implementations/   # Core mathematical logic problems
│   ├── DSA.py                    # Math solutions (Reverse, HCF, etc.)
│   ├── input.txt                 # Local input values
│   └── output.txt                # Local output results
│
└── Pattern Problems/             # 22 visual logic pattern solutions
    ├── DSA.py                    # Pattern functions (question1 - question22)
    ├── input.txt                 
    └── output.txt                
```

## ⚙️ Setup & Execution

### 1. Configure the Workspace
Ensure you are using **Visual Studio Code**. The custom build task relies on VS Code's internal task runner.

### 2. Panel Arrangement (Recommended)
For the best competitive programming workflow:
1. Open `DSA.py` in the main editor.
2. Go to **View -> Editor Layout -> Split Right**.
3. Open `input.txt` in the top right panel.
4. Open `output.txt` in the bottom right panel.

### 3. Running the Code
1. Place your test variables in the respective `input.txt` file. Each input should be on a new line.
2. In `DSA.py`, uncomment the function you want to test inside the `if __name__ == "__main__":` block.
3. Press **`Ctrl + Shift + B`**.
4. The script will execute, read the inputs, and the results will immediately populate in `output.txt`.

## 🧠 Topics Covered So Far

### Basic Math
* Digit Counting (String length vs. Math division)
* Number Reversal (Modulo and Floor Division)
* Palindrome Validation
* Highest Common Factor (Euclidean Algorithm)

### Patterns
* Growing/Shrinking Triangles
* Number Crowns and Pyramids
* Alternating Binary Matrices
* Alphabetical Grids (Using ASCII `chr()` offsets)
* Symmetrical Star Diamonds
* Bounding Box / Matrix Minimum Distance Patterns
