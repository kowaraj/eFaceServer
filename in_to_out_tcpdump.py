import sys

f_in = open(sys.argv[1], 'r')

l1 = f_in.readlines()
#print(l1)
l2 = [x[9:-19] for x in l1]

print(l2)
a1 = ' '.join(l2).split(' ')
print(a1)
a2 = ''.join(a1)
print(a2)
b1 = [ int(a2[i*2:i*2+2], 16) for i in range(int( (len(a2)+1)/2 ) )]
#[ int(a2[i*2:i*2+1], 16) for i in range(int( (len(a2)+1)/2 ))]
b2 = bytearray(b1)

f_out = open(sys.argv[2], 'w')
for x in b2:
    f_out.write(r'\x{0:02x}'.format(x))
    #f_out.write('\n')