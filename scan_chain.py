#!/usr/bin/env python

import sys, time
from threading import Thread
from ethjsonrpc import EthJsonRpc

wait_start = 0.01
wait_ceiling = 1.0

def append_hex(f, hex_string):
    f.write(hex_string.decode("hex"))

def run_scan_thread(n, start, end):
    range_size = end-start+1
    c = EthJsonRpc('127.0.0.1', 8545)
    print 'Worker {:d} started, assigned blocks #{:d} -- #{:d}'.format(n,start,end)

    f1 = open('msg_calls_{:02d}.dat'.format(n), 'ab')
    f2 = open('creations_{:02d}.dat'.format(n), 'ab')

    for bi in range(start, end+1):
        w = wait_start
        bc = bi - start
        if bc % 1000 == 0:
            print 'Worker {:d}: processed {:d} blocks {:.2f}%'.format(n,bc,float(bc*100.0)/float(range_size))
        while True:
            try:
                b = c.eth_getBlockByNumber(bi)
            except:
                time.sleep(w)
                w *= 2
                if w > wait_ceiling:
                    w = wait_ceiling
                continue
            break
        t = b['transactions']
        if len(t) == 0:
            continue
        for tx in t:
            # message call txn
            if tx['value'] == '0x0':
                append_hex(f1, tx['input'][2:])
            # contract creation txn
            if tx['to'] == None:
                append_hex(f2, tx['input'][2:])
    f1.close()
    f2.close()

if __name__ == '__main__':
    # spread jobs to workers
    if len(sys.argv) != 2:
        print 'Usage: {} [nthreads]'.format(sys.argv[0])
        exit()
    ntr = int(sys.argv[1])

    highest_block_no = 1843190

    range_size = highest_block_no/ntr

    cnt = 0
    range_start = 0
    range_end = range_size
    ths = []
    while True:
        ths.append(Thread(target=run_scan_thread, args=(cnt,range_start,range_end)))
        if range_end == highest_block_no:
            break
        range_start = range_end + 1
        range_end = range_start + range_size
        if range_end > highest_block_no:
            range_end = highest_block_no
        cnt += 1
    for t in ths:
        t.start()
    for t in ths:
        t.join()

    print 'All workers finished.'
