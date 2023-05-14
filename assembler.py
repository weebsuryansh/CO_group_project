

registers = {"R0":'000',
             "R1":"001",
             "R2":"010",
             "R3":"011",
             "R4":"100",
             "R5":"101",
             "R6":"110",
             "FLAG":"111"
             }


labels={}

variable ={}

register_name =["R0","R1","R2","R3","R4","R5","R6"]

def opcode0(instruction):
    y=bin(F2+1)
    y=int(y[2:])
    y=y.zfill(7)
    variable[instruction[1]]=str(y)


def opcode1(instruction):
    if(instruction[1] not in register_name):
        output_program.write("illegal register name")
        quit()
    elif(instruction[2] not in register_name):
        output_program.write("illegal register name")
        quit()
    elif(instruction[3] not in register_name):
        output_program.write("illegal register name")
        quit()
    else:
        global output_string
        output_string += "00000"+"00"+registers[instruction[1]]+registers[instruction[2]]+registers[instruction[3]]+"\n"

def opcode2(instruction):
    if(instruction[1] not in register_name):
        output_program.write("illegal register name")
        quit()
    elif(instruction[2] not in register_name):
        output_program.write("illegal register name")
        quit()
    elif(instruction[3] not in register_name):
        output_program.write("illegal register name")
        quit()
    else:
        global output_string
        output_string+=("00001"+"00"+registers[instruction[1]]+registers[instruction[2]]+registers[instruction[3]]+"\n")

def opcode3(instruction):
    if(instruction[1] not in register_name):
        output_program.write("illegal register name")
        quit()

    x=int(instruction[2][1:])
    if(x<0):
        output_program.write("invalid immediate value")
        quit()
    x=bin(x)
    x=x[2:]
    if(len(x)>7):
        output_program.write("illegal immediate value")
        quit()
    else:
        x=x.zfill(7)
    global output_string
    output_string+=("00010"+"0"+registers[instruction[1]]+x+"\n")

def opcode4(instruction):
    if(instruction[1] not in register_name):
        output_program.write("illegal register name")
        quit()
    elif(instruction[2] not in register_name):
        output_program.write("illegal register name")
        quit()
    else:
        output_string+=("00010"+"00000"+registers[instruction[1]]+registers[instruction[2]]+"\n")

def opcode5(instruction):
    if(instruction[1] not in register_name):
        print("illegal register name")
        quit()
    else:
        
        output_string+=("00100"+"0"+registers[instruction[1]]+variable[instruction[2]]+"\n")
    #complete the print statement.

def opcode6(instruction):
    if(instruction[1] not in register_name):
        output_program.write("invalid register name")
        quit()
    else:
        global output_string
        output_string+=("00101"+"0"+registers[instruction[1]]+variable[instruction[2]]+"\n")

def opcode7(instruction):
    if(instruction[1] not in register_name):
        output_program.write("illegal register name")
        quit()
    elif(instruction[2] not in register_name):
        output_program.write("illegal register name")
        quit()
    elif(instruction[3] not in register_name):
        output_program.write("illegal register name")
        quit()
    else:
        global output_string
        output_string+=("00110"+"00"+registers[instruction[1]]+registers[instruction[2]]+registers[instruction[3]]+"\n")

def opcode8(instruction):
    if(instruction[1] not in register_name):
        output_program.write("illegal register name")
        quit()
    elif(instruction[2] not in register_name):
        output_program.write("illegal register name")
        quit()
    else:
        global output_string
        output_string+=("00111"+"00000"+registers[instruction[1]]+registers[instruction[2]]+"\n")

def opcode9(instruction):
    if(instruction[1] not in register_name):
        output_program.write("illegal register name")
        quit()
    else:
        x=int(instruction[2][1:])
        x=bin(x)
        x=x[2:]
        if(len(x)>7):
            output_program.write("illegal immediate value")
            quit()
        else:
            x=x.zfill(7)
            global output_string
            output_string+=("01000"+"0"+registers[instruction[1]]+x+"\n")

def opcode10(instruction):
    x=int(instruction[2][1:])
    x=bin(x)
    x=x[2:]
    if(len(x)>7):
        output_program.write("illegal immediate value")
        quit()
    else:
        x=x.zfill(7)
        if(instruction[1] not in register_name):
            output_program.write("illegal register name")
            quit()
        else:
           global output_string
           output_string+=("01001"+"0"+registers[instruction[1]]+x+"\n")
    
def opcode11(instruction):
    if(instruction[1] not in register_name):
        output_program.write("illegal register name")
        quit()
    elif(instruction[2] not in register_name):
        output_program.write("illegal register name")
        quit()
    elif(instruction[3] not in register_name):
        output_program.write("illegal register name")
        quit()
    else:
        global output_string
        output_string+=("01010"+"00"+registers[instruction[1]]+registers[instruction[2]]+registers[instruction[3]]+"\n")

def opcode12(instruction):
    if(instruction[1] not in register_name):
        output_program.write("illegal register name")
        quit()
    elif(instruction[2] not in register_name):
        output_program.write("illegal register name")
        quit()
    elif(instruction[3] not in register_name):
        output_program.write("illegal register name")
        quit()
    else:
        global output_string
        output_string+=("01011"+"00"+registers[instruction[1]]+registers[instruction[2]]+registers[instruction[3]]+"\n")

def opcode13(instruction):
    if(instruction[1] not in register_name):
        output_program.write("illegal register name")
        quit()
    elif(instruction[2] not in register_name):
        output_program.write("illegal register name")
        quit()
    elif(instruction[3] not in register_name):
        output_program.write("illegal register name")
        quit()
    else:
        global output_string
        output_string+=("01100"+"00"+registers[instruction[1]]+registers[instruction[2]]+registers[instruction[3]]+"\n")


def opcode14(instruction):
    if(instruction[1] not in register_name):
        output_program.write("illegal register name")
        quit()
    elif(instruction[2] not in register_name):
        output_program.write("illegal register name")
        quit()
    else:
        global output_string
        output_string+=("01101"+"00000"+registers[instruction[1]]+registers[instruction[2]]+"\n")

def opcode15(instruction):
    if(instruction[1] not in register_name):
        output_program.write("illegal register name")
        quit()
    elif(instruction[2] not in register_name):
        output_program.write("illegal register name")
        quit()
    else:
        global output_string
        output_string+=("01110"+"00000"+registers[instruction[1]]+registers[instruction[2]]+"\n")

def opcode16(instruction):
    if instruction[1] not in labels.keys():
        print("Error 404, label doesn't exist.")
        return
    else:
        print("01111"+"0000"+labels[instruction[1]])

def opcode17(instruction):
    if instruction[1] not in labels.keys():
        print("Error 404, label doesn't exist.")
        return
    else:
        print("11100"+"0000"+labels[instruction[1]])

def opcode18(instruction):
    if instruction[1] not in labels.keys():
        print("Error 404, label doesn't exist.")
        return
    else:
        print("11101"+"0000"+labels[instruction[1]])

def opcode19(instruction):
    if instruction[1] not in labels.keys():
        print("Error 404, label doesn't exist.")
        return
    else:
        print("11111"+"0000"+labels[instruction[1]])

def opcode20(instruction):
    global output_string
    output_string+=("11010"+"00000000000")
 

program1 = open("input.txt")
program = program1.readlines()
for i in range(len(program)):
    if(program[i]=="\n"):
        program.pop(i)

no_of_instruction = len(program)

output_string= ""
output_program = open("output.txt","w")


y=program[-1].split()
if(y[0]!='hlt'):
    print ("halt not last instruction ")
    quit()
number_of_instructions_run =0

F1=0
F2=0

for i in program:
    if(i[0]=='var'):
        F1+=1
    else:
        F2+=1




e0=0   #no of variable instruction
e1=0   #no of non variable instruction


for i in program:
    x = list(i.split())
    
    if(x[0]=="var"):
        opcode0(x)
        number_of_instructions_run+=1
        if(e1>0):
            output_program.write("variable declared at middle")
            quit()
        else:
            e0+=1
    elif(x[0]=="add"):
        opcode1(x)
        number_of_instructions_run+=1
        e1+=1

    elif(x[0]=="sub"):
        opcode2(x)
        number_of_instructions_run+=1
        e1+=1
    elif(x[0]=="mov"):
        opcode3(x)
        number_of_instructions_run+=1
        e1+=1
    elif(x[0]=="mov" and x[2][0:3]=="reg"):
        opcode4(x)
        number_of_instructions_run+=1
        e1+=1
    elif(x[0]=="ld"):
        opcode5(x)
        number_of_instructions_run+=1
        e1+=1
    elif(x[0]=="st"):
        opcode6(x)
        number_of_instructions_run+=1
        e1+=1
    elif(x[0]=="mul"):
        opcode7(x)
        number_of_instructions_run+=1
        e1+=1
    elif(x[0]=="div"):
        opcode8(x)
        number_of_instructions_run+=1
        e1+=1
    elif(x[0]=="rs"):
        opcode9(x)
        number_of_instructions_run+=1
        e1+=1
    elif(x[0]=="ls"):
        opcode10(x)
        number_of_instructions_run+=1
        e1+=1
    elif(x[0]=="xor"):
        opcode11(x)
        number_of_instructions_run+=1
        e1+=1
    elif(x[0]=="or"):
        opcode12(x)
        number_of_instructions_run+=1
        e1+=1
    elif(x[0]=="and"):
        opcode13(x)
        number_of_instructions_run+=1
        e1+=1
    elif(x[0]=="not"):
        opcode14(x)
        number_of_instructions_run+=1
        e1+=1
    elif(x[0]=="cmp"):
        opcode15(x)
        number_of_instructions_run+=1
        e1+=1
    elif(x[0]=="jmp"):
        opcode16(x)
        number_of_instructions_run+=1
        e1+=1
    elif(x[0]=="jlt"):
        opcode17(x)
        number_of_instructions_run+=1
        e1+=1
    elif(x[0]=="jgt"):
        opcode18(x)
        number_of_instructions_run+=1
        e1+=1
    elif(x[0]=="je"):
        opcode19(x)
        number_of_instructions_run+=1
        e1+=1
    elif(x[0]=="hlt"):
        opcode20(x)
        e1+=1
    else:
        print("syntax error")
        quit()
    
output_program.write(output_string)

output_program.close()
program1.close()
