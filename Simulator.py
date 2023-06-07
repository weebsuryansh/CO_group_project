import struct
registers = {'000' :"R0",
             '001' :"R1",
             '010' :"R2",
             '011' :"R3",
             '100' :"R4",
             '101' :"R5",
             '110' :"R6",
             '111' :"FLAG"}
memory={}
Flags=""
dump_memory =[]
for i in range(128):
    dump_memory.append("0000000000000000")

def float_to_ieee_754(float_num):
    float_num=float(float_num)
    if float_num == 0:
        return '000' 
    abs_num = abs(float_num)
    bias = 3
    exponent = int(abs_num).bit_length() - 1 + bias
    mantissa = abs_num / (2 ** exponent)
    exponent_bits = format(exponent, '03b')
    mantissa_bits = format(int(mantissa * (2 ** 5)), '05b')
    ieee_754_bits = exponent_bits + mantissa_bits
    return str(ieee_754_bits).zfill(16)
def ieee_754_to_float(ieee_754_bits):
    ieee_754_bits = str(ieee_754_bits).zfill(8)
    exponent_bits = ieee_754_bits[:3]
    mantissa_bits = ieee_754_bits[3:]
    exponent = int(exponent_bits, 2)
    biased_exponent = exponent - 3
    mantissa = int(mantissa_bits, 2) / (2 ** 5)
    float_value = mantissa * (2 ** biased_exponent)
    return float(float_value)

def padding_zeros(x):
    return str(x).zfill(16)
def padding_zeros0(x):
    x= bin(x)
    x= str(x)
    x= x[2:]
    return str(x).zfill(16)

file_registers = {"R0" : "0000000000000000",
                  "R1" : "0000000000000000",
                  "R2" : "0000000000000000",
                  "R3" : "0000000000000000",
                  "R4" : "0000000000000000",
                  "R5" : "0000000000000000",
                  "R6" : "0000000000000000",
                  "FLAG" : "0000000000000000"}

def print_registers_program_counter():
    global program_counter
    temp = bin(program_counter)[2:]
    print(f"{temp.zfill(7)}        {file_registers['R0']} {file_registers['R1']} {file_registers['R2']} {file_registers['R3']} {file_registers['R4']} {file_registers['R5']} {file_registers['R6']} {file_registers['FLAG']}")

program_counter = 0

def opcode1(instruction):
    temp1=registers[instruction[7:10]]
    temp2=registers[instruction[10:13]]
    temp3=registers[instruction[13:16]]
    result = int(file_registers[temp2],2) + int(file_registers[temp3],2)
    if result <= 127 and result>= 0 :
        file_registers[temp1] = padding_zeros0(result)
        file_registers["FLAG"] = "0000000000000000"
        print_registers_program_counter()
    elif result>127 or result<0:
        file_registers[temp1] = padding_zeros0(0)
        file_registers["FLAG"] = "0000000000001000"
        print_registers_program_counter()
    global program_counter 
    program_counter += 1

def opcode2(instruction):
    temp1=registers[instruction[7:10]]
    temp2=registers[instruction[10:13]]
    temp3=registers[instruction[13:16]]
    result = int(file_registers[temp2],2) - int(file_registers[temp3],2)
    if int(file_registers[temp2],2) >= int(file_registers[temp3],2):
        file_registers[temp1] = padding_zeros0(result)
        file_registers["FLAG"] = "0000000000000000"
        print_registers_program_counter()
    elif int(file_registers[temp3],2) > int(file_registers[temp2],2):
        file_registers[temp1] = padding_zeros0(0)
        file_registers["FLAG"] = "0000000000001000"
        print_registers_program_counter()
    global program_counter 
    program_counter += 1

def opcode3(instruction):
    temp1=registers[instruction[6:9]]
    temp2=instruction[9:16]
    file_registers[temp1] = str(temp2).zfill(16)
    file_registers["FLAG"] = "0000000000000000"
    print_registers_program_counter()
    global program_counter 
    program_counter += 1

def opcode4(instruction):
    temp1=registers[instruction[10:13]]
    temp2=registers[instruction[13:16]]
    file_registers[temp1] = file_registers[temp2]
    file_registers["FLAG"] = "0000000000000000"
    print_registers_program_counter()
    global program_counter  
    program_counter += 1   

def opcode5(instruction):
    temp1=registers[instruction[6:9]]
    temp2=instruction[9:16]
    file_registers[temp1] = memory[temp2]
    file_registers["FLAG"] = "0000000000000000"
    print_registers_program_counter()
    global program_counter 
    program_counter += 1

def opcode6(instruction):
    temp1=registers[instruction[6:9]]
    temp2=instruction[9:16]
    memory[temp2] = file_registers[temp1]
    file_registers["FLAG"] = "0000000000000000"
    print_registers_program_counter()
    global program_counter 
    program_counter += 1

def opcode7(instruction):
    temp1=registers[instruction[7:10]]
    temp2=registers[instruction[10:13]]
    temp3=registers[instruction[13:16]]
    result = int(file_registers[temp2],2) * int(file_registers[temp3],2)
    if result <= 127 and result>= 0 :
        file_registers[temp1] = padding_zeros0(result)
        file_registers["FLAG"] = "0000000000000000"
    elif result>127 or result<0:
        file_registers[temp1] = padding_zeros0(0)
        file_registers["FLAG"] = "0000000000001000"
    print_registers_program_counter()
    global program_counter 
    program_counter += 1

def opcode8(instruction):
    temp1=registers[instruction[10:13]]
    temp2=registers[instruction[13:16]]
    if int(file_registers[temp2],2)==0:
        file_registers["FLAG"] = "0000000000001000"
        file_registers["R0"] = padding_zeros0(0)
        file_registers["R1"] = padding_zeros0(0)

    else:
        quotient = int(file_registers[temp1],2) // int(file_registers[temp2],2)
        remainder = int(file_registers[temp1],2) % int(file_registers[temp2],2)
        file_registers["R0"] = padding_zeros0(quotient)
        file_registers["R1"] = padding_zeros0(remainder)
        file_registers["FLAG"] = "0000000000000000"
    print_registers_program_counter()
    global program_counter
    program_counter += 1

def opcode9(instruction):
    temp1=registers[instruction[6:9]]
    temp2=int(instruction[9:16],2)
    temp3= int(file_registers[temp1],2)
    file_registers[temp1]= padding_zeros0(temp3>>temp2)
    file_registers["FLAG"] = "0000000000000000"
    print_registers_program_counter()
    global program_counter
    program_counter += 1

def opcode10(instruction):
    temp1=registers[instruction[6:9]]
    temp2=int(instruction[9:16],2)
    temp3= int(file_registers[temp1],2)
    file_registers[temp1]= padding_zeros0(temp3<<temp2)
    file_registers["FLAG"] = "0000000000000000"
    print_registers_program_counter()
    global program_counter
    program_counter += 1

def opcode11(instruction):
    temp1=registers[instruction[7:10]]
    temp2=registers[instruction[10:13]]
    temp3=registers[instruction[13:16]]
    result = int(file_registers[temp2])^int(file_registers[temp3])
    file_registers[temp1]=padding_zeros(result)
    file_registers["FLAG"] = "0000000000000000"
    print_registers_program_counter()
    global program_counter
    program_counter+=1

def opcode12(instruction):
    temp1=registers[instruction[7:10]]
    temp2=registers[instruction[10:13]]
    temp3=registers[instruction[13:16]]
    result = int(file_registers[temp2])|int(file_registers[temp3])
    file_registers[temp1]=padding_zeros(result)
    file_registers["FLAG"] = "0000000000000000"
    print_registers_program_counter()
    global program_counter
    program_counter+=1

def opcode13(instruction):
    temp1=registers[instruction[7:10]]
    temp2=registers[instruction[10:13]]
    temp3=registers[instruction[13:16]]
    result = int(file_registers[temp2])&int(file_registers[temp3])
    file_registers[temp1]=padding_zeros(result)
    file_registers["FLAG"] = "0000000000000000"
    print_registers_program_counter()
    global program_counter
    program_counter+=1

def opcode14(instruction):
    temp1=registers[instruction[10:13]]
    temp2=registers[instruction[13:16]]
    result = ~int(file_registers[temp2])
    file_registers[temp1]=padding_zeros(result)
    file_registers["FLAG"] = "0000000000000000"
    print_registers_program_counter()
    global program_counter
    program_counter+=1

def opcode15(instruction):
    temp1=registers[instruction[10:13]]
    temp2=registers[instruction[13:16]]
    compare = int(file_registers[temp1])-int(file_registers[temp2])
    if(compare>0):
        file_registers["FLAG"]="0000000000000010"
    elif(compare==0):
        file_registers["FLAG"]="0000000000000001"
    else:
        file_registers["FLAG"]="0000000000000100"
    print_registers_program_counter()
    global program_counter
    program_counter+=1

def opcode16(instruction):
    file_registers["FLAG"] = "0000000000000000"
    print_registers_program_counter()
    global program_counter
    program_counter=int(instruction[9:16],2)

def opcode17(instruction):
    global Flags
    Flags=file_registers["FLAG"]
    file_registers["FLAG"] = "0000000000000000"
    print_registers_program_counter()
    global program_counter
    if(Flags[-3]=='1'):
        program_counter=int(instruction[9:16],2)
    else:
        program_counter+=1

def opcode18(instruction):
    global Flags
    Flags=file_registers["FLAG"]
    file_registers["FLAG"] = "0000000000000000"
    print_registers_program_counter()
    global program_counter
    if(Flags[-2]=='1'):
        program_counter=int(instruction[9:16],2)
    else:
        program_counter+=1

def opcode19(instruction):
    global Flags
    Flags=file_registers["FLAG"]
    file_registers["FLAG"] = "0000000000000000"
    print_registers_program_counter()
    global program_counter
    if(Flags[-1]=='1'):
        program_counter=int(instruction[9:16],2)
    else:
        program_counter+=1

def opcode20(instruction):
    print_registers_program_counter()
    pass

def opcode21(instruction):
    temp1=registers[instruction[7:10]]
    temp2=registers[instruction[10:13]]
    temp3=registers[instruction[13:16]]
    result = ieee_754_to_float(file_registers[temp2]) + ieee_754_to_float(file_registers[temp3])
    if result <= 127 and result>= 0 :
        file_registers[temp1] = float_to_ieee_754(result)
        file_registers["FLAG"] = "0000000000000000"
        print_registers_program_counter()
    elif result>127 or result<0:
        file_registers[temp1] ="0000000000000000"
        file_registers["FLAG"] = "0000000000001000"
        print_registers_program_counter()
    global program_counter 
    program_counter += 1

def opcode22(instruction):
    temp1=registers[instruction[7:10]]
    temp2=registers[instruction[10:13]]
    temp3=registers[instruction[13:16]]
    result = ieee_754_to_float(file_registers[temp2]) - ieee_754_to_float(file_registers[temp3])
    if ieee_754_to_float(file_registers[temp2]) >= ieee_754_to_float(file_registers[temp3]):
        file_registers[temp1] = "0000000000000000"
        file_registers["FLAG"] = "0000000000000000"
        print_registers_program_counter()
    elif ieee_754_to_float(file_registers[temp3]) > ieee_754_to_float(file_registers[temp2]):
        file_registers[temp1] = float_to_ieee_754(0)
        file_registers["FLAG"] = "0000000000001000"
        print_registers_program_counter()
    global program_counter 
    program_counter += 1
def opcode23(instruction):
    temp1=registers[instruction[5:8]]
    temp2=instruction[8:16]
    file_registers[temp1] = str(temp2).zfill(16)
    file_registers["FLAG"] = "0000000000000000"
    print_registers_program_counter()
    global program_counter 
    program_counter += 1
def opcode24(instruction):
    temp1=registers[instruction[7:10]]
    temp2=registers[instruction[10:13]]
    temp3=registers[instruction[13:16]]
    result = ~(int(file_registers[temp2])&int(file_registers[temp3]))
    file_registers[temp1]=padding_zeros(result)
    file_registers["FLAG"] = "0000000000000000"
    print_registers_program_counter()
    global program_counter
    program_counter+=1
def opcode25(instruction):
    temp1=registers[instruction[7:10]]
    temp2=registers[instruction[10:13]]
    temp3=registers[instruction[13:16]]
    result = ~(int(file_registers[temp2])|int(file_registers[temp3]))
    file_registers[temp1]=padding_zeros(result)
    file_registers["FLAG"] = "0000000000000000"
    print_registers_program_counter()
    global program_counter
    program_counter+=1
def opcode26(instruction):
    temp1=registers[instruction[6:9]]
    temp2=instruction[9:16]
    result = int(file_registers[temp1],2) * int(temp2,2)
    if result <= 127 and result>= 0 :
        file_registers[temp1] = padding_zeros0(result)
        file_registers["FLAG"] = "0000000000000000"
    elif result>127 or result<0:
        file_registers[temp1] = padding_zeros0(0)
        file_registers["FLAG"] = "0000000000001000"
    print_registers_program_counter()
    global program_counter 
    program_counter += 1
def opcode27(instruction):
    temp1=registers[instruction[6:9]]
    temp2=instruction[9:16]
    result = int(file_registers[temp1],2) + int(temp2,2)
    if result <= 127 and result>= 0 :
        file_registers[temp1] = padding_zeros0(result)
        file_registers["FLAG"] = "0000000000000000"
    elif result>127 or result<0:
        file_registers[temp1] = padding_zeros0(0)
        file_registers["FLAG"] = "0000000000001000"
    print_registers_program_counter()
    global program_counter 
    program_counter += 1
def opcode28(instruction):
    temp1=registers[instruction[6:9]]
    temp2=instruction[9:16]
    result = int(file_registers[temp1],2) - int(temp2,2)
    if result <= 127 and result>= 0 :
        file_registers[temp1] = padding_zeros0(result)
        file_registers["FLAG"] = "0000000000000000"
    elif result>127 or result<0:
        file_registers[temp1] = padding_zeros0(0)
        file_registers["FLAG"] = "0000000000001000"
    print_registers_program_counter()
    global program_counter 
    program_counter += 1

program = []

while True:
    try:
        command = input()
        program.append(command)
    except EOFError:
        break

while(True):
    machine_code = program[program_counter]
    if(machine_code[0:5]=="00000"):
        opcode1(machine_code)
    elif(machine_code[0:5]=="00001"):
        opcode2(machine_code)
    elif(machine_code[0:5]=="00010"):
        opcode3(machine_code)
    elif(machine_code[0:5]=="00011"):
        opcode4(machine_code)
    elif(machine_code[0:5]=="00100"):
        opcode5(machine_code)     
    elif(machine_code[0:5]=="00101"):
        opcode6(machine_code)
    elif(machine_code[0:5]=="00110"):
        opcode7(machine_code)
    elif(machine_code[0:5]=="00111"):
        opcode8(machine_code)
    elif(machine_code[0:5]=="01000"):
        opcode9(machine_code)
    elif(machine_code[0:5]=="01001"):
        opcode10(machine_code)
    elif(machine_code[0:5]=="01010"):
        opcode11(machine_code)
    elif(machine_code[0:5]=="01011"):
        opcode12(machine_code)
    elif(machine_code[0:5]=="01100"):
        opcode13(machine_code)
    elif(machine_code[0:5]=="01101"):
        opcode14(machine_code)
    elif(machine_code[0:5]=="01110"):
        opcode15(machine_code)
    elif(machine_code[0:5]=="01111"):
        opcode16(machine_code)
    elif(machine_code[0:5]=="11100"):
        opcode17(machine_code)
    elif(machine_code[0:5]=="11101"):
        opcode18(machine_code)
    elif(machine_code[0:5]=="11111"):
        opcode19(machine_code)
    elif(machine_code[0:5]=="11010"):
        opcode20(machine_code)
        break
    elif(machine_code[0:5]=="10000"):
        opcode21(machine_code)
    elif(machine_code[0:5]=="10001"):
        opcode22(machine_code)
    elif(machine_code[0:5]=="10010"):
        opcode23(machine_code)
    elif(machine_code[0:5]=="10011"):
        opcode24(machine_code)
    elif(machine_code[0:5]=="10100"):
        opcode25(machine_code)
    elif(machine_code[0:5]=="10101"):
        opcode26(machine_code)
    elif(machine_code[0:5]=="10110"):
        opcode27(machine_code)
    elif(machine_code[0:5]=="10111"):
        opcode28(machine_code)

dump_memory =[]
for i in range(128):
    dump_memory.append("0000000000000000")
for i in range(len(program)):
    if("\n" not in program[i]):
        dump_memory[i]=program[i]
    else:
        dump_memory[i]=program[i][0:-1]
for i in memory.keys():
    dump_memory[int(i,2)]=memory[i]
for i in dump_memory:
    print(i)
