"""
File: largest_digit.py
Name:
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	This function is to find the largest digit
	:param n:(str) the number to find the largest digit
	:return :(int) the largest digit
	"""
	return find_largest_digit_helper(abs(n), 0)


def find_largest_digit_helper(n, lar):
	"""
	This is the help function to find the largest digit
	:param n  :(int) the number to find the largest digit
	:param lar:(int) found the largest digit
	:return   :(int) the largest digit
	"""
	if n < lar:
		return lar
	else:
		if n % 10 > lar:
			lar = n % 10

		return find_largest_digit_helper(int(n/10), lar)


if __name__ == '__main__':
	main()
