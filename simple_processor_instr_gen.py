#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import argparse
#import gmpy2 
from random import randint
import numpy as np
#from scipy.ndimage.interpolation import shift
import math

# instr1 
def ADD(instr):
    opcode = 0b100001
    instr = instr.strip()
    str_list = instr.split(',')
    rd = int(str_list[1])  # Destination register
    rs = int(str_list[2])  # Source register
    rt = int(str_list[3])  # Target register
    instr_val_0 = np.binary_repr(opcode, 6)  # Opcode (6 bits)
    instr_val_1 = np.binary_repr(rs, 5)      # Source register (5 bits)
    instr_val_2 = np.binary_repr(rt, 5)      # Target register (5 bits)
    instr_val_3 = np.binary_repr(rd, 5)      # Destination register (5 bits)
    instr_val_4 = np.binary_repr(0, 5)       # Shift amount (shamt, 5 bits)
    instr_val_5 = np.binary_repr(0, 6)   # Function code (6 bits)
    # Combine fields into a single machine code string
    return f"{instr_val_0}_{instr_val_1}_{instr_val_2}_{instr_val_3}_{instr_val_4}_{instr_val_5}"

# instr2
def SUB(instr):
    opcode = 0b100010 
    instr = instr.strip()
    str_list = instr.split(',')
    rd = int(str_list[1])  # Destination register
    rs = int(str_list[2])  # Source register
    rt = int(str_list[3])  # Target register
    instr_val_0 = np.binary_repr(opcode, 6)  # Opcode (6 bits)
    instr_val_1 = np.binary_repr(rs, 5)      # Source register (5 bits)
    instr_val_2 = np.binary_repr(rt, 5)      # Target register (5 bits)
    instr_val_3 = np.binary_repr(rd, 5)      # Destination register (5 bits)
    instr_val_4 = np.binary_repr(0, 5)       # Shift amount (shamt, 5 bits)
    instr_val_5 = np.binary_repr(0, 6)   # Function code (6 bits)
    # Combine fields into a single machine code string
    return f"{instr_val_0}_{instr_val_1}_{instr_val_2}_{instr_val_3}_{instr_val_4}_{instr_val_5}"

# instr4 ??
def SUBU(instr):
    opcode = 0
    instr = instr.strip()
    str_list = instr.split(',')
    rd = int(str_list[1])  # Destination register
    rs = int(str_list[2])  # Source register
    rt = int(str_list[3])  # Target register
    instr_val_0 = np.binary_repr(opcode, 6)  # Opcode (6 bits)
    instr_val_1 = np.binary_repr(rs, 5)      # Source register (5 bits)
    instr_val_2 = np.binary_repr(rt, 5)      # Target register (5 bits)
    instr_val_3 = np.binary_repr(rd, 5)      # Destination register (5 bits)
    instr_val_4 = np.binary_repr(0, 5)       # Shift amount (shamt, 5 bits)
    instr_val_5 = np.binary_repr(0, 6)   # Function code (6 bits)
    # Combine fields into a single machine code string
    return f"{instr_val_0}_{instr_val_1}_{instr_val_2}_{instr_val_3}_{instr_val_4}_{instr_val_5}"

# instr5 
def ADDI(instr):
    opcode = 0b000001  # Opcode for ADDI
    instr = instr.strip()
    str_list = instr.split(',')
    rt = int(str_list[1])  # Target register
    rs = int(str_list[2])  # Source register
    immi = int(str_list[3])  # Immediate value
    instr_val_0 = np.binary_repr(opcode, 6)  # Opcode (6 bits)
    instr_val_1 = np.binary_repr(rs, 5)      # Source register (5 bits)
    instr_val_2 = np.binary_repr(rt, 5)      # Target register (5 bits)
    instr_val_3 = np.binary_repr(immi, 16)   # Immediate value (16 bits)
    # Combine fields into a single machine code string
    return f"{instr_val_0}_{instr_val_1}_{instr_val_2}_{instr_val_3}"

# instr6 ??
def ADDIU(instr):
    opcode = 0  # Opcode for ADDI
    instr = instr.strip()
    str_list = instr.split(',')
    rt = int(str_list[1])  # Target register
    rs = int(str_list[2])  # Source register
    immi = int(str_list[3])  # Immediate value
    instr_val_0 = np.binary_repr(opcode, 6)  # Opcode (6 bits)
    instr_val_1 = np.binary_repr(rs, 5)      # Source register (5 bits)
    instr_val_2 = np.binary_repr(rt, 5)      # Target register (5 bits)
    instr_val_3 = np.binary_repr(immi, 16)   # Immediate value (16 bits)
    # Combine fields into a single machine code string
    return f"{instr_val_0}_{instr_val_1}_{instr_val_2}_{instr_val_3}"

# instr7 ??
def MADD(instr):
    opcode = 0  # Opcode for R-type instructions is 0
    instr = instr.strip()
    str_list = instr.split(',')
    rs = int(str_list[1])  # Source register
    rt = int(str_list[2])  # Target register
    instr_val_0 = np.binary_repr(opcode, 6)  # Opcode (6 bits)
    instr_val_1 = np.binary_repr(rs, 5)      # Source register (5 bits)
    instr_val_2 = np.binary_repr(rt, 5)      # Target register (5 bits)
    instr_val_3 = np.binary_repr(0, 5)       # Destination register (not used, 5 bits)
    instr_val_4 = np.binary_repr(0, 5)       # Shift amount (shamt, 5 bits)
    instr_val_5 = np.binary_repr(0, 6)   # Function code (6 bits)
    # Combine fields into a single machine code string
    return f"{instr_val_0}_{instr_val_1}_{instr_val_2}_{instr_val_3}_{instr_val_4}_{instr_val_5}"

# instr8 ??
def MADDU(instr):
    opcode = 0  # Opcode for R-type instructions is 0
    instr = instr.strip()
    str_list = instr.split(',')
    rs = int(str_list[1])  # Source register
    rt = int(str_list[2])  # Target register
    instr_val_0 = np.binary_repr(opcode, 6)  # Opcode (6 bits)
    instr_val_1 = np.binary_repr(rs, 5)      # Source register (5 bits)
    instr_val_2 = np.binary_repr(rt, 5)      # Target register (5 bits)
    instr_val_3 = np.binary_repr(0, 5)       # Destination register (not used, 5 bits)
    instr_val_4 = np.binary_repr(0, 5)       # Shift amount (shamt, 5 bits)
    instr_val_5 = np.binary_repr(0, 6)   # Function code (6 bits)
    # Combine fields into a single machine code string
    return f"{instr_val_0}_{instr_val_1}_{instr_val_2}_{instr_val_3}_{instr_val_4}_{instr_val_5}"

# instr9 (check this)
def MUL(instr):
    opcode = 0b101101  # Opcode for R-type instructions is 0
    instr = instr.strip()
    str_list = instr.split(',')
    rs = int(str_list[1])  # Source register
    rt = int(str_list[2])  # Target register
    instr_val_0 = np.binary_repr(opcode, 6)  # Opcode (6 bits)
    instr_val_1 = np.binary_repr(rs, 5)      # Source register (5 bits)
    instr_val_2 = np.binary_repr(rt, 5)      # Target register (5 bits)
    instr_val_3 = np.binary_repr(0, 5)      # Destination register (5 bits)
    instr_val_4 = np.binary_repr(0, 5)       # Shift amount (shamt, 5 bits)
    instr_val_5 = np.binary_repr(0, 6)   # Function code (6 bits)
    # Combine fields into a single machine code string
    return f"{instr_val_0}_{instr_val_1}_{instr_val_2}_{instr_val_3}_{instr_val_4}_{instr_val_5}"

# instr10
def AND(instr):
    opcode = 0b100011  # Opcode for R-type instructions is 0
    instr = instr.strip()
    str_list = instr.split(',')
    rd = int(str_list[1])  # Destination register
    rs = int(str_list[2])  # Source register
    rt = int(str_list[3])  # Target register
    instr_val_0 = np.binary_repr(opcode, 6)  # Opcode (6 bits)
    instr_val_1 = np.binary_repr(rs, 5)      # Source register (5 bits)
    instr_val_2 = np.binary_repr(rt, 5)      # Target register (5 bits)
    instr_val_3 = np.binary_repr(rd, 5)      # Destination register (5 bits)
    instr_val_4 = np.binary_repr(0, 5)       # Shift amount (shamt, 5 bits)
    instr_val_5 = np.binary_repr(0, 6)   # Function code (6 bits)
    # Combine fields into a single machine code string
    return f"{instr_val_0}_{instr_val_1}_{instr_val_2}_{instr_val_3}_{instr_val_4}_{instr_val_5}"

# instr11
def OR(instr):
    opcode = 0b100100  # Opcode for R-type instructions is 0
    instr = instr.strip()
    str_list = instr.split(',')
    rd = int(str_list[1])  # Destination register
    rs = int(str_list[2])  # Source register
    rt = int(str_list[3])  # Target register
    instr_val_0 = np.binary_repr(opcode, 6)  # Opcode (6 bits)
    instr_val_1 = np.binary_repr(rs, 5)      # Source register (5 bits)
    instr_val_2 = np.binary_repr(rt, 5)      # Target register (5 bits)
    instr_val_3 = np.binary_repr(rd, 5)      # Destination register (5 bits)
    instr_val_4 = np.binary_repr(0, 5)       # Shift amount (shamt, 5 bits)
    instr_val_5 = np.binary_repr(0, 6)   # Function code (6 bits)
    # Combine fields into a single machine code string
    return f"{instr_val_0}_{instr_val_1}_{instr_val_2}_{instr_val_3}_{instr_val_4}_{instr_val_5}"

# instr12
def ANDI(instr):
    opcode = 0b000001  # Opcode for ADDI
    instr = instr.strip()
    str_list = instr.split(',')
    rt = int(str_list[1])  # Target register
    rs = int(str_list[2])  # Source register
    immi = int(str_list[3])  # Immediate value
    instr_val_0 = np.binary_repr(opcode, 6)  # Opcode (6 bits)
    instr_val_1 = np.binary_repr(rs, 5)      # Source register (5 bits)
    instr_val_2 = np.binary_repr(rt, 5)      # Target register (5 bits)
    instr_val_3 = np.binary_repr(immi, 16)   # Immediate value (16 bits)
    # Combine fields into a single machine code string
    return f"{instr_val_0}_{instr_val_1}_{instr_val_2}_{instr_val_3}"

def SUBI(instr):
    opcode = 0b000010  # Opcode for ADDI
    instr = instr.strip()
    str_list = instr.split(',')
    rt = int(str_list[1])  # Target register
    rs = int(str_list[2])  # Source register
    immi = int(str_list[3])  # Immediate value
    instr_val_0 = np.binary_repr(opcode, 6)  # Opcode (6 bits)
    instr_val_1 = np.binary_repr(rs, 5)      # Source register (5 bits)
    instr_val_2 = np.binary_repr(rt, 5)      # Target register (5 bits)
    instr_val_3 = np.binary_repr(immi, 16)   # Immediate value (16 bits)
    # Combine fields into a single machine code string
    return f"{instr_val_0}_{instr_val_1}_{instr_val_2}_{instr_val_3}"


# instr13
def ORI(instr):
    opcode = 0b000100  # Opcode for ADDI
    instr = instr.strip()
    str_list = instr.split(',')
    rt = int(str_list[1])  # Target register
    rs = int(str_list[2])  # Source register
    immi = int(str_list[3])  # Immediate value
    instr_val_0 = np.binary_repr(opcode, 6)  # Opcode (6 bits)
    instr_val_1 = np.binary_repr(rs, 5)      # Source register (5 bits)
    instr_val_2 = np.binary_repr(rt, 5)      # Target register (5 bits)
    instr_val_3 = np.binary_repr(immi, 16)   # Immediate value (16 bits)
    # Combine fields into a single machine code string
    return f"{instr_val_0}_{instr_val_1}_{instr_val_2}_{instr_val_3}"


# instr14
def NOT(instr):
    opcode = 0b100101  # Opcode for R-type instructions is 0
    instr = instr.strip()
    str_list = instr.split(',')
    rd = int(str_list[1])  # Destination register
    rs = int(str_list[2])  # Source register
    rt = int(str_list[3])  # Target register
    instr_val_0 = np.binary_repr(opcode, 6)  # Opcode (6 bits)
    instr_val_1 = np.binary_repr(rs, 5)      # Source register (5 bits)
    instr_val_2 = np.binary_repr(rt, 5)      # Target register (5 bits)
    instr_val_3 = np.binary_repr(rd, 5)      # Destination register (5 bits)
    instr_val_4 = np.binary_repr(0, 5)       # Shift amount (shamt, 5 bits)
    instr_val_5 = np.binary_repr(0, 6)   # Function code (6 bits)
    # Combine fields into a single machine code string
    return f"{instr_val_0}_{instr_val_1}_{instr_val_2}_{instr_val_3}_{instr_val_4}_{instr_val_5}"


# instr15
def XORI(instr):
    opcode = 0b000110  # Opcode for ADDI
    instr = instr.strip()
    str_list = instr.split(',')
    rt = int(str_list[1])  # Target register
    rs = int(str_list[2])  # Source register
    immi = int(str_list[3])  # Immediate value
    instr_val_0 = np.binary_repr(opcode, 6)  # Opcode (6 bits)
    instr_val_1 = np.binary_repr(rs, 5)      # Source register (5 bits)
    instr_val_2 = np.binary_repr(rt, 5)      # Target register (5 bits)
    instr_val_3 = np.binary_repr(immi, 16)   # Immediate value (16 bits)
    # Combine fields into a single machine code string
    return f"{instr_val_0}_{instr_val_1}_{instr_val_2}_{instr_val_3}"


# instr16
def XOR(instr):
    opcode = 0b100110  # Opcode for R-type instructions is 0
    instr = instr.strip()
    str_list = instr.split(',')
    rd = int(str_list[1])  # Destination register
    rs = int(str_list[2])  # Source register
    rt = int(str_list[3])  # Target register
    instr_val_0 = np.binary_repr(opcode, 6)  # Opcode (6 bits)
    instr_val_1 = np.binary_repr(rs, 5)      # Source register (5 bits)
    instr_val_2 = np.binary_repr(rt, 5)      # Target register (5 bits)
    instr_val_3 = np.binary_repr(rd, 5)      # Destination register (5 bits)
    instr_val_4 = np.binary_repr(0, 5)       # Shift amount (shamt, 5 bits)
    instr_val_5 = np.binary_repr(0, 6)   # Function code (6 bits)
    # Combine fields into a single machine code string
    return f"{instr_val_0}_{instr_val_1}_{instr_val_2}_{instr_val_3}_{instr_val_4}_{instr_val_5}"


# instr17 (check this)
def SLL(instr):
    opcode = 0b001000  # Opcode for R-type instructions is 0
    instr = instr.strip()
    str_list = instr.split(',')
    rt = int(str_list[1])  # Destination register
    rs = int(str_list[2])  # Source register
    immi = int(str_list[3])  # Target register
    instr_val_0 = np.binary_repr(opcode, 6)  # Opcode (6 bits)
    instr_val_1 = np.binary_repr(rs, 5)      # Source register (5 bits)
    instr_val_2 = np.binary_repr(rt, 5)      # Target register (5 bits)
    instr_val_3 = np.binary_repr(immi, 16)   # Function code (6 bits)
    # Combine fields into a single machine code string
    return f"{instr_val_0}_{instr_val_1}_{instr_val_2}_{instr_val_3}"

# instr18
def SRL(instr):
    opcode = 0b001001  # Opcode for R-type instructions is 0
    instr = instr.strip()
    str_list = instr.split(',')
    rt = int(str_list[1])  # Destination register
    rs = int(str_list[2])  # Source register
    immi = int(str_list[3])  # Target register
    instr_val_0 = np.binary_repr(opcode, 6)  # Opcode (6 bits)
    instr_val_1 = np.binary_repr(rs, 5)      # Source register (5 bits)
    instr_val_2 = np.binary_repr(rt, 5)      # Target register (5 bits)
    instr_val_3 = np.binary_repr(immi, 16)   # Function code (6 bits)
    # Combine fields into a single machine code string
    return f"{instr_val_0}_{instr_val_1}_{instr_val_2}_{instr_val_3}"

# instr19 (check this)
def SLA(instr):
    opcode = 0b001010  # Opcode for R-type instructions is 0
    instr = instr.strip()
    str_list = instr.split(',')
    rs = int(str_list[1])  # Destination register
    rt = int(str_list[2])  # Target register
    immi = int(str_list[3])  # Shift amount
    instr_val_0 = np.binary_repr(opcode, 6)  # Opcode (6 bits)
    instr_val_1 = np.binary_repr(rs, 5)       # RS is 0 for shift instructions
    instr_val_2 = np.binary_repr(rt, 5)      # Target register (5 bits)
    instr_val_3 = np.binary_repr(immi, 16)      # Destination register (5 bits)
    # Combine fields into a single machine code string
    return f"{instr_val_0}_{instr_val_1}_{instr_val_2}_{instr_val_3}"

# instr20 (check this)
def SRA(instr):
    opcode = 0b001011  # Opcode for R-type instructions is 0
    instr = instr.strip()
    str_list = instr.split(',')
    rs = int(str_list[1])  # Destination register
    rt = int(str_list[2])  # Target register
    immi = int(str_list[3])  # Shift amount
    instr_val_0 = np.binary_repr(opcode, 6)  # Opcode (6 bits)
    instr_val_1 = np.binary_repr(rs, 5)       # RS is 0 for shift instructions
    instr_val_2 = np.binary_repr(rt, 5)      # Target register (5 bits)
    instr_val_3 = np.binary_repr(immi, 16)      # Destination register (5 bits)
    # Combine fields into a single machine code string
    return f"{instr_val_0}_{instr_val_1}_{instr_val_2}_{instr_val_3}"

# instr21 (check this)
def LW(instr):
    opcode = 0b001110  # Opcode for ADDI
    instr = instr.strip()
    str_list = instr.split(',')
    rt = int(str_list[1])  # Target register
    rs = int(str_list[2])  # Source register
    immi = int(str_list[3])  # Immediate value
    instr_val_0 = np.binary_repr(opcode, 6)  # Opcode (6 bits)
    instr_val_1 = np.binary_repr(rs, 5)      # Source register (5 bits)
    instr_val_2 = np.binary_repr(rt, 5)      # Target register (5 bits)
    instr_val_3 = np.binary_repr(immi, 16)   # Immediate value (16 bits)
    # Combine fields into a single machine code string
    return f"{instr_val_0}_{instr_val_1}_{instr_val_2}_{instr_val_3}"
    
# instr22 (check this)
def SW(instr):
    opcode = 0b001111  # Opcode for ADDI
    instr = instr.strip()
    str_list = instr.split(',')
    rt = int(str_list[1])  # Target register
    rs = int(str_list[2])  # Source register
    immi = int(str_list[3])  # Immediate value
    instr_val_0 = np.binary_repr(opcode, 6)  # Opcode (6 bits)
    instr_val_1 = np.binary_repr(rs, 5)      # Source register (5 bits)
    instr_val_2 = np.binary_repr(rt, 5)      # Target register (5 bits)
    instr_val_3 = np.binary_repr(immi, 16)   # Immediate value (16 bits)
    # Combine fields into a single machine code string
    return f"{instr_val_0}_{instr_val_1}_{instr_val_2}_{instr_val_3}"

# instr23 ??
def LUI(instr):
    opcode = 0  # Opcode for ADDI
    instr = instr.strip()
    str_list = instr.split(',')
    rt = int(str_list[1])  # Target register
    rs = int(str_list[2])  # Source register
    immi = int(str_list[3])  # Immediate value
    instr_val_0 = np.binary_repr(opcode, 6)  # Opcode (6 bits)
    instr_val_1 = np.binary_repr(rs, 5)      # Source register (5 bits)
    instr_val_2 = np.binary_repr(rt, 5)      # Target register (5 bits)
    instr_val_3 = np.binary_repr(immi, 16)   # Immediate value (16 bits)
    # Combine fields into a single machine code string
    return f"{instr_val_0}_{instr_val_1}_{instr_val_2}_{instr_val_3}"

# instr24  
def BEQ(instr):
    opcode = 0b010000  # Opcode for ADDI
    instr = instr.strip()
    str_list = instr.split(',')
    rt = int(str_list[1])  # Target register
    rs = int(str_list[2])  # Source register
    immi = int(str_list[3])  # Immediate value
    instr_val_0 = np.binary_repr(opcode, 6)  # Opcode (6 bits)
    instr_val_1 = np.binary_repr(rs, 5)      # Source register (5 bits)
    instr_val_2 = np.binary_repr(rt, 5)      # Target register (5 bits)
    instr_val_3 = np.binary_repr(immi, 16)   # Immediate value (16 bits)
    # Combine fields into a single machine code string
    return f"{instr_val_0}_{instr_val_1}_{instr_val_2}_{instr_val_3}"

# instr25
def BNE(instr):
    opcode = 0b010001  # Opcode for ADDI
    instr = instr.strip()
    str_list = instr.split(',')
    rt = int(str_list[1])  # Target register
    rs = int(str_list[2])  # Source register
    immi = int(str_list[3])  # Immediate value
    instr_val_0 = np.binary_repr(opcode, 6)  # Opcode (6 bits)
    instr_val_1 = np.binary_repr(rs, 5)      # Source register (5 bits)
    instr_val_2 = np.binary_repr(rt, 5)      # Target register (5 bits)
    instr_val_3 = np.binary_repr(immi, 16)   # Immediate value (16 bits)
    # Combine fields into a single machine code string
    return f"{instr_val_0}_{instr_val_1}_{instr_val_2}_{instr_val_3}"

# instr26
def BGT(instr):
    opcode = 0b010010  # Opcode for ADDI
    instr = instr.strip()
    str_list = instr.split(',')
    rt = int(str_list[1])  # Target register
    rs = int(str_list[2])  # Source register
    immi = int(str_list[3])  # Immediate value
    instr_val_0 = np.binary_repr(opcode, 6)  # Opcode (6 bits)
    instr_val_1 = np.binary_repr(rs, 5)      # Source register (5 bits)
    instr_val_2 = np.binary_repr(rt, 5)      # Target register (5 bits)
    instr_val_3 = np.binary_repr(immi, 16)   # Immediate value (16 bits)
    # Combine fields into a single machine code string
    return f"{instr_val_0}_{instr_val_1}_{instr_val_2}_{instr_val_3}"

# instr27
def BGTE(instr):
    opcode = 0b010011  # Custom opcode for BGTE
    instr = instr.strip()
    str_list = instr.split(',')
    rs = int(str_list[1])  # Source register
    rt = int(str_list[2])  # Target register
    offset = int(str_list[3])  # Branch offset
    instr_val_0 = np.binary_repr(opcode, 6)  # Opcode (6 bits)
    instr_val_1 = np.binary_repr(rs, 5)      # Source register (5 bits)
    instr_val_2 = np.binary_repr(rt, 5)      # Target register (5 bits)
    instr_val_3 = np.binary_repr(offset, 16) # Offset (16 bits)
    # Combine fields into a single machine code string
    return f"{instr_val_0}_{instr_val_1}_{instr_val_2}_{instr_val_3}"

# instr28
def BLE(instr):
    opcode = 0b010100  # Custom opcode for BLE
    instr = instr.strip()
    str_list = instr.split(',')
    rs = int(str_list[1])  # Source register
    rt = int(str_list[2])  # Target register
    offset = int(str_list[3])  # Branch offset
    instr_val_0 = np.binary_repr(opcode, 6)  # Opcode (6 bits)
    instr_val_1 = np.binary_repr(rs, 5)      # Source register (5 bits)
    instr_val_2 = np.binary_repr(rt, 5)      # Target register (5 bits)
    instr_val_3 = np.binary_repr(offset, 16) # Offset (16 bits)
    # Combine fields into a single machine code string
    return f"{instr_val_0}_{instr_val_1}_{instr_val_2}_{instr_val_3}"

# instr29
def BLEQ(instr):
    opcode = 0b010101  # Custom opcode for BLEQ
    instr = instr.strip()
    str_list = instr.split(',')
    rs = int(str_list[1])  # Source register
    rt = int(str_list[2])  # Target register
    offset = int(str_list[3])  # Branch offset
    instr_val_0 = np.binary_repr(opcode, 6)  # Opcode (6 bits)
    instr_val_1 = np.binary_repr(rs, 5)      # Source register (5 bits)
    instr_val_2 = np.binary_repr(rt, 5)      # Target register (5 bits)
    instr_val_3 = np.binary_repr(offset, 16) # Offset (16 bits)
    # Combine fields into a single machine code string
    return f"{instr_val_0}_{instr_val_1}_{instr_val_2}_{instr_val_3}"

# instr30 (check this)
def BLEU(instr):
    opcode = 0b010110  # Custom opcode for BLEU
    instr = instr.strip()
    str_list = instr.split(',')
    rs = int(str_list[1])  # Source register
    rt = int(str_list[2])  # Target register
    offset = int(str_list[3])  # Branch offset
    instr_val_0 = np.binary_repr(opcode, 6)  # Opcode (6 bits)
    instr_val_1 = np.binary_repr(rs, 5)      # Source register (5 bits)
    instr_val_2 = np.binary_repr(rt, 5)      # Target register (5 bits)
    instr_val_3 = np.binary_repr(offset, 16) # Offset (16 bits)
    # Combine fields into a single machine code string
    return f"{instr_val_0}_{instr_val_1}_{instr_val_2}_{instr_val_3}"

# instr31 (check this)
def BGTU(instr):
    opcode = 0b010111  # Custom opcode for BGTU (choose a unique opcode)
    instr = instr.strip()
    str_list = instr.split(',')
    rs = int(str_list[1])  # Source register
    rt = int(str_list[2])  # Target register
    offset = int(str_list[3])  # Branch offset
    instr_val_0 = np.binary_repr(opcode, 6)  # Opcode (6 bits)
    instr_val_1 = np.binary_repr(rs, 5)      # Source register (5 bits)
    instr_val_2 = np.binary_repr(rt, 5)      # Target register (5 bits)
    instr_val_3 = np.binary_repr(offset, 16) # Offset (16 bits)
    # Combine fields into a single machine code string
    return f"{instr_val_0}_{instr_val_1}_{instr_val_2}_{instr_val_3}"

# instr32
def J(instr):
    opcode = 0b011000  # Standard opcode for JUMP in MIPS
    instr = instr.strip()
    str_list = instr.split(',')
    address = int(str_list[1])  # Target address (word-aligned)
    instr_val_0 = np.binary_repr(opcode, 6)
    instr_val_1 = np.binary_repr(0, 11)     # Opcode (6 bits)
    instr_val_2 = np.binary_repr(address, 15)   # Address (26 bits)
    # Combine fields into a single machine code string
    return f"{instr_val_0}_{instr_val_1}_{instr_val_2}"

# instr33
def JR(instr):
    opcode = 0b011001       # R-type base opcode
    funct = 0x08        # funct code for JR
    instr = instr.strip()
    str_list = instr.split(',')
    rs = int(str_list[1])  # Source register (the jump address is in this register)
    instr_val_0 = np.binary_repr(opcode, 6)  # Opcode (6 bits)
    instr_val_1 = np.binary_repr(rs, 5)      # rs (5 bits)
    instr_val_2 = np.binary_repr(0, 5)       # rt (unused, set to 0)
    instr_val_3 = np.binary_repr(0, 5)       # rd (unused, set to 0)
    instr_val_4 = np.binary_repr(0, 5)       # shamt (set to 0)
    instr_val_5 = np.binary_repr(0, 6)   # funct (6 bits)
    return f"{instr_val_0}_{instr_val_1}_{instr_val_2}_{instr_val_3}_{instr_val_4}_{instr_val_5}"

# instr34
def JAL(instr):
    opcode = 0b011010  # Opcode for JAL in MIPS
    instr = instr.strip()
    str_list = instr.split(',')
    address = int(str_list[1])  # Target address (should be word-aligned)
    instr_val_0 = np.binary_repr(opcode, 6)     # Opcode (6 bits)
    instr_val_1 = np.binary_repr(0, 11)     # Opcode (6 bits)
    instr_val_2 = np.binary_repr(address, 15)   # Target address (26 bits)
    return f"{instr_val_0}_{instr_val_1}_{instr_val_2}"

# instr35
def SLT(instr):
    opcode = 0b101100      # R-type opcode
    instr = instr.strip()
    str_list = instr.split(',')
    rd = int(str_list[1])  # Destination register
    rs = int(str_list[2])  # Source register
    rt = int(str_list[3])  # Target register
    instr_val_0 = np.binary_repr(opcode, 6)  # Opcode (6 bits)
    instr_val_1 = np.binary_repr(rs, 5)      # rs (5 bits)
    instr_val_2 = np.binary_repr(rt, 5)      # rt (5 bits)
    instr_val_3 = np.binary_repr(rd, 5)      # rd (5 bits)
    instr_val_4 = np.binary_repr(0, 5)       # shamt (always 0)
    instr_val_5 = np.binary_repr(0, 6)   # funct (6 bits)
    return f"{instr_val_0}_{instr_val_1}_{instr_val_2}_{instr_val_3}_{instr_val_4}_{instr_val_5}"

# instr36
def SLTI(instr):
    opcode = 0b001001  # Opcode for SLTI
    instr = instr.strip()
    str_list = instr.split(',')
    rt = int(str_list[1])         # Destination register
    rs = int(str_list[2])         # Source register
    imm = int(str_list[3])        # Immediate value (signed)
    instr_val_0 = np.binary_repr(opcode, 6)    # Opcode (6 bits)
    instr_val_1 = np.binary_repr(rs, 5)        # rs (5 bits)
    instr_val_2 = np.binary_repr(rt, 5)        # rt (5 bits)
    instr_val_3 = np.binary_repr(imm, 16)      # Immediate (16 bits)
    return f"{instr_val_0}_{instr_val_1}_{instr_val_2}_{instr_val_3}"

# instr37
def SEQ(instr):
    opcode = 0b001101  # Opcode for SLTI
    instr = instr.strip()
    str_list = instr.split(',')
    rt = int(str_list[1])         # Destination register
    rs = int(str_list[2])         # Source register
    imm = int(str_list[3])        # Immediate value (signed)
    instr_val_0 = np.binary_repr(opcode, 6)    # Opcode (6 bits)
    instr_val_1 = np.binary_repr(rs, 5)        # rs (5 bits)
    instr_val_2 = np.binary_repr(rt, 5)        # rt (5 bits)
    instr_val_3 = np.binary_repr(imm, 16)      # Immediate (16 bits)
    return f"{instr_val_0}_{instr_val_1}_{instr_val_2}_{instr_val_3}"

# instr38 ??
def MFCL(instr):
    opcode = 0b111000  # Coprocessor opcode
    rs_field = 0b00000  # Custom value to represent MFCL operation (can vary)
    instr = instr.strip()
    str_list = instr.split(',')
    rd = int(str_list[1])  # Destination register in CPU
    rt = int(str_list[2])  # Source register in coprocessor
    instr_val_0 = np.binary_repr(opcode, 6)   # Opcode (6 bits)
    instr_val_1 = np.binary_repr(rs_field, 5) # rs (MFCL operation selector)
    instr_val_2 = np.binary_repr(rt, 5)       # Coprocessor reg (rt)
    instr_val_3 = np.binary_repr(rd, 5)       # Destination CPU reg (rd)
    instr_val_4 = np.binary_repr(0, 5)        # shamt (not used)
    instr_val_5 = np.binary_repr(0, 6)        # funct (not used)
    return f"{instr_val_0}_{instr_val_1}_{instr_val_2}_{instr_val_3}_{instr_val_4}_{instr_val_5}"

# instr39 ??
def MTCL(instr):
    opcode = 0b111001  # Coprocessor base opcode
    rs_field = 0b00001  # Custom value for MTCL (different from MFCL)
    instr = instr.strip()
    str_list = instr.split(',')
    rt = int(str_list[1])  # Destination register in coprocessor
    rs = int(str_list[2])  # Source register in CPU
    instr_val_0 = np.binary_repr(opcode, 6)   # Opcode (6 bits)
    instr_val_1 = np.binary_repr(rs_field, 5) # Custom selector for MTCL
    instr_val_2 = np.binary_repr(rt, 5)       # Coprocessor destination register
    instr_val_3 = np.binary_repr(rs, 5)       # CPU source register
    instr_val_4 = np.binary_repr(0, 5)        # shamt (unused)
    instr_val_5 = np.binary_repr(0, 6)        # funct (unused)
    return f"{instr_val_0}_{instr_val_1}_{instr_val_2}_{instr_val_3}_{instr_val_4}_{instr_val_5}"

# instr40 ??
def ADD_S(instr):
    opcode = 0b110001  # COP1 opcode
    fmt = 0b10000      # Single precision
    funct = 0b000000   # ADD.S funct code
    instr = instr.strip()
    str_list = instr.split(',')
    fd = int(str_list[1])  # Destination float reg
    fs = int(str_list[2])  # Source float reg
    ft = int(str_list[3])  # Target float reg
    instr_val_0 = np.binary_repr(opcode, 6)  # Opcode
    instr_val_1 = np.binary_repr(fmt, 5)     # Format (single)
    instr_val_2 = np.binary_repr(ft, 5)      # ft
    instr_val_3 = np.binary_repr(fs, 5)      # fs
    instr_val_4 = np.binary_repr(fd, 5)      # fd
    instr_val_5 = np.binary_repr(funct, 6)   # Function
    return f"{instr_val_0}_{instr_val_1}_{instr_val_2}_{instr_val_3}_{instr_val_4}_{instr_val_5}"

# instr41 ??
def SUB_S(instr):
    opcode = 0b110010  # COP1 opcode
    fmt = 0b10000      # Format for single-precision float
    funct = 0b000001   # Function code for sub.s
    instr = instr.strip()
    str_list = instr.split(',')
    fd = int(str_list[1])  # Destination float register
    fs = int(str_list[2])  # First source float register
    ft = int(str_list[3])  # Second source float register
    instr_val_0 = np.binary_repr(opcode, 6)  # Opcode
    instr_val_1 = np.binary_repr(fmt, 5)     # fmt
    instr_val_2 = np.binary_repr(ft, 5)      # ft
    instr_val_3 = np.binary_repr(fs, 5)      # fs
    instr_val_4 = np.binary_repr(fd, 5)      # fd
    instr_val_5 = np.binary_repr(funct, 6)   # funct
    return f"{instr_val_0}_{instr_val_1}_{instr_val_2}_{instr_val_3}_{instr_val_4}_{instr_val_5}"

# instr42 ??
def C_EQ_S(instr):
    opcode = 0b110011  # COP1
    fmt = 0b10000      # Single-precision
    funct = 0b110010   # Function code for c.eq.s
    cc = 0b00000       # Condition code (FCC 0)
    instr = instr.strip()
    str_list = instr.split(',')
    fs = int(str_list[1])  # First float operand
    ft = int(str_list[2])  # Second float operand
    instr_val_0 = np.binary_repr(opcode, 6)  # Opcode
    instr_val_1 = np.binary_repr(fmt, 5)     # Format
    instr_val_2 = np.binary_repr(ft, 5)      # ft
    instr_val_3 = np.binary_repr(fs, 5)      # fs
    instr_val_4 = np.binary_repr(cc, 5)      # condition code
    instr_val_5 = np.binary_repr(funct, 6)   # funct
    return f"{instr_val_0}_{instr_val_1}_{instr_val_2}_{instr_val_3}_{instr_val_4}_{instr_val_5}"

# instr43 ??
def C_LE_S(instr):
    opcode = 0b110100  # COP1
    fmt = 0b10000      # Format: single-precision
    funct = 0b110110   # Function code for c.le.s
    cc = 0b00000       # Condition code FCC0
    instr = instr.strip()
    str_list = instr.split(',')
    fs = int(str_list[1])  # First operand
    ft = int(str_list[2])  # Second operand
    instr_val_0 = np.binary_repr(opcode, 6)  # Opcode
    instr_val_1 = np.binary_repr(fmt, 5)     # fmt
    instr_val_2 = np.binary_repr(ft, 5)      # ft
    instr_val_3 = np.binary_repr(fs, 5)      # fs
    instr_val_4 = np.binary_repr(cc, 5)      # condition code
    instr_val_5 = np.binary_repr(funct, 6)   # funct
    return f"{instr_val_0}_{instr_val_1}_{instr_val_2}_{instr_val_3}_{instr_val_4}_{instr_val_5}"

# instr44 ??
def C_LT_S(instr):
    opcode = 0b110101  # COP1
    fmt = 0b10000      # Format: single-precision
    funct = 0b110100   # Function code for c.lt.s
    cc = 0b00000       # Condition code FCC0
    instr = instr.strip()
    str_list = instr.split(',')
    fs = int(str_list[1])  # First operand
    ft = int(str_list[2])  # Second operand
    instr_val_0 = np.binary_repr(opcode, 6)
    instr_val_1 = np.binary_repr(fmt, 5)
    instr_val_2 = np.binary_repr(ft, 5)
    instr_val_3 = np.binary_repr(fs, 5)
    instr_val_4 = np.binary_repr(cc, 5)
    instr_val_5 = np.binary_repr(funct, 6)
    return f"{instr_val_0}_{instr_val_1}_{instr_val_2}_{instr_val_3}_{instr_val_4}_{instr_val_5}"

# instr45 ??
def C_GE_S(instr):
    opcode = 0b110110  # COP1
    fmt = 0b10000      # Format for single-precision
    funct = 0b110111   # Function code for c.ge.s
    cc = 0b00000       # Condition code FCC0
    instr = instr.strip()
    str_list = instr.split(',')
    fs = int(str_list[1])  # First operand
    ft = int(str_list[2])  # Second operand
    instr_val_0 = np.binary_repr(opcode, 6)  # Opcode
    instr_val_1 = np.binary_repr(fmt, 5)     # fmt
    instr_val_2 = np.binary_repr(ft, 5)      # ft
    instr_val_3 = np.binary_repr(fs, 5)      # fs
    instr_val_4 = np.binary_repr(cc, 5)      # condition code
    instr_val_5 = np.binary_repr(funct, 6)   # funct
    return f"{instr_val_0}_{instr_val_1}_{instr_val_2}_{instr_val_3}_{instr_val_4}_{instr_val_5}"

# instr46 ??
def C_GT_S(instr):
    opcode = 0b110111  # COP1
    fmt = 0b10000      # Format: single-precision
    funct = 0b111000   # Function code for c.gt.s
    cc = 0b00000       # Condition code FCC0
    instr = instr.strip()
    str_list = instr.split(',')
    fs = int(str_list[1])  # First operand
    ft = int(str_list[2])  # Second operand
    instr_val_0 = np.binary_repr(opcode, 6)  # Opcode
    instr_val_1 = np.binary_repr(fmt, 5)     # fmt
    instr_val_2 = np.binary_repr(ft, 5)      # ft
    instr_val_3 = np.binary_repr(fs, 5)      # fs
    instr_val_4 = np.binary_repr(cc, 5)      # condition code
    instr_val_5 = np.binary_repr(funct, 6)   # funct
    return f"{instr_val_0}_{instr_val_1}_{instr_val_2}_{instr_val_3}_{instr_val_4}_{instr_val_5}"

# instr47 ??
def MOV_S(instr):
    opcode = 0b010001  # COP1
    fmt = 0b10000      # Format: single-precision
    funct = 0b000000   # Function code for mov.s
    cc = 0b00000       # Condition code FCC0
    instr = instr.strip()
    str_list = instr.split(',')
    fd = int(str_list[1])  # Destination operand
    fs = int(str_list[2])  # Source operand
    instr_val_0 = np.binary_repr(opcode, 6)  # Opcode
    instr_val_1 = np.binary_repr(fmt, 5)     # fmt
    instr_val_2 = np.binary_repr(fs, 5)      # fs (source register)
    instr_val_3 = np.binary_repr(fd, 5)      # fd (destination register)
    instr_val_4 = np.binary_repr(cc, 5)      # condition code
    instr_val_5 = np.binary_repr(funct, 6)   # funct
    return f"{instr_val_0}_{instr_val_1}_{instr_val_2}_{instr_val_3}_{instr_val_4}_{instr_val_5}"

def FINISH(instr):
    opcode=0x3f
    instr_val_0 =np.binary_repr(opcode,6)
    instr_val_1 =np.binary_repr(0,26)
    return instr_val_0+instr_val_1

file_a=open("machine_code.txt","w")
file_b=open("assembly.txt")

Instrs=file_b.readlines()

for instrs in Instrs:
    if(instrs[0:3]=="ADD" and instrs[0:4]!="ADDU" and instrs[0:4]!="ADDI" and instrs[0:5]!="ADDIU"):
        ret_instr=ADD(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:3]=="SUB" and instrs[0:4]!="SUBU" and instrs[0:4]!="SUBI"):
        ret_instr=SUB(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:4]=="SUBU"):
        ret_instr=SUBU(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:4]=="SUBI"):
        ret_instr=SUBI(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:4]=="ADDI" and instrs[0:5]!="ADDIU"):
        ret_instr=ADDI(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:5]=="ADDIU"):
        ret_instr=ADDIU(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:4]=="MADD" and instrs[0:5]!="MADDU"):
        ret_instr=MADD(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:5]=="MADDU"):
        ret_instr=MADDU(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:3]=="MUL"):
        ret_instr=MUL(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:3]=="AND"):
        ret_instr=AND(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:2]=="OR"):
        ret_instr=OR(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:4]=="ANDI"):
        ret_instr=ANDI(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:3]=="ORI"):
        ret_instr=ORI(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:3]=="NOT"):
        ret_instr=NOT(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:4]=="XORI"):
        ret_instr=XORI(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:3]=="XOR"):
        ret_instr=XOR(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:3]=="SLL"):
        ret_instr=SLL(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:3]=="SRL"):
        ret_instr=SRL(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:3]=="SLA"):
        ret_instr=SLA(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:3]=="SRA"):
        ret_instr=SRA(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:2]=="LW"):
        ret_instr=LW(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:2]=="SW"):
        ret_instr=SW(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:3]=="LUI"):
        ret_instr=LUI(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:3]=="BEQ"):
        ret_instr=BEQ(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:3]=="BNE"):
        ret_instr=BNE(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:3]=="BGT"):
        ret_instr=BGT(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:4]=="BGTE"):
        ret_instr=BGTE(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:3]=="BLE"):
        ret_instr=BLE(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:4]=="BLEQ"):
        ret_instr=BLEQ(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:4]=="BLEU"):
        ret_instr=BLEU(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:4]=="BGTU"):
        ret_instr=BGTU(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:1]=="J"):
        ret_instr=J(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:2]=="JR"):
        ret_instr=JR(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:3]=="JAL"):
        ret_instr=JAL(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:3]=="SLT"):
        ret_instr=SLT(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:4]=="SLTI"):
        ret_instr=SLTI(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:3]=="SEQ"):
        ret_instr=SEQ(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:4]=="MFCL"):
        ret_instr=MFCL(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:4]=="MTCL"):
        ret_instr=MTCL(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:5]=="ADD_S"):
        ret_instr=ADD_S(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:5]=="SUB_S"):
        ret_instr=SUB_S(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:6]=="C_EQ_S"):
        ret_instr=C_EQ_S(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:6]=="C_LE_S"):
        ret_instr=C_LE_S(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:6]=="C_LT_S"):
        ret_instr=C_LT_S(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:6]=="C_GE_S"):
        ret_instr=C_GE_S(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:6]=="C_GT_S"):
        ret_instr=C_GT_S(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:5]=="MOV_S"):
        ret_instr=MOV_S(instrs)
        file_a.write(ret_instr +','+'\n')
    else:
        print(instrs[0:14])
        print("danger danger undefined instruction!!!!")
        
        

file_a.close()
file_b.close()
    
























