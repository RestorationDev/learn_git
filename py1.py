

# given an array of int, and int target, return indices of the numbers such 
# that they add up to the target


import collections

def add_no2(nums, target):
	#nums = [2, 7, 11, 15]
	
	l_pairs = []
	s_pairs = ()

	for i, v in enumerate(nums):
		print(target, v, target - v)

		delta = target - v

		if delta in nums:
			l_pairs.append(v)
			l_pairs.append(delta)

	print(l_pairs)	


def add_no3(nums, target):

	pairs = {}

	for i, v in enumerate(nums):
		delta = target - v

		if delta not in pairs:
			pairs[delta] = i
		else:
			return [pairs[delta], i]


def add_no1(nums, target):
	
	s_pairs = ()
	l_pairs = []

	for i, v1 in enumerate(nums):
		for j, v2 in enumerate(nums):
			if i == j:
				continue
			print(i, j)
			if (v1 + v2) == target:
				print('these two numbers add up ', i, j)
				l_pairs.append(i)
				l_pairs.append(j)
				s_pairs = set(l_pairs)

	print(s_pairs)

nums = [2,7,11,15]
#nums = [3,3]
nums = [2,3,4]
target = 6
add_no2(nums, target)
print(add_no3(nums, target))




