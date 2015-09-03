# http://www.pythonchallenge.com/pc/def/ocr.html
import sys
openMess = open("mess.txt", "r")
readMess = openMess.read()
for i in range(0, len(readMess)):
	if (ord(readMess[i]) >= 97 and ord(readMess[i]) <= 122):
		sys.stdout.write(readMess[i])
sys.stdout.write("\n")
