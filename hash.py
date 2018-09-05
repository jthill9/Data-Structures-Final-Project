#!/usr/bin/env python3

import sys

def hash(msg):
	#msg = sys.argv[1]
	hsum = 0 # hash sum

	# Pad msg to make its length divisible by 4
	while len(msg) % 4:
		msg = msg + ' '


	for i in range(0, len(msg), 4):
		psum = 0 # partial sum
		charvals = [(ord(c)*16777619)%128 for c in msg[i:i+4]]
		if i % 16 < 4:
			for j in range(4):
				psum = (psum * 16777619) ^ charvals[j]

		elif i % 16 < 8:
			for j in range(4):
				psum = psum ^ ((psum << 5) + (psum >> 2) + charvals[j])

		elif i % 16 < 12:
			for j in range(4):
				psum = 33 * psum ^ charvals[j]

		elif i % 16 < 16:
			for j in range(4):
				psum = ((psum << 5) * charvals[j])

		hsum = hsum + ((psum**50)*51)%(1<<128) ^ psum

	hsum>>64

	return (hex(hsum)[2:])
