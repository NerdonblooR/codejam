def initialize_lawn(row,col):
	lawn = []
	for i in range(row):
		lawn.append([])
		for j in range(col):
			lawn[i].append(0)
	return lawn


def find_min_height(lawn,row,col):
	min_h = 99999999
	for i in range(row):
		for j in range(col):
			if lawn[i][j] < min_h:
				min_h = lawn[i][j]
	return min_h

def find_max_height(lawn,row,col):
	max_h = 0
	for i in range(row):
		for j in range(col):
			if lawn[i][j] > max_h:
				max_h = lawn[i][j]
	return max_h

def restore_lawn(lawn,row,col,min_h):
	for i in range(row):
		for j in range(col):
			if lawn[i][j] == min_h:
			   lawn[i][j] += 1

def check_row(lawn, row, col, min_h):
	for i in range(col):
		if lawn[row][i] != min_h:
			return False
	return True

def check_col(lawn, row, col, min_h):
	for i in range(row):
		if lawn[i][col] != min_h:
			return False
	return True

def is_possible(lawn,row,col,min_h):
	for i in range(row):
		for j in range(col):
			if lawn[i][j] == min_h:
				if not check_row(lawn, i, col, min_h) \
				and not check_col(lawn, row, j, min_h):
					return False
	return True

def final_answer(lawn,row,col,min_h,max_h):
	if min_h == max_h:
		return "YES"
	else:
		while min_h != max_h:
			if not is_possible(lawn,row,col,min_h):
				return "NO"
			restore_lawn(lawn,row,col,min_h)
			min_h = find_min_height(lawn,row,col)
			max_h = find_max_height(lawn,row,col)
		return "YES"

def main():
	fi = open("B-large.in", "r")
	fo = open("output.txt", "w")
	case_num = int(fi.readline().strip())
	for i in range(case_num):
		size = fi.readline().strip().split()
		row = int(size[0])
		col = int(size[1])
		lawn = initialize_lawn(row,col)
		for j in range(row):
			row_content = fi.readline().strip().split()
			print row_content
			for k in range(col):
				lawn[j][k] = int(row_content[k])
		min_h = find_min_height(lawn,row,col)
		max_h = find_max_height(lawn,row,col)
		a = final_answer(lawn,row,col,min_h,max_h)
		fo.write("Case #{0}: {1}\n".format(i+1,a))
		print "Case #{0}: {1}\n".format(i+1,a)
	fi.close()
	fo.close()

if __name__ == '__main__':
	main()