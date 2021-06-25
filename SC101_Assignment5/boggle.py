"""
File: boggle.py
Name:
----------------------------------------
TODO:
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
ROW = 4

# Global variable
# dict in vocabulary order dictionary is 2 layer dict:
# the first layer key is the first char, and the 2nd layer of key is the first 2 chars.
dict = {}


def main():
	# Design a board (dict) to store all input chars in <Key>:<Item> pair, and the detail is below
	# <Key> - a (tuple) to store position. such as (0,0)
	# <Item> - a (dict) to store required information
	# - char is to store input value(char)
	# - traverse is to check whether this char is used later
	# - checked is the parameter to verify the position backtrack whole route

	board = {}
	found_lst = []  	# found_lst to store found vocabulary
	execution = True 	# check whether input error

	read_dictionary()

	for row in range(ROW):
		line = input(f'{row + 1} row of letters: ')
		char_lst = line.split(' ')
		if not check_letters(char_lst):
			print("Illegal input")
			execution = False
			break
		else:
			for col in range(ROW):
				board[(row, col)] = {}
				board[(row, col)]['char'] = char_lst[col].lower()
				board[(row, col)]['traverse'] = False
				board[(row, col)]['checked'] = False

	if execution:
		show_vocabulary(board, found_lst)


def check_letters(char_lst):
	"""
	This function checks whether any in-correct char in char list. I consider below case
	- element of char_lst equals to ROW
	- Only one char in each element from char_lst
	- The char is Alphabet rather than other type (like number)
	:param char_lst: (list) A list of char to check whether input is right
	:return: (bool) If the input is correct
	"""
	if len(char_lst) != ROW:
		return False

	for char in char_lst:
		if len(char) != 1:
			return False
		elif not char.isalpha():
			return False

	return True


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	global dict

	with open(FILE, 'r') as r:
		for item in r:
			if item[0] in dict:
				pass
			else:
				dict[item[0]] = {}

			if len(item[0:len(item) - 1]) < 2:
				dict[item[0]][item[0]] = []
				dict[item[0]][item[0]].append(item[0:len(item) - 1])
			elif item[0:2] in dict[item[0]]:
				dict[item[0]][item[0:2]].append(item[0:len(item) - 1])
			else:
				dict[item[0]][item[0:2]] = []
				dict[item[0]][item[0:2]].append(item[0:len(item) - 1])


def show_vocabulary(board, result_lst):
	"""
	This function is to search all vocabulary
	:param board:(dict) a dictionary to store boggle information
	:param result_lst:(list) to store found vocabulary
	"""
	# Helper function to check word
	# Iterate each position as starting point
	for key in board:
		find_word(board, key, "", ROW, result_lst)
	print(f'There are {len(result_lst)} words in total.')


def find_word(board, pos, current_string, len_limit, result_lst):
	"""
	This function is the helper function to search all vocabulary in boggle board through
	backtracking algorithm
	:param board			:(dict) a dictionary to store boggle information
	:param pos				:(tuple) to store current position for char
	:param current_string	:(str) current combined string
	:param len_limit		:(int) the minimum length for searched string
	:param result_lst		:(list) to store found vocabulary
	"""

	global dict

	# Base case is that all elements in board are checked
	if check_board(board):
		return

	else:
		# Choose
		board[pos]['traverse'] = True
		current_string += board[pos]['char']

		if len(current_string) >= 4 and current_string not in result_lst:
			if current_string in dict[current_string[0]][current_string[0:2]]:
					print("Found " + "\"" + current_string + "\"")
					result_lst.append(current_string)

		# Explore
		for key in get_adjacent(pos, board):
			if has_prefix(current_string):
				find_word(board, key, current_string, len_limit, result_lst)

		# Un-choose
		if len(current_string) > 1:
			current_string = current_string[0:len(current_string) - 1]
		else:
			current_string = ""
			board[pos]['checked'] = True

		board[pos]['traverse'] = False

def get_adjacent(key, board):
	"""
	This function is to collect adjacent positions (including self) for traverse
	:param key		:(tuple) a position for board
	:param board	:(dict) a dictionary to store boggle information
	:return adj_lst	:(list) a list for all adjacent positions not traversed
	"""
	adj_lst = []
	x, y = key

	for i in [0, -1, 1]:
		for j in [0, -1, 1]:
			if y + j > 3 or y + j < 0 or x + i > 3 or x + i < 0:
				pass
			elif j == 0 and i == 0:
				pass
			else:
				if not board[(x + i, y + j)]['traverse']:
					adj_lst.append((x + i, y + j))
				else:
					pass

	return adj_lst


def check_board(board):
	"""
	This function is to check whether whole board is checked
	:param board:(dict) a dictionary to store boggle information
	:return		:(bool) if all elements in board are checked
	"""
	for key in board:
		if not board[key]['checked']:
			return False

	return True


def has_prefix(sub_s):
	"""
	This function is find whether any string in dict contains sub string
	:param sub_s:(str) input for sub string to search in dictionary
	:return		:(bool) if sub_s is composed of strings in dict
	"""
	global dict

	if sub_s[0] in dict:
		if len(sub_s) == 1:
			return True
		if sub_s[0:2] in dict[sub_s[0]]:
			for string in dict[sub_s[0]][sub_s[0:2]]:
				if string.startswith(sub_s):
					return True
	return False


if __name__ == '__main__':
	main()
