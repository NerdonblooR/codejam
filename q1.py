def initialize_gameboard():
	game_board = []
	for i in range(4):
		game_board.append([0,0,0,0])
	return game_board

def game_is_completed(game_board):
	return game_board[0].count('.') == 0 and game_board[1].count('.') == 0 \
	and game_board[2].count('.') == 0 and game_board[3].count('.') == 0 


def row_winner(game_board):
	for i in range(4):
		collection = [game_board[i][0], game_board[i][1],game_board[i][2],game_board[i][3]]
		if collection.count('X') == 4 or (collection.count('X') == 3 and collection.count('T') == 1):
			return "X won"
		elif collection.count('O') == 4 or (collection.count('O') == 3 and collection.count('T') == 1):
			return "O won"
	return "Draw"

def col_winner(game_board):
	for i in range(4):
		collection = [game_board[0][i], game_board[1][i],game_board[2][i],game_board[3][i]]
		if collection.count('X') == 4 or (collection.count('X') == 3 and collection.count('T') == 1):
			return "X won"
		elif collection.count('O') == 4 or (collection.count('O') == 3 and collection.count('T') == 1):
			return "O won"
	return "Draw"

def diag_winner(game_board):
	collection = [game_board[0][0],game_board[1][1],game_board[2][2],game_board[3][3]]
	if collection.count('X') == 4 or (collection.count('X') == 3 and collection.count('T') == 1):
		return "X won"
	elif collection.count('O') == 4 or (collection.count('O') == 3 and collection.count('T') == 1):
		return "O won"
	collection = [game_board[0][3],game_board[1][2],game_board[2][1],game_board[3][0]]
	if collection.count('X') == 4 or (collection.count('X') == 3 and collection.count('T') == 1):
		return "X won"
	elif collection.count('O') == 4 or (collection.count('O') == 3 and collection.count('T') == 1):
		return "O won"
	return "Draw"

def winner(game_board):
	winners = [row_winner(game_board), col_winner(game_board), diag_winner(game_board)]
	for winner in winners:
		if winner != "Draw":
			return winner
	if game_is_completed(game_board):
		return "Draw"
	else:
		return "Game has not completed"



def main():
	fi = open("A-large.in", "r")
	fo = open("output.txt", "w")
	case_num = int(fi.readline().strip())
	for i in range(case_num):
		game_board = initialize_gameboard()
		for j in range(4):
			row = fi.readline().strip()
			for k in range(4):
				game_board[j][k] = row[k]
		w = winner(game_board)
		fo.write("Case #{0}: {1}\n".format(i+1, w))
		print "Case #{0}: {1}\n".format(i+1, w)
		fi.readline()
	fi.close()
	fo.close()




if __name__ == '__main__':	
	main()