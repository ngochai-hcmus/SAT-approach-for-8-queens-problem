#Task C (write rule CNF clauses)

file_name_output1 = "ruleLevel1_taskC.txt"
fout1 = open(file_name_output1, "w")

file_name_output2 = "ruleLevel2_taskC.txt"
fout2 = open(file_name_output2, "w")

sentences_level1 = [] #row + diagonal
sentences_level2 = [] #row + column + diagonal

def sentences_row(row:int):
  temp = ''
  for i in range (0, 8):
    temp = temp + 'b[' + str(row) + '][' + str(i) + ']'
    if(i!=7):
      temp = temp + ' v '
  sentences_level1.append(temp)
  sentences_level2.append(temp)
  for i in range(0, 8):
    for j in range(i + 1, 8):
      temp = 'not(b[' + str(row) + '][' + str(i) + ']) v not(b[' + str(row) + '][' + str(j) + '])'
      sentences_level1.append(temp)
      sentences_level2.append(temp)

def sentences_col(col:int):
  temp = ''
  for i in range (0, 8):
    temp = temp + 'b[' + str(i) + '][' + str(col) + ']'
    if(i!=7):
      temp = temp + ' v '
  sentences_level2.append(temp)
  for i in range(0, 8):
    for j in range(i + 1, 8):
      temp = 'not(b[' + str(i) + '][' + str(col) + ']) v not(b[' + str(j) + '][' + str(col) + '])'
      sentences_level2.append(temp)

def sentences_diagonal():
  for i in range(0, 8):
    for j in range (0, 8):
      x = i + 1
      y = j + 1
      while (x>=0 and x<8 and y>=0 and y<8):
        temp = 'not(b[' + str(i) + '][' + str(j) + ']) v not(b[' + str(x) + '][' + str(y) + '])'
        sentences_level1.append(temp)
        sentences_level2.append(temp)
        x = x + 1
        y = y + 1
      
      x = i + 1
      y = j - 1
      while (x>=0 and x<8 and y>=0 and y<8):
        temp = 'not(b[' + str(i) + '][' + str(j) + ']) v not(b[' + str(x) + '][' + str(y) + '])'
        sentences_level1.append(temp)
        sentences_level2.append(temp)
        x = x + 1
        y = y - 1

for i in range(0, 8):
  sentences_row(i)
for i in range(0, 8):
  sentences_col(i)
sentences_diagonal()

for sentence in sentences_level1:
  fout1.write(str(sentence) + '\n')

for sentence in sentences_level2:
  fout2.write(str(sentence) + '\n')

fout1.close()
fout2.close()


#Task C (translate)
file_name_input = "ruleLevel2_taskC.txt"
fin = open(file_name_input, "r")

file_name_output = "solution_taskC.txt"
fout = open(file_name_output, "w")

value_file = fin.read().split('\n')

res_line = ""
number = -1
check = 0

for value_line in value_file:
  for val in value_line:
    if val == 'n':
      res_line = res_line + '-'
    elif val == 'v':
      res_line = res_line + ' v '
    elif val>='0' and val <='9' and number == -1:
      number = int(val) * 8
      check = check + 1
    elif val>='0' and val <='9' and number != -1:
      number = number + int(val) + 1
      check = check + 1
    elif val == ']' and check == 2:
      res_line = res_line + str(number)
      number = -1
      check = 0
  res_line = res_line + '\n'
  fout.write(res_line)
  res_line = ''
  
fout.close()