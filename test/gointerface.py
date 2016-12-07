#!/usr/bin/python
import rlp
from gen_freq_opcode import opcode_table
from gen_freq_opcode import inv_opcode_table
from bitarray import bitarray
import binascii
import sys,socket

TCP_IP = '127.0.0.1'
TCP_PORT = 5005

huffman_file = 'huffmanopcodes.txt'

def start_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_IP, TCP_PORT))
    s.listen(1)
    print 'Listening on %s:%d' % (TCP_IP, TCP_PORT)
    return s

def accept_and_handle(s, hcode_table):
    conn, addr = s.accept()
    print 'Accepted connection from ', addr
    f = conn.makefile()

    while True:
        hin = f.readline().strip()
        if hin == '':
            print "Connect closed"
            break
        bc = binascii.unhexlify(hin)
        huff = assign_opcode(bc, hcode_table)
        hout = binascii.hexlify(huff.tobytes()) + '\n'
        print hout
        s.sendall(hout)
    f.close()

#Compression testing with huffman codes
def init_hc_table(filename):
    hcode_table = {}
    with open(filename, mode='r') as file:
        for line in file:
                token = str.split(line)
                hcode_table[inv_opcode_table[token[0]]] = token[1]
    return hcode_table

def assign_opcode(bc, hcode_table):
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

if __name__ == '__main__':
    hcode_table = init_hc_table(huffman_file)
    s = start_server()
    while True:
        try:
            accept_and_handle(s, hcode_table)
        except (KeyboardInterrupt, SystemExit):
            break
    print 'Shutdown'
    s.close()
    sys.exit(0)
