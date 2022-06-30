import os

os.chdir(os.getcwd() + "\\ratsu_input")
inputf = open("input0.txt", "r")
outputf = open("ratsuval.txt", "w")

# tavalise ratsu käigud
# . * . * .
# * . . . *
# . . @ . .
# * . . . *
# . * . * .

rows, columns = 0, 0

def create_table(file):
    
    lines = file.readlines()
    first_line = lines[0].strip().split(" ")
    
    global rows, columns
    rows = first_line[0]
    columns = first_line[1]
    
    
create_table(inputf)
outputf.close()
