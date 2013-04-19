import math

def is_fair(num):
	reverse = 0
	original_num = num
	if num % 10 == 0:
		return False
	while num >= 10:
		reverse += num % 10;
		num /= 10
		reverse *= 10
	reverse += num;
	return reverse == original_num

def is_square(apositiveint):
  x = apositiveint // 2
  seen = set([x])
  while x * x != apositiveint:
    x = (x + (apositiveint // x)) // 2
    if x in seen: return False
    seen.add(x)
  return True

def count_fair(start, end):
	count = 0
	fair_num = 1
	while fair_num < start
	while start <= end:
		if is_fair(start) and is_square(start) and is_fair(int(math.sqrt(start))):
			print start
			fair_num += 1
		start += 1
	return fair_num

def main():
	fi = open("C-large-1.in", "r")
	fo = open("output.txt", "w")
	case_num = int(fi.readline().strip())
	for i in range(case_num):
		case = fi.readline().strip().split()
		start = int(case[0])
		end = int(case[1])
		a = count_fair(start,end)
		fo.write("Case #{0}: {1}\n".format(i+1, a))
		print "Case #{0}: {1}\n".format(i+1, a)
	fi.close()
	fo.close()

if __name__ == '__main__':
	main()