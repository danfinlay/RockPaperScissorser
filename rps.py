def bot(my, op):
	moves = ['rock', 'paper', 'scissors']
	total = len(my)
	if total > 2:
		last = zip(my[-2:], op[-2:])
		hist = zip(my, op)
		for i in range(total - 3, -1, -1):
			if hist[i:i+2] == last:
				return moves[(moves.index(op[i+2]) + 1) % 3]
	return moves[total % 3]


player_wins = 0.0

def evaluate_winner(comp_move, player_move):
	if player_move == comp_move:
		return 0.5
		i -= 1
	if player_move == 'rock':
		if comp_move == 'scissors':
			return 1
		if comp_move == 'paper':
			return 0
	if player_move == 'paper':
		if comp_move == 'scissors':
			return 0
		if comp_move == 'rock':
			return 1
	if player_move == 'scissors':
		if comp_move == 'paper':
			return 1
		if comp_move == 'rock':
			return 0



i = 1
comp = []
player = []
while i < 21:
	comp_move = bot(comp, player)
	player_move = raw_input('Round '+str(i)+'.  What is your move?  (Type "rock", "paper", or "scissors" exactly, no caps)')
	comp.append(comp_move)
	player.append(player_move)
	player_wins = player_wins + evaluate_winner(comp_move, player_move)
	print "For round "+str(i)+", you played "+str(player_move)+" and the computer played "+str(comp_move)+"."
	print "You have won "+str(player_wins)+"/"+str(i)+"."
	i+=1