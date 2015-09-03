# http://www.pythonchallenge.com/pc/def/map.html
import sys

decode = list("pc def map")

def bumpTwo(decodeList):
	for i in range(0, len(decodeList)):
		toAscii = ord(decodeList[i])

		if (toAscii in range(97, 120)):
			addTwo = str(chr(ord(decodeList[i]) + 2))
		
		elif (toAscii == 32 or toAscii == 46):
			addTwo = str(chr(ord(decodeList[i])))
		else:
			addTwo = str(chr(ord(decodeList[i]) - 24))
		sys.stdout.write(addTwo)

bumpTwo(decode)

#printMe = bumpTwo(decode)
#print ''.join(printMe)
