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

abc=0

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
