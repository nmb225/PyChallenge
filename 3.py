# http://www.pythonchallenge.com/pc/def/equality.html
import re
bigSmall = open("bigSmall.txt", "r")
readBS = bigSmall.read()

print "".join(re.findall("[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]", readBS))
