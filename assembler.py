registers = {"reg0":'000',
             "reg1":"001",
             "reg2":"010",
             "reg3":"011",
             "reg4":"100",
             "reg5":"101",
             "reg6":"110",
             "FLAG":"111"
             }

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
    variable[instruction[1]]="001000"
