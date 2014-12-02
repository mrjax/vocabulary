#!/usr/bin/python

import sys, random

if len(sys.argv) > 1:
	numWords = int(sys.argv[1])
else:
	print("Needs number of output words")
	numWords = int(input('->'))

if len(sys.argv) > 2:
	numLines = int(sys.argv[2])

random.seed()





input = open('input.txt', 'r')
#input.read(), input.read(10) reads in 10 chars
#input.tell() returns place in file
#input.seek(offset[, from]), goes offset positions away in file, optionally "from" some reference point.  0 for start of file, 1 for current position, 2 for end of file


output = open('output.txt', 'r+')
#output.write(' ')
#output.close()

def findLargest(ingoes):
	longest = 1
	for element in ingoes:
		if len(element) > longest:
			longest = len(element)
	return longest

def printClean(str, num, out):
	diff = num - len(str)
	
	#print(str, end='')
	out.write(str)

	for it in range(diff):
		#print(' ', end='')
		out.write(' ')

	#print(' ', end='')
	out.write(' ')

text = input.read()
lines = text.split('\n')
newItems = lines[0].split()
oldItems = lines[1].split()

result = []

i = numWords
while(i):
	rand = random.randint(0,100)
	if rand < 70:
		rand = random.randint(0, len(newItems) -1)
		result.append(newItems[rand])
	else:
		rand = random.randint(0, len(oldItems) -1)
		result.append(oldItems[rand])
	i-=1


largest1 = findLargest(newItems)
largest2 = findLargest(oldItems)

if largest1 > largest2:
	largest = largest1
else: 
	largest = largest2


if len(sys.argv) > 2:
	j = 0
	while j < len(result):
		k = 0
		while k < numLines:
			
			printClean(result[j], largest, output)

			j+=1
			k+=1
		#print('')
		output.write('\n')
else:
	l = 0
	while l < len(result):
		output.write(result[l] + ' ')
		#print(result[l])
		l += 1



#output.write()
output.close()

