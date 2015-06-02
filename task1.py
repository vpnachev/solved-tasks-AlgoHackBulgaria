import sys

def is_palindrom(word):
	return word == word[::-1]

def rotate_word(word):
	return word[1:]+word[0]

def solve_problem():
	word = input()
	output = "NONE"
	for index in range(len(word)):
		if is_palindrom(word):
			output = word
			print(word)
		word = rotate_word(word)
	if output == "NONE":
		print(output)

if __name__ == "__main__":
    solve_problem()