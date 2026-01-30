# Size of the square grid used to print the ASCII face
GRID_SIZE = 25

# Calculating the center of the grid to place facial features symmetrically
CENTER_ROW = GRID_SIZE // 2
CENTER_COL = GRID_SIZE // 2

# Radius of the face and thickness of the outline
FACE_RADIUS = 8
FACE_THICKNESS = 2


def is_hat(row, col):
    """
    Determines whether the current (row, col) position
    belongs to Charlie Chaplin's bowler hat.

    The hat is constructed using simple row and column ranges
    to simulate a tapered shape (narrow top, wider middle, widest brim).
    """

    # Top of the hat crown (narrow section)
    if row == 2 and 10 <= col <= 14:
        return True

    # Middle of the hat crown (wider section)
    if 3 <= row <= 4 and 8 <= col <= 16:
        return True

    # Hat brim (widest section)
    if row == 5 and 6 <= col <= 18:
        return True

    return False


def is_face_outline(row, col):
    """
    Determines whether the current position lies on the
    outline of the face.

    The face is treated as a circle centered at (CENTER_ROW, CENTER_COL).
    Only points whose distance lies within a specific range
    are considered part of the outline.
    """

    # Squared distance from the center of the face
    distance_sq = (row - CENTER_ROW) ** 2 + (col - CENTER_COL) ** 2

    # Outer and inner boundaries of the face outline
    outer = FACE_RADIUS ** 2
    inner = (FACE_RADIUS - FACE_THICKNESS) ** 2

    # Returns True only for points forming the circular outline
    return inner <= distance_sq <= outer


def is_eye(row, col):
    """
    Checks whether the position corresponds to either of the eyes.
    Eyes are placed symmetrically on the same row.
    """
    return row == 9 and col in (9, 15)


def is_nose(row, col):
    """
    Adds a minimal nose representation using a single character
    placed at the center column.
    """
    return row == 11 and col == CENTER_COL


def is_moustache(row, col):
    """
    Determines whether the position belongs to Charlie Chaplin's
    iconic 'toothbrush' moustache.

    The moustache is kept small and centered to maintain recognizability
    without increasing complexity.
    """
    return row in (12, 13) and 11 <= col <= 13


def get_character(row, col):
    """
    Decides which character should be printed at a given (row, col).

    A priority-based approach is used so that important features
    like the hat and facial details appear correctly when regions overlap.
    """

    if is_hat(row, col):
        return "#"
    elif is_eye(row, col):
        return "o"
    elif is_nose(row, col):
        return "|"
    elif is_moustache(row, col):
        return "="
    elif is_face_outline(row, col):
        return "*"
    else:
        return " "


def render_face():
    """
    Iterates over the entire grid and prints the ASCII face
    row by row by evaluating each position logically.
    """

    for row in range(GRID_SIZE):
        line = ""
        for col in range(GRID_SIZE):
            line += get_character(row, col)
        print(line)


# Entry point of the program
if __name__ == "__main__":
    render_face()
