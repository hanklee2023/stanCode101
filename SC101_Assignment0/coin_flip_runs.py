"""
File: coin_flip_runs.py
Name:
-----------------------
This program should simulate coin flip(s)
with the number of runs input by users.
A 'run' is defined as consecutive results
on either 'H' or 'T'. For example, 'HHHHHTHTT'
is regarded as a 2-run result.
Your program should stop immediately after your
coin flip results reach the runs!
"""

import random as r


def main():

	print("Let's flip a conin!")
	c = int(input("Number of runs: "))

	# num_run = total assigned run times
	# last_coin is the last result of coin
	# consecutive_coin is consecutive result for the same coin = 1
	# random coin 0 = H, 1 = T
	num_run = c
	last_coin = -1
	consecutive_coin = 0

	while num_run != 0:
		result = r.randint(0,1)

		if last_coin == -1:
			last_coin = result
			if result == 0:
				print("H", end='')
			else:
				print("T", end='')

		elif last_coin == result and consecutive_coin != 1:
			consecutive_coin = 1
			if result == 0:
				print("H", end='')
			else:
				print("T", end='')
			num_run = num_run - 1


		elif last_coin != result:
			consecutive_coin = 0
			last_coin = result
			if result == 0:
				print("H", end='')
			else:
				print("T", end='')
		else:
			pass

	print("")

###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
