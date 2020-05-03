import os, sys, ctypes

def printAllKLength(set, k): 

	n = len(set) 
	printAllKLengthRec(set, "", n, k) 

def printAllKLengthRec(set, prefix, n, k): 
	
	if (k == 0) : 
		f.write('\n')
		f.write(prefix)
		return

	for i in range(n): 
		newPrefix = prefix + set[i] 

		printAllKLengthRec(set, newPrefix, n, k - 1) 

if __name__ == "__main__": 

	filename = 'output.txt'
	# Change this to the name of your output file. If it does not exist, it will be created.

	k = 4
	# Change this to the desired length of your outputted strings.

	strings = 1
	# Change this to the desired outputted characters.
	# Use `1` for a, b, c...z
	# Use `2` for 0, 1, 2...9
	# Use `3` for 0, 1, 2...9, a...y, z

	alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	characters = alphabet + numbers
	# You can also edit the alphabet or numbers array to whatever characters you'd like.
	# Be sure to delcare your file encoding if you use exotic Unicode characters.

	if (strings == 1):
		strings = alphabet
	elif (strings == 2):
		strings = numbers
	elif (strings == 3):
		strings = characters
	else:
		ctypes.windll.user32.MessageBoxW(0, "`strings` must be a value 1, 2, or 3.", "Fatal Error", 0)
		raise SyntaxError("`strings` must be a value 1, 2, or 3.")

	print("* Opening file...")

	f = open(filename, 'w+')

	print("* Generating strings...")

	printAllKLength(strings, k) 
	
	print("* Done printing strings.")
	print("* Finishing and saving...")

	f.close()

	with open(filename, 'r') as fin:
		data = fin.read().splitlines(True)
	with open(filename, 'w') as fout:
		fout.writelines(data[1:])
	
	print("* Done.")

# https://github.com/3x
# Forked from ChitraNayal's article (https://www.geeksforgeeks.org/print-all-combinations-of-given-length/)
# Code contributed from mgilson on Stack Overflow <3
