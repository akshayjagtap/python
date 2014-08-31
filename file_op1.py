import sys
import time

y = str(sys.argv)
var = [sys.argv[1],sys.argv[2],sys.argv[3]]
t = time.time()
print t

for name in var:
	name = name + '_%s' % (t) + '.txt'
	print name
	file = open (name,'w') 
	file.write("This file is for me.")
	file.close()
