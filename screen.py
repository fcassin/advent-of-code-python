letter_a = """
.##..
#..#.
#..#.
####.
#..#.
#..#.
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

letter_y = """
#...#
#...#
.#.#.
..#..
..#..
..#..
"""

def concatenate_letter(letter):
    result = ""
    
    for char in letter:
        if char in ["#", "."]:
            result += char
            
    return result

letters = {
    "A": concatenate_letter(letter_a),
    "E": concatenate_letter(letter_e),
    "G": concatenate_letter(letter_g),
    "H": concatenate_letter(letter_h),
    "O": concatenate_letter(letter_o),
    "P": concatenate_letter(letter_p),
    "R": concatenate_letter(letter_r),
    "Y": concatenate_letter(letter_y),
}

def concatenate_letter_from_grid(letter):
    result = []

    for y in range(6):
        for x in range(5):
            result.append(letter[x][y])

    return result

def read_letters_from_grid(grid):
    result = ""

    for start_col in range(0, len(grid), 5):
        concatenated_letter = ""

        for y in range(len(grid[0])):
            for x in range(5):
                concatenated_letter += grid[start_col + x][y]

        found = False
        for letter, letter_pattern in letters.items():
            if concatenated_letter == letter_pattern:
                found = True
                result += letter
                break
            
        if not found:
            result += "?"

    return result