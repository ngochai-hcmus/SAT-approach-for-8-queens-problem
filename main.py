import tkinter
import taskF
import UI
from tkinter import simpledialog


if __name__ == '__main__':
    application_window = tkinter.Tk()
    application_window.withdraw()
    file_name = simpledialog.askstring("Input", "Please type your file name?", parent=application_window)

    queens = []

    fin = open(file_name, "r")
    number_queens = fin.readline()
    value_file = fin.readline().split(' ')

    for value_line in value_file:
        value_line = value_line.strip('(')
        value_line = value_line.strip(')')
        value = tuple(map(int, value_line.split(',')))
        queens.append(value)

    solver = taskF.A_star(queens)
    UI.chess_game(solver)
    
