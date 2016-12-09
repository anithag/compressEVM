#!/usr/bin/env python

import rlp,sys

def get_evm_bytes(fh):
    data = fh.read()

    sz = 0
    offset = 0
    while offset < len(data):
        block, offset = rlp.codec.consume_item(data, offset)
        for tx in block[1]:
            if tx[3] == '':
                sz += len(tx[5])
    return sz

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'Supply file name!'
        exit()
    f = open(sys.argv[1], 'rb')
    print '%d bytes of EVM bytecode' % get_evm_bytes(f)
    f.close()
