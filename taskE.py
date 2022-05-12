from operator import mod
from attr import has
from queue import PriorityQueue

class State:
    def __init__(self, queens: list):
        self.queens = queens.copy()
        self.board = [[False]*8 for i in range(0, 8)]
        for coordinate in queens:
            row = coordinate[0]
            col = coordinate[1]
            self.board[row][col] = True

    def get_hash_code(self):
        hash_code = 0
        for i in range(0, 8):
            for j in range(0, 8):
                hash_code = hash_code*2 + int(self.board[i][j])
        return hash_code

    def get_path_cost(self):
        return len(self.queens)
    
    def __lt__(self, other):
        this_funtion = self.get_path_cost() + self.heuristic_value()
        other_funtion = other.get_path_cost() + other.heuristic_value()

        return this_funtion < other_funtion
    
    def __repr__(self):
      return '{}'.format(self.get_hash_code())

    def is_attack(self, coordinate: tuple):
        row = coordinate[0]
        col = coordinate[1]

        #check row
        for i in range(0, 8):
            if self.board[row][i] and i != col:
                return True
        
        #check column
        for i in range(0, 8):
            if self.board[i][col] and i != row:
                return True

        #check diagonals
        for i in range(-8, 8):
            x = row + i
            y = col + i
            if x >= 0 and x < 8 and y >= 0 and y < 8 and i != 0:
                if self.board[x][y]:
                    return True
      
            x = row - i
            y = col + i
            if x >= 0 and x < 8 and y >= 0 and y < 8 and i != 0:
                if self.board[x][y]:
                    return True
        return False

    def add_queen(self, coordinate: tuple):
        row = coordinate[0]
        col = coordinate[1]
        if self.board[row][col] or self.is_attack((row, col)):
            return False
        self.queens.append((row, col))
        self.board[row][col] = True
        return True

    def heuristic_value(self):
        value = 0
        for i in range(0, 8):
            for j in range(0, 8):
                if not self.is_attack((i, j)) and not self.board[i][j]:
                    value = value + 1
        return value

    def is_goal(self):
        if len(self.queens) != 8:
            return False
        for i in range(0, 8):
            for j in range(0, 8):
                if self.board[i][j] and self.is_attack((i, j)):
                    return False
        return True
    def __str__(self):
        line = ''
        for coordinate in self.queens:
            line += str(coordinate) + ' '
        return line
        
def A_star(queens):
    start = State(queens)
    frontier = PriorityQueue()
    explored = []
    
    frontier.put(start)
    explored.append(start.get_hash_code())
    
    while not frontier.empty():
        node = frontier.get()
        if node.is_goal():
            return node
        
        for i in range(0, 8):
            for j in range(0, 8):
                temp_node = State(node.queens)
                if temp_node.add_queen((i, j)):
                    if not temp_node.get_hash_code() in explored:
                        frontier.put(temp_node)
                        explored.append(temp_node.get_hash_code())
    return None

solution = []

fin = open("problem_taskE.txt", "r")
number_queens = fin.readline()
value_file = fin.readline().split(' ')

for value_line in value_file:
    value_line = value_line.strip('(')
    value_line = value_line.strip(')')
    value = tuple(map(int, value_line.split(',')))
    solution.append(value)


solver = A_star(solution)
print(solver)
