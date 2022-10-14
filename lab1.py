# 2.1.

def f1(l):
	max = None
	for x in l:
		if max is None or max < x:
			max = x
	return max


print(f1([1,4,2,6,4,5]))

# 2.2.
def f2(l, start=0, stop=-1):
	max = None
	for x in l[start:stop]:
		if max is None or max < x:
			max = x
	return max

print(f2([1,4,2,6,4,5,7], 2, 4))

# 2.3.

def longest_positive(l:list):
	max_len = 0
	current_len = 0
	max_start = 0
	current_start = 0

	for i in range(len(l)):
		if l[i] >= 0:
			current_len += 1
		else:
			if current_len > max_len:
				max_len = current_len
				max_start = current_start
			current_start = i + 1
			current_len = 0

	# this check is in case the last element is positive:
	if current_len > max_len:
		max_len = current_len
		max_start = current_start

	return l[max_start: max_start + max_len]


print(longest_positive([1,3,-1,2,0,1,5,4,-2,4,5,-3,0,1,2]))

# 2.4.

def is_palindrome(l):
	half = len(l) // 2

	first_half = l[:half]
	second_half = l[-half:]

	second_half.reverse()

	return first_half == second_half

# another option

def is_palindrome2(l):
	return l == l[::-1]

print(is_palindrome([1,2,3,4,3,2,1])) # true
print(is_palindrome([1,2,3,3,5,4,3,2,1])) # false
print(is_palindrome2([1,2,3,3,2,1])) # true
print(is_palindrome2([1,2,3,3,4,3,2,1])) # false

# 2.5.

def longest_sequence(l):
	s = []
	longest = []
	for x in l:
		if not s or x != s[0]: # if s is empty or x is not the same as the contents of s
			if len(longest) < len(s):
				longest = s
			s = [x]
		else:
			s.append(x)

	if len(longest) < len(s):
		longest = s
	return longest

print(longest_sequence([1,1,2,2,2,2,1,1,1,1,1,2,2,2,2]))

# 2.6.

def set_ify_string(s):
	return "".join(set(list(s)))

# 2.7.

from functools import reduce

def getYouth(l):
    # this function computes the age of a given CNP
    def age(cnp):
        # conversion to integer of the two-character year code
        if int(cnp[1:3]) <= 22:
            return 2022 - int("20"+cnp[1:3])
        else:
            return 2022 - int("19"+cnp[1:3])

    # computing the average ages (a map could have also been used)
    avg = reduce(lambda a,b:a+b, [age(x[-1]) for x in l]) / len(l)

    #print([(ln,age(cnp)) for (fn,ln,cnp) in l], avg)
    # we return the last name and the age of the filtered list l
    return [(ln,age(cnp)) for (fn,ln,cnp) in l if cnp[0]=='2' and age(cnp) <= avg]

print(getYouth([ ("Mary", "Smith", "2030602123456"), ("Anne", "Doe", "2121092123456"), ("Matei", "Dan", "1121202123456"), ("Maggie", "Byrne", "2121078123456")]))


# PRACTICE

input_file_name = "python_practice_input.txt"
streets:'dict[tuple[int,str],set[int]]' = {}

def read_input():
	f = open(input_file_name)
	txt = f.read()
	lines = txt.split("\n")
	node_count = int(lines[0])

	for ln in lines[1:]:
		[start, color, end] = ln.split(" ")
		streets[int(start), color] = streets.get((int(start),color), set()).union([int(end)])



def get_result(start:int, colors:str):
	reachable  = current = set([start])

	for c in colors:
		new = set()
		for x in current:
			new.update(streets.get((x,c), set()))

		reachable .update(new)
		current = new

	print(reachable)
read_input()
get_result(0, "rrg")