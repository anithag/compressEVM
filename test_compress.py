import rlp

f = open("compresstestnet.bin", "rb")
data = f.read()

offset = 0
while offset < len(data):
    group, offset = rlp.codec.consume_item(data, offset)
    for b in group[1]:
        #if len(b[2]) >= 1:
        #    print offset
        #    print b[2][0]
        print b[0][-3]
