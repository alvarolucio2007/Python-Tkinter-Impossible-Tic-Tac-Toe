import grid


def detect_win(grid):
    def detect_for(x):
        # checking every row
        for row in grid:
            count = 0
            for item in row:
                # print('hi', item)
                if item == x:
                    count += 1
            if count == 3:
                return True
        # checking every column
        for j in range(3):
            count = 0
            for i in range(3):
                if grid[i][j] == x:
                    count += 1
            if count == 3:
                return True
        # Checking diagonal i
        count = 0
        for i in range(3):
            if grid[i][i] == x:
                count += 1
        if count == 3:
            return True
        # checking the other diagonal(I want to die)
        count = 0
        for i in range(3):
            if grid[i][2 - i] == x:
                count += 1
        if count == 3:
            return True

    if detect_for(grid.key.get("x")):
        # print('X winss')
        return "x"
    if detect_for(grid.key.get("o")):
        # print('O winss')
        return "o"
    # print(f"X: {detect_for(key.get('x'))}, O: {detect_for(key.get('o'))}")


def detect_draw(grid_2):
    for i in grid_2:
        for j in i:
            if j == grid.key.get("blank"):
                return False

    return True
