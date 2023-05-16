registers = {"R0":'000',
             "R1":"001",
             "R2":"010",
             "R3":"011",
             "R4":"100",
             "R5":"101",
             "R6":"110",
             "FLAGS":"111"}

halts= 0 #no of halts in the code

numbering={}

labels={}

variable ={}

register_name =["R0","R1","R2","R3","R4","R5","R6"]
register_name0 =["R0","R1","R2","R3","R4","R5","R6","FLAGS"]

def opcode0(instruction):
    if(len(instruction)!=2):
        print(f"must contain 2 parameters only in line {number_of_instructions_run}")
        quit()
    y=F2 + len(variable)
    y=bin(y)
    y=y[2:]
    y=y.zfill(7)                                                                                              
    variable[instruction[1]]=str(y)

def opcode1(instruction):
    if(len(instruction)!=4):
        print(f"must contain 4 parameters only in line {number_of_instructions_run}")
        quit()
    if("FLAGS" in instruction):
        print(f"illegal use of flags in line {number_of_instructions_run}")
        quit() 
    if(instruction[1] not in register_name):
        print(f"illegal register name on line {number_of_instructions_run}")
        quit()
    elif(instruction[2] not in register_name):
        print(f"illegal register name on line {number_of_instructions_run}")
        quit()
    elif(instruction[3] not in register_name):
        print(f"illegal register name on line {number_of_instructions_run}")
        quit()
    else:
        global output_string
        output_string += "00000"+"00"+registers[instruction[1]]+registers[instruction[2]]+registers[instruction[3]]+"\n"

def opcode2(instruction):
    if(len(instruction)!=4):
        print(f"must contain 4 parameters only in line {number_of_instructions_run}")
        quit()
    if("FLAGS" in instruction):
        print(f"illegal use of flags in line {number_of_instructions_run}")
        quit() 
    if(instruction[1] not in register_name):
        print(f"illegal register name on line {number_of_instructions_run}")
        quit()
    elif(instruction[2] not in register_name):
        print(f"illegal register name on line {number_of_instructions_run}")
        quit()
    elif(instruction[3] not in register_name):
        print(f"illegal register name on line {number_of_instructions_run}")
        quit()
    else:
        global output_string
        output_string+=("00001"+"00"+registers[instruction[1]]+registers[instruction[2]]+registers[instruction[3]]+"\n")

def opcode3(instruction):
    if(len(instruction)!=3):
        print(f"must contain 3 parameters only in line {number_of_instructions_run}")
        quit()
    if("FLAGS" in instruction):
        print(f"illegal use of flags in line {number_of_instructions_run}")
        quit()
    if(instruction[1] not in register_name):
        print(f"illegal register name on line {number_of_instructions_run}")
        quit()
    y101=str(instruction[2][1:])
    if(y101.isnumeric()!=True):
        print(f"immediate value is not a integer value on line {number_of_instructions_run}")
        quit()
    if(float(instruction[2][1:])-int(float(instruction[2][1:]))!=0):                                                 
        print(f"immediate value is not a integer value on line {number_of_instructions_run}")
        quit()
    x=int(float(instruction[2][1:]))
    if(x<0):
        print(f"invalid immediate value on line {number_of_instructions_run}")
        quit()
    x=bin(x)
    x=x[2:]
    if(len(x)>7):
        print(f"illegal immediate value on line {number_of_instructions_run}")
        quit()
    else:
        x=x.zfill(7)
        global output_string
        output_string+=("00010"+"0"+registers[instruction[1]]+x+"\n")

def opcode4(instruction):
    if(len(instruction)!=3):
        print(f"must contain 3 parameters only in line {number_of_instructions_run}")
        quit()
    if(instruction[1] not in register_name0):
        print(f"illegal register name on line {number_of_instructions_run}")
        quit()
    elif(instruction[1] =="FLAGS"):
        print(f"illegal use of flag on line {number_of_instructions_run}")
        quit()
    elif(instruction[2] not in register_name0):
        print(f"illegal register name on line {number_of_instructions_run}")
        quit()
    else:
        global output_string                                                                                     
        output_string+=("00011"+"00000"+registers[instruction[1]]+registers[instruction[2]]+"\n")

def opcode5(instruction):
    if(len(instruction)!=3):
        print(f"must contain 3 parameters only  in line {number_of_instructions_run}")
        quit()
    if("FLAGS" in instruction):
        print(f"illegal use of flags in line {number_of_instructions_run}")
        quit() 
    if(instruction[1] not in register_name):
        print(f"illegal register name on line {number_of_instructions_run}")
        quit()
    elif(instruction[2] not in variable.keys()):
        print(f"Unnamed Variable on line {number_of_instructions_run}")
        quit()
    else:
        global output_string                                                                                        
        output_string+=("00100"+"0"+registers[instruction[1]]+variable[instruction[2]]+"\n")

def opcode6(instruction):
    if(len(instruction)!=3):
        print(f"must contain 3 parameters only in line {number_of_instructions_run}")
        quit()
    if("FLAGS" in instruction):
        print(f"illegal use of flags in line {number_of_instructions_run}")
        quit() 
    if(instruction[1] not in register_name):
        print(f"invalid register name on line {number_of_instructions_run}")
        quit()
    elif(instruction[2] not in variable.keys()):
        print(f"Unnamed Variable on line {number_of_instructions_run}")
        quit()
    else:
        global output_string
        output_string+=("00101"+"0"+registers[instruction[1]]+variable[instruction[2]]+"\n")

def opcode7(instruction):
    if(len(instruction)!=4):
        print(f"must contain 4 parameters only in line {number_of_instructions_run}")
        quit()
    if("FLAGS" in instruction):
        print(f"illegal use of flags in line {number_of_instructions_run}")
        quit() 
    if(instruction[1] not in register_name):
        print(f"illegal register name on line {number_of_instructions_run}")
        quit()
    elif(instruction[2] not in register_name):
        print(f"illegal register name on line {number_of_instructions_run}")
        quit()
    elif(instruction[3] not in register_name):
        print(f"illegal register name on line {number_of_instructions_run}")
        quit()
    else:
        global output_string
        output_string+=("00110"+"00"+registers[instruction[1]]+registers[instruction[2]]+registers[instruction[3]]+"\n")

def opcode8(instruction):
    if(len(instruction)!=3):
        print(f"must contain 3 parameters only in line {number_of_instructions_run}")
        quit()
    if("FLAGS" in instruction):
        print(f"illegal use of flags in line {number_of_instructions_run}")
        quit() 
    if(instruction[1] not in register_name):
        print(f"illegal register name on line {number_of_instructions_run}")
        quit()
    elif(instruction[2] not in register_name):
        print(f"illegal register name on line {number_of_instructions_run}")
        quit()
    else:
        global output_string
        output_string+=("00111"+"00000"+registers[instruction[1]]+registers[instruction[2]]+"\n")

def opcode9(instruction):
    if(len(instruction)!=3):
        print(f"must contain 3 parameters only in line {number_of_instructions_run}")
        quit()
    if("FLAGS" in instruction):
        print(f"illegal use of flags in line {number_of_instructions_run}")
        quit() 
    if(instruction[1] not in register_name):
        print(f"illegal register name on line {number_of_instructions_run}")
        quit()
    if(float(instruction[2][1:])-int(float(instruction[2][1:]))!=0):                                                
        print(f"invalid immediate value on line {number_of_instructions_run}")
        quit()
    x=int(float(instruction[2][1:]))
    if(x<0):
        print(f"invalid immediate value on line {number_of_instructions_run}")
        quit()
    x=bin(x)
    x=x[2:]
    if(len(x)>7):
        print(f"illegal immediate value on line {number_of_instructions_run}")
        quit()
    else:
        x=x.zfill(7)
        global output_string
        output_string+=("01000"+"0"+registers[instruction[1]]+x+"\n")

def opcode10(instruction):
    if(len(instruction)!=3):
        print(f"must contain 3 parameters only in line {number_of_instructions_run}")
        quit()
    if("FLAGS" in instruction):
        print(f"illegal use of flags in line {number_of_instructions_run}")
        quit() 
    if(instruction[1] not in register_name):
        print(f"illegal register name on line {number_of_instructions_run}")
        quit()
    if(float(instruction[2][1:])-int(float(instruction[2][1:]))!=0):                                                
        print(f"invalid immediate value on line {number_of_instructions_run}")
        quit()
    x=int(float(instruction[2][1:]))
    if(x<0):
        print(f"invalid immediate value on line {number_of_instructions_run}")
        quit()
    x=bin(x)
    x=x[2:]
    if(len(x)>7):
        print(f"illegal immediate value on line {number_of_instructions_run}")
        quit()
    else:
        x=x.zfill(7)
        global output_string
        output_string+=("01001"+"0"+registers[instruction[1]]+x+"\n")
    
def opcode11(instruction):
    if(len(instruction)!=4):
        print(f"must contain 4 parameters only in line {number_of_instructions_run}")
        quit()
    if("FLAGS" in instruction):
        print(f"illegal use of flags in line {number_of_instructions_run}")
        quit() 
    if(instruction[1] not in register_name):
        print(f"illegal register name on line {number_of_instructions_run}")
        quit()
    elif(instruction[2] not in register_name):
        print(f"illegal register name on line {number_of_instructions_run}")
        quit()
    elif(instruction[3] not in register_name):
        print(f"illegal register name on line {number_of_instructions_run}")
        quit()
    else:
        global output_string
        output_string+=("01010"+"00"+registers[instruction[1]]+registers[instruction[2]]+registers[instruction[3]]+"\n")

def opcode12(instruction):
    if(len(instruction)!=4):
        print(f"must contain 4 parameters only in line {number_of_instructions_run}")
        quit()
    if("FLAGS" in instruction):
        print(f"illegal use of flags in line {number_of_instructions_run}")
        quit() 
    if(instruction[1] not in register_name):
        print(f"illegal register name on line {number_of_instructions_run}")
        quit()
    elif(instruction[2] not in register_name):
        print(f"illegal register name on line {number_of_instructions_run}")
        quit()
    elif(instruction[3] not in register_name):
        print(f"illegal register name on line {number_of_instructions_run}")
        quit()
    else:
        global output_string
        output_string+=("01011"+"00"+registers[instruction[1]]+registers[instruction[2]]+registers[instruction[3]]+"\n")

def opcode13(instruction):
    if(len(instruction)!=4):
        print(f"must contain 4 parameters only in line {number_of_instructions_run}")
        quit()
    if("FLAGS" in instruction):
        print(f"illegal use of flags in line {number_of_instructions_run}")
        quit() 
    if(instruction[1] not in register_name):
        print(f"illegal register name on line {number_of_instructions_run}")
        quit()
    elif(instruction[2] not in register_name):
        print(f"illegal register name on line {number_of_instructions_run}")
        quit()
    elif(instruction[3] not in register_name):
        print(f"illegal register name on line {number_of_instructions_run}")
        quit()
    else:
        global output_string
        output_string+=("01100"+"00"+registers[instruction[1]]+registers[instruction[2]]+registers[instruction[3]]+"\n")


def opcode14(instruction):
    if(len(instruction)!=3):
        print(f"must contain 3 parameters only in line {number_of_instructions_run}")
        quit()
    if("FLAGS" in instruction):
        print(f"illegal use of flags in line {number_of_instructions_run}")
        quit() 
    if(instruction[1] not in register_name):
        print(f"illegal register name on line {number_of_instructions_run}")
        quit()
    elif(instruction[2] not in register_name):
        print(f"illegal register name on line {number_of_instructions_run}")
        quit()
    else:
        global output_string
        output_string+=("01101"+"00000"+registers[instruction[1]]+registers[instruction[2]]+"\n")

def opcode15(instruction):
    if(len(instruction)!=3):
        print(f"must contain 3 parameters only  in line {number_of_instructions_run}")
        quit()
    if("FLAGS" in instruction):
        print(f"illegal use of flags in line {number_of_instructions_run}")
        quit() 
    if(instruction[1] not in register_name):
        print(f"illegal register name on line {number_of_instructions_run}")
        quit()
    elif(instruction[2] not in register_name):
        print(f"illegal register name on line {number_of_instructions_run}")
        quit()
    else:
        global output_string
        output_string+=("01110"+"00000"+registers[instruction[1]]+registers[instruction[2]]+"\n")

def opcode16(instruction):
    if(len(instruction)!=2):
        print(f"must contain 4 parameters only  in line {number_of_instructions_run}")
        quit()
    if("FLAGS" in instruction):
        print(f"illegal use of flags in line {number_of_instructions_run}")
        quit() 
    if instruction[1] not in numbering.keys():
        print(f"label doesn't exist on line {number_of_instructions_run}")
        quit()
    else:
        global output_string
        z0=bin(numbering[instruction[1]])
        z0=z0[2:]
        z0=z0.zfill(7)
        output_string+=("01111"+"0000"+z0+"\n")

def opcode17(instruction):
    if(len(instruction)!=2):
        print(f"must contain 2 parameters only in line {number_of_instructions_run}")
        quit()
    if("FLAGS" in instruction):
        print(f"illegal use of flags in line {number_of_instructions_run}")
        quit() 
    if instruction[1] not in numbering.keys():
        print(f"label doesn't exist on line {number_of_instructions_run}")
        quit()
    else:
        global output_string
        z0=bin(numbering[instruction[1]])
        z0=z0[2:]
        z0=z0.zfill(7)
        output_string+=("11100"+"0000"+z0+"\n")

def opcode18(instruction):
    if(len(instruction)!=2):
        print(f"must contain 2 parameters only  in line {number_of_instructions_run}")
        quit()
    if("FLAGS" in instruction):
        print(f"illegal use of flags in line {number_of_instructions_run}")
        quit() 
    if instruction[1] not in numbering.keys():
        print(f"label doesn't exist on line {number_of_instructions_run}")
        quit()
    else:
        global output_string
        z0=bin(numbering[instruction[1]])
        z0=z0[2:]
        z0=z0.zfill(7)
        output_string+=("11101"+"0000"+z0+"\n")

def opcode19(instruction):
    if(len(instruction)!=2):
        print(f"must contain 2 parameters only in line {number_of_instructions_run}")
        quit()
    if("FLAGS" in instruction):
        print(f"illegal use of flags in line {number_of_instructions_run}")
        quit() 
    if instruction[1] not in numbering.keys():
        print(f"label doesn't exist on line {number_of_instructions_run}")
        quit()
    else:
        global output_string
        z0=bin(numbering[instruction[1]])
        z0=z0[2:]
        z0=z0.zfill(7)
        output_string+=("11111"+"0000"+z0+"\n")

def opcode20(instruction):
    if(len(instruction)!=1):
        print(f"must contain 1 parameters only in line {number_of_instructions_run}")
        quit()
    if("FLAGS" in instruction):
        print(f"illegal use of flags in line {number_of_instructions_run}")
        quit() 
    global output_string
    output_string+=("11010"+"00000000000")
 
p101=[]
program=[]
while True:
    try:
        n = input()
        n=str(n)
        program.append(n)
    except EOFError:
        break

for i in range(len(program)):
    if(program[i]!="\n"):
        l101=program[i].lstrip()
        p101.append(l101)
program= p101.copy()

no_of_instruction = len(program)                                                                                       

output_string= ""
                                                                                                                        
y=program[-1]
if("hlt" not in program[-1]):    ##i changed program[-1][-3:]="hlt" to this condition.
    print(f"halt not last instruction ")
    quit()

number_of_instructions_run =1

F1=0    #no of variable instruction
F2=0    #no of non variable instruction

for i in program:
    v101=i.split()
    if(v101[0]=='var'):
        F1+=1
    else:
        F2+=1

e0=0   #no of variable instruction
e1=0   #no of non variable instruction
operand=["var","add","sub","mov","ld","st","mul","div","rs","ls","xor","or","and","not","cmp","jmp","jlt","jgt","je","hlt"]
for i in range (0,len(program)):
    p102=program[i].split()
    p103=p102[0]
    if p103[-1]== ':':
        numbering[p103[:-1]]=int(i-F1)
for i in program:
    x = list(i.split())
    if(x[0][:-1] in numbering.keys()):
        x=x[1:]
    
    if(x[0]=="var"):
        opcode0(x)
        number_of_instructions_run+=1
        if(e1>0):
            print(f"variable declared at middle  on line {number_of_instructions_run}")
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
    elif(x[0]=="mov" and x[2][0]=="$"):
        opcode3(x)
        number_of_instructions_run+=1
        e1+=1
    elif(x[0]=="mov" and (x[2] in register_name or x[2]=="FLAGS")):                                                              
        opcode4(x)
        number_of_instructions_run+=1
        e1+=1
    elif(x[0]=="mov" and x[2][0]!="$"):
        print(f"invalid immediate value on line {number_of_instructions_run}")
        quit()
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
        halts+=1
        if (halts>1):
            print(f"Halt in Middle on line {number_of_instructions_run}")
            quit()
    elif (x[0] not in operand):
        print(f"invalid Operand on line {number_of_instructions_run}")
        quit()
    else:                                                  
        print(f"general syntax error on line {number_of_instructions_run}")
        number_of_instructions_run+=1
        e1+=1
        quit()
print(output_string)
