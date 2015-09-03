# http://www.pythonchallenge.com/pc/def/peak.html

import pickle, urllib2

openURL = urllib2.urlopen("http://www.pythonchallenge.com/pc/def/banner.p");
readURL = openURL.read();
pickles = pickle.loads(readURL);

print '\n'.join(''.join(p[0] * p[1] for p in row) for row in pickles)
