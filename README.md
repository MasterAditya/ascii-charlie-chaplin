ASCII-Style Face Image of Charlie Chaplin
Project Purpose
The purpose of this project is to demonstrate Python fundamentals and logical thinking by generating an ASCII-style face image of Charlie Chaplin using only basic programming concepts.
Instead of focusing on visual realism or advanced graphics, the project focuses on:

Logic building
Decision-making using conditions
Understanding how a visual idea can be translated into simple rules

No external libraries, image converters, or advanced graphics techniques are used.
How the Code Works
The terminal screen is treated as a 2D grid of rows and columns.
For each position in the grid, the program decides which character should be printed based on logical rules.
Core Idea
For every (row, column) position:

Check if it belongs to the hat
Else check if it belongs to eyes, nose, or moustache
Else check if it belongs to the face outline
Otherwise, print empty space

This converts a drawing problem into a classification and control-flow problem.
Key Components

Grid and Positioning
A fixed 25 × 25 grid is used.
The center of the grid is calculated to place facial features symmetrically.

Feature-based Functions
Each facial feature is handled by a separate function:
is_hat(row, col) → Determines hat shape using row/column ranges
is_eye(row, col) → Places symmetric eyes
is_nose(row, col) → Adds a minimal nose hint
is_moustache(row, col) → Draws Charlie Chaplin’s iconic moustache
is_face_outline(row, col) → Draws the face outline using a simple distance check
This modular approach improves clarity and makes the logic easy to explain.
Priority-based Rendering
Some features overlap, so a priority order is used:
Hat
Eyes
Nose
Moustache
Face outline
Empty space
The first matching condition determines the character printed at that position.
Rendering the Output
Nested loops iterate over each grid position, build each line character by character, and print the final ASCII image row by row.

How to Run the Program
Requirements

Python 3.x installed
No external libraries required

Steps

Clone the repository or download the file.
Open a terminal in the project directory.
Run the program using:textpython ascii_charlie_chaplin.py

The ASCII-style image of Charlie Chaplin will be displayed directly in the terminal.
Notes

The face is intentionally drawn as an outline rather than a filled shape to keep the focus on logic rather than decoration.
The project avoids advanced graphics techniques to stay aligned with Python fundamentals and logic-building objectives.

Conclusion
This project demonstrates how simple programming constructs such as loops, conditionals, and basic arithmetic can be combined to produce structured and meaningful output. The emphasis is on clarity, explainability, and honest implementation.