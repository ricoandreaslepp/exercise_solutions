def fill_and_print(table, comps, output, first_line, second_line):
    
        first_letter = first_line[0]
        second_letter = first_line[3]
        third_letter = second_line[0]
        fourth_letter = second_line[3]
        first_operator = first_line[1:3]
        second_operator = second_line[1:3]
                     
        first_letter_pos = ord(first_letter)-ord('a')
        second_letter_pos = ord(second_letter)-ord('a')
        third_letter_pos = ord(third_letter)-ord('a')
        fourth_letter_pos = ord(fourth_letter)-ord('a')
        
        table[first_letter_pos][second_letter_pos] = first_operator
        table[third_letter_pos][fourth_letter_pos] = second_operator
        
        ans = True
        # a x b
        # a x c
        if (first_letter != third_letter and second_letter == fourth_letter):
            first_letter, second_letter = second_letter, first_letter
            first_operator = comps.get(first_operator)
            third_letter, fourth_letter = fourth_letter, third_letter
            second_operator = comps.get(second_operator)
            #output.write(first_letter + first_operator + second_letter + "\n")
            #output.write(third_letter + second_operator + fourth_letter + "\n")
            
            first_letter_pos = ord(first_letter)-ord('a')
            second_letter_pos = ord(second_letter)-ord('a')
            third_letter_pos = ord(third_letter)-ord('a')
            fourth_letter_pos = ord(fourth_letter)-ord('a')
            
        
        if (first_letter == third_letter and second_letter != fourth_letter):
            if (first_operator == '=='):
                table[second_letter_pos][fourth_letter_pos] = second_operator
            elif (second_operator == '=='):
                table[fourth_letter_pos][second_letter_pos] = first_operator
            elif (first_operator == '<<' and second_operator == '>>'):
                table[second_letter_pos][fourth_letter_pos] = second_operator
            elif (first_operator == '>>' and second_operator == '<<'):
                table[fourth_letter_pos][second_letter_pos] = comps.get(second_operator)
            elif (first_operator == '<<' and second_operator == '>='):
                table[fourth_letter_pos][second_letter_pos] = first_operator
            elif (first_operator == '<=' and second_operator == '>>'):
                table[fourth_letter_pos][second_letter_pos] = comps.get(second_operator)
            elif (first_operator == '>=' and second_operator == '<<'):
                table[second_letter_pos][fourth_letter_pos] = second_operator
            elif (first_operator == '<<' and second_operator == '>='):
                table[fourth_letter_pos][second_letter_pos] = first_operator 
            elif (first_operator == '>>' and second_operator == '<='):
                table[fourth_letter_pos][second_letter_pos] = first_operator
            elif (first_operator == '<=' and second_operator == '>>'):
                table[fourth_letter_pos][second_letter_pos] = comps.get(second_operator)
            elif (first_operator == '<=' and second_operator == '>='):
                table[fourth_letter_pos][second_letter_pos] = second_operator
            elif (first_operator == '>=' and second_operator == '<='):
                table[fourth_letter_pos][second_letter_pos] = comps.get(second_operator)
                
            
                
        # final fill
        if (table[0][1] != '??'):
            table[1][0] = comps.get(table[0][1])
        else:
            table[0][1] = comps.get(table[1][0])
            
        if (table[0][2] != '??'):
            table[2][0] = comps.get(table[0][2])
        else:
            table[0][2] = comps.get(table[2][0])
            
        if (table[1][2] != '??'):
            table[2][1] = comps.get(table[1][2])
        else:
            table[1][2] = comps.get(table[2][1])
        
        if (ans):
            for line in table:
                for word in line:
                    output.write(str(word) + ' ')
                output.write("\n")
        else:
            #output.write("VASTUOLU filler\n")
            output.write("VASTUOLU")

def solve(first_line, second_line, output):
    
    table = [['==', '??', '??'],
             ['??', '==', '??'],
             ['??', '??', '==']]
    
    comps = {'<=' : '>=',
             '>=' : '<=',
             '<<' : '>>',
             '>>' : '<<',
             '==' : '==',
             '??' : '??'
            }
    
    first_letter = first_line[0]
    second_letter = first_line[3]
    third_letter = second_line[0]
    fourth_letter = second_line[3]
    first_operator = first_line[1:3]
    second_operator = second_line[1:3]
    #output.write(first_letter + second_letter +third_letter+fourth_letter+"\n")
    #output.write(first_operator+second_operator+"\n")
    
    # normaalkuju
    if (first_letter == fourth_letter or second_letter == third_letter):
        second_line = (fourth_letter + comps.get(second_operator) + third_letter)
        fourth_letter, third_letter = third_letter, fourth_letter
        second_operator = comps.get(second_operator)    
            
    first_letter_pos = ord(first_letter)-ord('a')
    second_letter_pos = ord(second_letter)-ord('a')
    third_letter_pos = ord(third_letter)-ord('a')
    fourth_letter_pos = ord(fourth_letter)-ord('a')


    # initial check for false inputs assuming it's true
    answer = True
    if (first_letter == second_letter):
        if (first_operator != '==' and first_operator != '<=' and first_operator != '>='):
            answer = False
        else:
            first_operator = '=='
    
    if (third_letter == fourth_letter):
        if (second_operator != '==' and second_operator != '<=' and second_operator != '>='):
            answer = False
        else:
            second_operator = '=='
            
    if (first_letter == third_letter and second_letter == fourth_letter):
        
        if (first_operator != second_operator):
            # priorities or false
            if (first_operator == '<<' and second_operator == '<='):
                second_operator = first_operator
            elif (second_operator == '<<' and first_operator == '<='):
                first_operator = second_operator
            elif (first_operator == '>>' and second_operator == '>='):
                second_operator == first_operator
            elif (second_operator == '>>' and first_operator == '>='):
                first_operator == second_operator
            elif (first_operator == '==' and (second_operator == '<=' or second_operator == '>=')):
                  second_operator = first_operator
            elif (second_operator == '==' and (first_operator == '<=' or first_operator == '>=')):
                  first_operator == second_operator
            elif ((first_operator == '<=' or first_operator == '>=') and (second_operator == '<=' or second_operator == '>=')):
                first_operator = '=='
                second_operator = '=='
            else:
                answer = False
                #output.write("FOUND\n")
                
    # final init of first and second line
    first_line = (first_letter + first_operator + second_letter)
    second_line = (third_letter + second_operator + fourth_letter)
    #output.write(first_line + " " + second_line + "\n")
    # final check
    if (not answer):
        #output.write("VASTUOLU answer")
        output.write("VASTUOLU")
    else:
        # siia peaksid jõudma ainult normaalkujul olevad avaldised
        fill_and_print(table, comps, output, first_line, second_line)

# files
output = open("seosval.txt", "w")
#file = open("seose_variandid.txt", "r")

#output = open("seosout.txt", "w")
file = open("seossis.txt", "r")
'''
# testing code
i = 1
for line in file.read().split("----"):
    first_line = line.strip()[0:4]
    second_line = line.strip()[5:9]
    output.write(first_line + " " + second_line + "\n")
    solve(first_line, second_line, output)
    output.write("\n" + str(i) + "\n----\n")
    i += 1
output.close()
'''
# actual code
lines = file.read().split("\n")
first_line = lines[0][0:4]
second_line = lines[1][0:4]
print(first_line, second_line)
solve(first_line, second_line, output)
output.close()
