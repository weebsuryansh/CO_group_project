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

def opcode6(instruction):
    x=str(instruction[2])
    print("00101"+"0"+registers[instruction[1]]+x)

def opcode7(instruction):
    print("00110"+"00"+registers[instruction[1]]+registers[instruction[2]]+registers[instruction[3]])

def opcode8(instruction):
    print("00111"+"00000"+registers[instruction[1]]+registers[instruction[2]])

def opcode9(instruction):
    x=int(instruction[2][1:])
    x=bin(x)
    x=x[2:]
    if(len(x)>7):
        pass
    else:
        x=x.zfill(7)
    print("01000"+"0"+registers[instruction[1]]+x)

def opcode10(instruction):
    x=int(instruction[2][1:])
    x=bin(x)
    x=x[2:]
    if(len(x)>7):
        pass
    else:
        x=x.zfill(7)
    print("01001"+"0"+registers[instruction[1]]+x)

def opcode11(instruction):
    print("01010"+"00"+registers[instruction[1]]+registers[instruction[2]]+registers[instruction[3]])

def opcode12(instruction):
    print("01011"+"00"+registers[instruction[1]]+registers[instruction[2]]+registers[instruction[3]])

def opcode13(instruction):
    print("01100"+"00"+registers[instruction[1]]+registers[instruction[2]]+registers[instruction[3]])

def opcode14(instruction):
    print("01101"+"00000"+registers[instruction[1]]+registers[instruction[2]])

def opcode15(instruction):
    print("01110"+"00000"+registers[instruction[1]]+registers[instruction[2]])
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
    x = list(i.split())
    if(x[0]=="var"):
        opcode1(x)
    if(x[0]=="add"):
        opcode2(x)
    if(x[0]=="sub"):
        opcode3(x)
    if(x[0]=="mov"):
        opcode4(x)
    if(x[0]=="mov" and x[2][0:3]=="reg"):
        opcode5(x)
    if(x[0]=="ld"):
        opcode6(x)
    if(x[0]=="st"):
        opcode7(x)
    if(x[0]=="mul"):
        opcode8(x)
    if(x[0]=="div"):
        opcode9(x)
    if(x[0]=="rs"):
        opcode10(x)
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
        opcode16(x)
    if(x[0]=="jlt"):
        opcode17(x)
    if(x[0]=="jgt"):
        opcode18(x)
    if(x[0]=="je"):
        opcode19(x)
    if(x[0]=="hlt"):
        opcode20(x)

