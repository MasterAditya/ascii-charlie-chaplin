# ASCII-Style Face Image of Charlie Chaplin (Sketch Version)
# Using only Python fundamentals: loops, conditionals, logic, math

GRID_SIZE = 25
CENTER_ROW = GRID_SIZE // 2
CENTER_COL = GRID_SIZE // 2

FACE_RADIUS = 8
FACE_THICKNESS = 2


def is_hat(row, col):
    # Hat crown
    if 2 <= row <= 4 and 7 <= col <= 17:
        return True
    # Hat brim
    if row == 5 and 6 <= col <= 18:
        return True
    return False


def is_face_outline(row, col):
    # Draw only the outline (not filled face)
    distance_sq = (row - CENTER_ROW) ** 2 + (col - CENTER_COL) ** 2
    outer = FACE_RADIUS ** 2
    inner = (FACE_RADIUS - FACE_THICKNESS) ** 2
    return inner <= distance_sq <= outer


def is_eye(row, col):
    return (row == 9 and col in (9, 15))


def is_nose(row, col):
    # Very subtle nose hint
    return row == 11 and col == CENTER_COL


def is_moustache(row, col):
    # Chaplin's iconic small moustache (2 rows thick)
    return row in (12, 13) and 10 <= col <= 14


def get_character(row, col):
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
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            print(get_character(row, col), end="")
        print()


# Entry point
render_face()
