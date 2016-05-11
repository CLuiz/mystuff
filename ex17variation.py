from sys import argv
from os.path import exists

script, from_file, to_file = argv

# we could do these two on one line, how?
indata = open(from_file).read()

print "Input file size: %d bytes" % len(indata)
out_file = open(to_file, 'w')
out_file.write(indata)

out_file.close()

