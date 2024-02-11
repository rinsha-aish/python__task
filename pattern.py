def print_hexagon(rows, cols):
    for i in range(rows):
        if i % 2 == 0:
            top_row = " " * (rows - i - 1) * 3 + " ___" * (cols // 2)
            mid_row = "/   \\___/" * (cols // 2)
            print(top_row)
            print(mid_row)
        else:
            mid_row = "\\___/     " * (cols // 2)
            bottom_row = " " * (rows - i - 1) * 3 + "\\___/" * (cols // 2)
            print(mid_row)
            print(bottom_row)

# user input for rows and columns
rows, cols = map(int, input("Input:- ").split())

# Function calling
print_hexagon(rows, cols)
