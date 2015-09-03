# http://www.pythonchallenge.com/pc/def/linkedlist.php

import urllib2

urlRoot = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=";
starter = "12345";
storage = [starter];

def getExtension(base, extension):
	mergeUrl = base+extension;
	openUrl  = urllib2.urlopen(mergeUrl);
	readUrl  = openUrl.read();
	nothing  = "and the next nothing is"

	if nothing in readUrl:
		for x in range(1, 7):
			if readUrl[-x] == ' ':
				suffix = readUrl[-x+1:]
		return suffix;

	else:
		suffix = str(int(extension)/2);
		print "^^^^^^ POSSIBLE MATCH ^^^^^^";
		return suffix;

# END getExtension

x=1;
while x <= 400:
	nextStorage = getExtension(urlRoot, storage[x-1]);
	if nextStorage not in storage:
		storage.append(nextStorage);
		print str(x) + ": " + nextStorage;
	else:
		print "Found it!"
		break;
	x=x+1;
