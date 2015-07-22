def count_neighbours(grid, row, col):
    max_row = len(grid) - 1
    max_col = len(grid[0]) - 1
    count = 0

    # top left
    if row-1 >= 0 and col-1 >= 0 and grid[row-1][col-1] == 1:
        count = count + 1
    # top middle
    if row-1 >= 0 and grid[row-1][col] == 1:
        count = count + 1
    # top right
    if row-1 >= 0 and col+1 <= max_col and grid[row-1][col+1] == 1:
        count = count + 1
    # middle left
    if col-1 >= 0 and grid[row][col-1] == 1:
        count = count + 1
    # middle right
    if col+1 <= max_col and grid[row][col+1] == 1:
        count = count + 1
    # bottom left
    if row+1 <= max_row and col-1 >= 0 and grid[row+1][col-1] == 1:
        count = count + 1
    # bottom middle
    if row+1 <= max_row and grid[row+1][col] == 1:
        count = count + 1
    # bottom right
    if row+1 <=max_row and col+1 <= max_col and grid[row+1][col+1] == 1:
        count = count + 1

    return count
