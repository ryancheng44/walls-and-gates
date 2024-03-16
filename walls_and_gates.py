# (I only know how to run Python code on Mac) Open the Terminal app, 
# and make your way to the directory in which this file is located
# using the commands "ls" and "cd", then run this using the command
# "python3 (this file name)"

example_input_1 = [[2147483647, -1, 0, 2147483647], [2147483647, 2147483647, 2147483647, -1], 
                   [2147483647, -1, 2147483647, -1], [0, -1, 2147483647, 2147483647]]
example_input_2 = [[-1]]
sample_input = [[0, -1], [2147483647, 0]]

def solve(input):
    for i in range(len(input)):
        for j in range(len(input[i])):
            if input[i][j] == 0:
                fill(input, i, j, 1)
    return input

def fill(input, i, j, distance_to_nearest_gate):
    if i + 1 < len(input):
        if distance_to_nearest_gate < input[i+1][j]:
            input[i+1][j] = distance_to_nearest_gate
            fill(input, i+1, j, distance_to_nearest_gate + 1)
    if i - 1 >= 0:
        if distance_to_nearest_gate < input[i-1][j]:
            input[i-1][j] = distance_to_nearest_gate
            fill(input, i-1, j, distance_to_nearest_gate + 1)
    if j + 1 < len(input[i]):
        if distance_to_nearest_gate < input[i][j+1]:
            input[i][j+1] = distance_to_nearest_gate
            fill(input, i, j+1, distance_to_nearest_gate + 1)
    if j - 1 >= 0:
        if distance_to_nearest_gate < input[i][j-1]:
            input[i][j-1] = distance_to_nearest_gate
            fill(input, i, j-1, distance_to_nearest_gate + 1)

def main():
    print(solve(example_input_1))
    print(solve(example_input_2))
    print(solve(sample_input))

if __name__ == "__main__":
    main()