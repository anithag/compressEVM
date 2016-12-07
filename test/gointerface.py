#!/usr/bin/python
import rlp
from gen_freq_opcode import opcode_table
from gen_freq_opcode import inv_opcode_table
from bitarray import bitarray
from optparse import OptionParser
import binascii
import sys

parser = OptionParser()
parser.add_option("-b", "--bytecode", dest="bytecode",
                          help="EVM bytecode as hex string")

(options, args) = parser.parse_args()
hbytecode = options.bytecode
#hbytecode = sys.argv[1]


#Compression testing with huffman codes
hcode_table = {}
fileName="/Users/anithagollamudi/cs222/compressEVM/test/huffmanopcodes.txt"
with open(fileName, mode='r') as file: 
    for line in file:
            token = str.split(line)
            hcode_table[inv_opcode_table[token[0]]] = token[1]

def assign_opcode(bc):
    l = list(bc)
    newl = bitarray()
    for i in l:
        x = ord(i)
        if x in opcode_table:
            #print hcode_table[x], ":", opcode_table[x]
            newl.extend(hcode_table[x])
        else:
            b = bin(x)
            s = str(b)
            newl.extend(s[2:])
    return newl


bytecode = binascii.unhexlify(hbytecode)
#print "Hexlified bytecode", hbytecode
#print "Unhexlified bytecode", bytecode
#print "end"
newl= assign_opcode(bytecode)
newbytecode = newl.tobytes()
print newbytecode
#print "hello world"
