registers = {"reg0":'000',
             "reg1":"001",
             "reg2":"010",
             "reg3":"011",
             "reg4":"100",
             "reg5":"101",
             "reg6":"110",
             "FLAG":"111"
             }

labels={"label1":"0001101",
        "label2":"0001000",
        "label3":"0001100",
        "label4":"0001110"}

variable = {}



def opcode1(instruction):
    print("00000"+"00"+registers[instruction[1]]+registers[instruction[2]]+registers[instruction[3]])

def opcode2(instruction):
    print("00001"+"00"+registers[instruction[1]]+registers[instruction[2]]+registers[instruction[3]])

def opcode3(instruction):
    x=int(instruction[2][1:])
    x=bin(x)
    x=x[2:]
    if(len(x)>7):
        pass
    else:
        x=x.zfill(7)
    print("00010"+"0"+registers[instruction[1]]+x)

def opcode4(instruction):
    print("00010"+"00000"+registers[instruction[1]]+registers[instruction[2]])

def opcode5(instruction):
    print("00100"+"0"+registers[instruction[1]]+"")
    #complete the print statement.

def opcode(instruction):
    variable[instruction[1]]="001000"

#space for opcodes of between

def opcode16(instruction):
    print("01111"+"0000"+labels[instruction[1]])

def opcode17(instruction):
    print("11100"+"0000"+labels[instruction[1]])

def opcode18(instruction):
    print("11101"+"0000"+labels[instruction[1]])

def opcode19(instruction):
    print("11111"+"0000"+labels[instruction[1]])

def opcode20():
    print("11010"+"00000000000")
 

program = open("")
program = program.readlines()

for i in program:
    x = i.split()
    if(x[0]=="var"):
        pass
    if(x[0]=="add"):
        pass
    if(x[0]=="sub"):
        pass
    if(x[0]=="mov"):
        pass
    if(x[0]=="mov" and x[2][0:3]=="reg"):
        pass
    if(x[0]=="ld"):
        pass
    if(x[0]=="st"):
        pass
    if(x[0]=="mul"):
        pass
    if(x[0]=="div"):
        pass
    if(x[0]=="rs"):
        pass
    if(x[0]=="ls"):
        pass
    if(x[0]=="xor"):
        pass
    if(x[0]=="or"):
        pass
    if(x[0]=="and"):
        pass
    if(x[0]=="not"):
        pass
    if(x[0]=="cmp"):
        pass
    if(x[0]=="jlt"):
        pass
    if(x[0]=="jgt"):
        pass
    if(x[0]=="je"):
        pass
    if(x[0]=="hlt"):
        pass

