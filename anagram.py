from sys import argv

script, word1, word2 = argv

def length_check(word1, word2):
	return len(word1) == len(word2)
			
def dicter(word):
	tempDict = {}
	for letter in word:
		if letter not in tempDict:
			tempDict[letter] = 1
		else:
			tempDict[letter] += 1
	return tempDict
	
# checker code block was not required
"""
def checker(word1, word2):
	wordDict1 ={}
	wordDict2 ={}
	if length_check(word1, word2) == True:
		wordDict1 = dicter(word1)
		wordDict2 = dicter(word2)
#	print wordDict2
	return wordDict1 == wordDict2
	"""
if (len(word1) == len(word2) and (dicter(word1) == dicter(word2))):
	print "The strings %s and %s are anagrams." % (word1, word2) 
else:
	print "The strings %s and %s are not anagrams." % (word1, word2)


