#Task D
import numpy as np
from pysat.solvers import Glucose3

clauses = []

def clauses_row(row:int):
  temp = []
  for i in range (0, 8):
    temp.append(row * 8 + i + 1)
  clauses.append(temp)
  for i in range(0, 8):
    for j in range(i + 1, 8):
      clauses.append([-(row * 8 + i + 1), -(row * 8 + j + 1)])

def clauses_col(col:int):
  temp = []
  for i in range (0, 8):
    temp.append(i * 8 + col + 1)
  clauses.append(temp)
  for i in range(0, 8):
    for j in range(i + 1, 8):
      clauses.append([-(i * 8 + col + 1), -(j * 8 + col + 1)])

def clauses_diagonal():
  for i in range(0, 8):
    for j in range (0, 8):
      x = i + 1
      y = j + 1
      while (x>=0 and x<8 and y>=0 and y<8):
        clauses.append([-(i * 8 + j + 1), -(x * 8 + y + 1)])
        x = x + 1
        y = y + 1
      
      x = i + 1
      y = j - 1
      while (x>=0 and x<8 and y>=0 and y<8):
        clauses.append([-(i * 8 + j + 1), -(x * 8 + y + 1)])
        x = x + 1
        y = y - 1

for i in range(0, 8):
  clauses_row(i)
for i in range(0, 8):
  clauses_col(i)
clauses_diagonal()

file_name_output1 = "/home/problem_taskD.txt"
fout1 = open(file_name_output1, "w")

file_name_output2 = "/home/solution_taskD.txt"
fout2 = open(file_name_output2, "w")

g = Glucose3()
for val in clauses:
  g.add_clause(val)

g.solve(assumptions=[2])

fout2.write('v ')
for val in g.get_model():
  fout2.write(str(val))
  fout2.write(' ')
fout2.write('0')

fout1.write('p ' + 'cnf ' + str(g.nof_vars()) + ' ' + str(g.nof_clauses()) + '\n')

for val in clauses:
  for i in range(0, len(val)):
    if i != 0:
      fout1.write(' ')
    fout1.write(str(val[i]))
  fout1.write(' 0 \n')

fout1.close()
fout2.close()