letter_a = """
.##..
#..#.
#..#.
####.
#..#.
#..#.
"""

letter_b = """
###..
#..#.
###..
#..#.
#..#.
###..
"""

letter_c = """
.##..
#..#.
#....
#....
#..#.
.##..
"""

letter_e = """
####.
#....
###..
#....
#....
####.
"""

letter_g = """
.##..
#..#.
#....
#.##.
#..#.
.###.
"""

letter_h = """
#..#.
#..#.
####.
#..#.
#..#.
#..#.
"""

letter_j = """
..##.
...#.
...#.
...#.
#..#.
.##..
"""

letter_l = """
#....
#....
#....
#....
#....
####.
"""

letter_o = """
.##..
#..#.
#..#.
#..#.
#..#.
.##..
"""

letter_p = """
###..
#..#.
#..#.
###..
#....
#....
"""

letter_r = """
###..
#..#.
#..#.
###..
#.#..
#..#.
"""

letter_u = """
#..#.
#..#.
#..#.
#..#.
#..#.
.##..
"""


letter_y = """
#...#
#...#
.#.#.
..#..
..#..
..#..
"""


letter_z = """
####.
...#.
..#..
.#...
#....
####.
"""


def concatenate_letter(letter):
    result = ""

    for char in letter:
        if char in ["#", "."]:
            result += char

    return result


letters = {
    "A": concatenate_letter(letter_a),
    "B": concatenate_letter(letter_b),
    "C": concatenate_letter(letter_c),
    "E": concatenate_letter(letter_e),
    "G": concatenate_letter(letter_g),
    "H": concatenate_letter(letter_h),
    "J": concatenate_letter(letter_j),
    "L": concatenate_letter(letter_l),
    "O": concatenate_letter(letter_o),
    "P": concatenate_letter(letter_p),
    "R": concatenate_letter(letter_r),
    "U": concatenate_letter(letter_u),
    "Y": concatenate_letter(letter_y),
    "Z": concatenate_letter(letter_z),
}


LETTER_WIDTH = 5
LETTER_HEIGHT = 6


def concatenate_letter_from_grid(letter):
    result = []

    for y in range(LETTER_HEIGHT):
        for x in range(LETTER_WIDTH):
            result.append(letter[x][y])

    return result


def crop_to_content(grid, fill="."):
    xs = [x for x in range(len(grid)) if any(val != fill for val in grid[x])]
    ys = [
        y
        for y in range(len(grid[0]))
        if any(grid[x][y] != fill for x in range(len(grid)))
    ]

    if len(xs) == 0 or len(ys) == 0:
        return []

    return [
        [grid[x][y] for y in range(ys[0], ys[-1] + 1)] for x in range(xs[0], xs[-1] + 1)
    ]


def read_letters_from_grid(grid, fill=".", verbose=True):
    grid = crop_to_content(grid, fill)

    if len(grid) == 0:
        return ""

    result = ""
    for start_col in range(0, len(grid), LETTER_WIDTH):
        concatenated_letter = ""

        for y in range(LETTER_HEIGHT):
            for x in range(LETTER_WIDTH):
                col = start_col + x
                if col < len(grid) and y < len(grid[col]):
                    concatenated_letter += grid[col][y]
                else:
                    concatenated_letter += "."

        found = False
        for letter, letter_pattern in letters.items():
            if concatenated_letter == letter_pattern:
                found = True
                result += letter
                break

        if not found:
            result += "?"

            if verbose:
                print(f"unknown glyph at column {start_col}:")
                for y in range(LETTER_HEIGHT):
                    row = concatenated_letter[
                        y * LETTER_WIDTH : (y + 1) * LETTER_WIDTH
                    ]
                    print(f"    {row}")

    return result

