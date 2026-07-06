# COS202 Assignments – Mathematical Calculator & CGPA Calculator

## Author
- **Name:** [ADEJUWON ERIOLUWA IYANUAYO]
- **Course:** COS202


## Overview
This repository contains the practical solutions submitted for the COS202 
1. A Mathematical Calculator (MC)
2. A Personal Pocket CGPA Calculator (PPC)

---

## 1. Mathematical Calculator (MC)

### Description
"ZEEEEE Calculator" is a menu-driven, command-based calculator built in 
Python. Instead of typing an operation directly, the user enters a 
command (CALC, C, or OFF), then supplies two numbers and an operator 
symbol when prompted.

### Features
- **CALC** – prompts the user for two numbers and an operator, then computes the result
- **C** – clears/resets the calculator
- **OFF** – exits the program
- Supports the following operators:
  - `+` Addition
  - `-` Subtraction
  - `/` Division (with a "MATH ERROR" message on divide-by-zero)
  - `//` Floor Division
  - `*` Multiplication
  - `**` Exponentiation (Power)
  - `%` Modulus
- Uses Python's `match-case` statement to handle operator selection
- Invalid commands and invalid operators are both handled with clear error messages



---

## 2. Personal Pocket CGPA Calculator (PPC)

### Description
A Python program that calculates a student's CGPA using selection 
control statements (if/elif/else) based on grades and credit units entered.

### Features
- Accepts course credit units and grades as input
- Uses conditional logic to assign grade points (e.g., A=5, B=4, C=3, D=2, F=0)
- Calculates and displays the CGPA automatically

