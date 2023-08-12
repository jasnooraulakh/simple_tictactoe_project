# write your code here

print("X O X")
print("O X O")
print("X X O")


def print_pattern(symbol_string):
    print("---------")
    for i in range(0, 9, 3):
        print(f"| {symbol_string[i]} {symbol_string[i+1]} {symbol_string [i+2]} |")
    print("---------")


symbol_sequence = input()
print_pattern(symbol_sequence)
