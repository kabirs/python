#!/usr/bin/env python3.3
basevalue=15
for a in range(1,basevalue):
	for b in range(1,basevalue) :
		if a>=b :
			print(repr(b).ljust(1)+"x"+repr(a).ljust(1)+"="+repr(b*a).ljust(3),end=' ')
	print('')
