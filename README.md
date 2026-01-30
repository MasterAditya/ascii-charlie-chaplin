# ASCII-Style Face Image of Charlie Chaplin

## Project Purpose

This project demonstrates **Python fundamentals and logic building** by generating an **ASCII-style face image of Charlie Chaplin** using only basic programming constructs.

The focus of the project is on:
- Logical decision-making
- Use of loops and conditional statements
- Converting a visual idea into simple, explainable rules

No external libraries, image converters, or advanced graphics techniques are used.

---

## How the Code Works

The terminal screen is treated as a **2D grid** of rows and columns.

For each `(row, column)` position, the program decides what character to print based on logical conditions:
- Hat
- Eyes
- Nose
- Moustache
- Face outline
- Empty space

Each facial feature is implemented as a separate function (`is_hat`, `is_eye`, etc.).  
A **priority-based `if-elif` structure** ensures correct overlapping of features.

Simple arithmetic is used only to support logic, such as checking whether a position lies on the face outline.

---

## How to Run the Program

### Requirements
- Python 3.x
- No external libraries required

### Steps
1. Clone this repository or download the file.
2. Open a terminal in the project directory.
3. Run the program:

```bash
python ascii_charlie_chaplin.py
