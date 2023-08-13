# write your code here

print("X O X")
print("O X O")
print("X X O")


def print_pattern(symbol_string):
    """Print the pattern"""
    print("---------")
    for i in range(0, 9, 3):
        print(f"| {symbol_string[i]} {symbol_string[i+1]} {symbol_string [i+2]} |")
    print("---------")


def game_mechanics(string_input):
    """Recognize pattern and determine result"""
    rows = [string_input[0:3], string_input[3:6], string_input[6:9]]
    columns = [string_input[0::3], string_input[1::3], string_input[2::3]]
    diagonals = [string_input[0::4], string_input[2:7:2]]

    winning_pattern = rows + columns + diagonals

    if "XXX" in winning_pattern and "OOO" in winning_pattern:
        print("Impossible")
    elif "OOO" in winning_pattern:
        print("O wins")
    elif "XXX" in winning_pattern:
        print("X wins")
    elif string_input.count("_") == 0:
        print("Draw")
    elif abs(str(rows).count("X") - str(rows).count("O")) > 1:
        print("Impossible")
    else:
        print("Game not finished")


symbol_sequence = input()
print_pattern(symbol_sequence)

game_mechanics(symbol_sequence)
