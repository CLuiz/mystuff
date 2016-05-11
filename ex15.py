# imports argv functionality from the argv module
from sys import argv

# assigns the number of arguments 
script, filename = argv

# open the second argument and saves it as txt
txt = open(filename)

# prints a message about the input filename
print "Here's your file %r:" % filename

# prints text of txt
print txt.read()

# prompts for filename for a raw_input call
print "Type filename again:"
file_again = raw_input("> ")

# same as 8
txt_again = open(file_again)

print txt_again.read()

txt.close()
txt_again.close()