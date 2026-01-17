import tkinter


# declaring globals
display, root, key, grid, flag = [1] * 5
checked = [0, 0, 0]
inputs = [1, 1, -1]
first_move = False
moves_first = 0


def init():
    display, root, key, grid, flag = [1] * 5

    first_move = False

    print("with", inputs)

    display = []
    root = tkinter.Tk()
    key = {"blank": "  ", "x": "X", "o": "O"}
    grid = [
        [key.get("blank"), key.get("blank"), key.get("blank")],
        [key.get("blank"), key.get("blank"), key.get("blank")],
        [key.get("blank"), key.get("blank"), key.get("blank")],
    ]
    flag = 1
