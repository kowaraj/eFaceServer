import sys

f_in = open(sys.argv[1], 'r')

l1 = f_in.readlines()
l2 = [x[16:-1] for x in l1]

a1 = '\t'.join(l2).split('\t')
b1 = [int(x,16) for x in a1]
b2 = bytearray(b1)

f_out = open(sys.argv[2], 'w')
for x in b2:
    f_out.write(hex(x))
    f_out.write('\n')