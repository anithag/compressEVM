import numpy as np
import binascii as ba
import os
import math

#fileName="creations.dat"
#with open(fileName, mode='rb') as file: # b is important -> binary
#        fileContent = bytearray(file.read())

#unique, counts = np.unique(fileContent, return_counts=True)

#opfreq = np.asarray((unique, counts)).T

opcode_table = {
                0x00:"stop",
                0x01:"add",
                0x02:"mul",
                0x03:"sub",
                0x04:"div",
                0x05:"sdiv",
                0x06:"mod",
                0x07:"smod",
                0x08:"addmod",
                0x09:"mulmod",
                0x0a:"exp",
                0x0b:"signextend",
                0x10:"lt",
                0x11:"gt",
                0x12:"slt",
                0x13:"sgt",
                0x14:"eq",
                0x15:"iszero",
                0x16:"and",
                0x17:"or",
                0x18:"xor",
                0x19:"not",
                0x1a:"byte",
                0x20:"sha3",
                0x30:"address",
                0x31:"balance",
                0x32:"origin",
                0x33:"caller",
                0x34:"callvalue",
                0x35:"calldataload",
                0x36:"calldatasize",
                0x37:"calldatacopy",
                0x38:"codesize",
                0x39:"codecopy",
                0x3a:"gasprice",
                0x3b:"extcodesize",
                0x3c:"extcodecopy",
                0x40:"blockhash",
                0x41:"coinbase",
                0x42:"timestamp",
                0x43:"number",
                0x44:"difficulty",
                0x45:"gaslimit",
                0x50:"pop",
                0x51:"mload",
                0x52:"mstore",
                0x53:"mstore8",
                0x54:"sload",
                0x55:"sstore",
                0x56:"jump",
                0x57:"jumpi",
                0x58:"pc",
                0x59:"msize",
                0x5a:"gas",
                0x5b:"jumpdest",
                0x60:"push1",
                0x61:"push2",
                0x62:"push3",
                0x63:"push4",
                0x64:"push5",
                0x65:"push6",
                0x66:"push7",
                0x67:"push8",
                0x68:"push9",
                0x69:"push10",
                0x6a:"push11",
                0x6b:"push12",
                0x6c:"push13",
                0x6d:"push14",
                0x6e:"push15",
                0x6f:"push16",
                0x70:"push17",
                0x71:"push18",
                0x72:"push19",
                0x73:"push20",
                0x74:"push21",
                0x75:"push22",
                0x76:"push23",
                0x77:"push24",
                0x78:"push25",
                0x79:"push26",
                0x7a:"push27",
                0x7b:"push28",
                0x7c:"push29",
                0x7d:"push30",
                0x7e:"push31",
                0x7f:"push32",
                0x80:"dup1",
                0x81:"dup2",
                0x82:"dup3",
                0x83:"dup4",
                0x84:"dup5",
                0x85:"dup6",
                0x86:"dup7",
                0x87:"dup8",
                0x88:"dup9",
                0x89:"dup10",
                0x8a:"dup11",
                0x8b:"dup12",
                0x8c:"dup13",
                0x8d:"dup14",
                0x8e:"dup15",
                0x8f:"dup16",
                0x90:"swap1",
                0x91:"swap2",
                0x92:"swap3",
                0x93:"swap4",
                0x94:"swap5",
                0x95:"swap6",
                0x96:"swap7",
                0x97:"swap9",
                0x99:"swap9",
                0x99:"swap10",
                0x9a:"swap11",
                0x9b:"swap12",
                0x9c:"swap13",
                0x9d:"swap14",
                0x9e:"swap15",
                0x9f:"swap16",
                0xa0:"log0",
                0xa1:"log1",
                0xa2:"log2",
                0xa3:"log3",
                0xa4:"log4",
                0xf0:"create",
                0xf1:"call",
                0xf2:"callcode",
                0xf3:"return",
                0xf4:"delegatecall",
                0xff:"suicide"
        }
inv_opcode_table = {v: k for k, v in opcode_table.items()}
#data = {}
#for x in opfreq:
#    if x[0] in opcode_table:
#      data[opcode_table[x[0]]]= x[1]
#
#sortedopcodes = sorted(data.items(), key=lambda x:x[1])

# disable printing sorted opcodes for now
#for y in sortedopcodes:
#    print(y[1], "\t", y[0])


#Compression testing with huffman codes
#hcode_table = {}
#fileName="huffmanopcodes.txt"
#with open(fileName, mode='r') as file: 
#    for line in file:
#            token = str.split(line)
#            hcode_table[inv_opcode_table[token[0]]] = token[1]

#compute the compression size with huffman codes
#opcode: opcode, counts
#Algorithm: get the huffman code and its size. Multiply it with counts

##comprsize = 0
##for idx in opfreq:
##   if idx[0] in opcode_table:
##        #get the opcode
##        opcode = opcode_table[idx[0]]
##        #get the huffman code
##        hcode = hcode_table[opcode]
##        hsize = len(hcode)
##        comprsize = comprsize+ (hsize * idx[1])
##   else:
##        comprsize = comprsize + (8 * idx[1]) 
##
### Original size in bytes
##origsize=os.stat('creations.dat').st_size
##print("Original Size:", origsize) 
##
###compressed size in bytes
##comprsize = math.ceil(comprsize/8)
##print("Compressed Size:", comprsize)
##
###savings
##print("Compression ratio:", comprsize/origsize)
##
