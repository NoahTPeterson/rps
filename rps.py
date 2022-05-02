from random import choice
moves = ['rock', 'paper', 'scissors']
player_picks = []
total_games = 0
wins = 0
losses = 0
ties = 0

while True:
    #computer move
    our_move = choice(moves)
    
    rock_count = player_picks.count("rock")
    paper_count = player_picks.count("paper")
    scissors_count = player_picks.count("scissors")
    
    if rock_count > paper_count and rock_count > scissors_count:
        our_move = 'paper'
    elif paper_count > rock_count and paper_count > scissors_count:
        our_move = 'scissors'
    elif scissors_count > rock_count and scissors_count > paper_count:
        our_move = 'rock'  
        
    
    #print(f"Rocks: {rock_count} Paper: {paper_count} Scissors: {scissors_count}")
    
    #player move
    player_move = str(input("Enter Choice (rock, paper or scissors)"))
    while player_move not in moves:
        print("Please enter a valid move")
        player_move = str(input("Enter Choice (rock, paper or scissors)"))
    print("Computer chose " + our_move)
    assert player_move in moves, f'{player_move} not in {moves}'
    player_picks.append(player_move)
    total_games += 1
    
    #game logic
    if player_move == 'rock':
        if our_move == 'rock':
            print("Tie")
            ties += 1
        elif our_move == 'paper':
            print("Computer Wins")
            losses += 1
        elif our_move == 'scissors':
            print("Player Wins")
            wins += 1
    elif player_move == 'paper':
        if our_move == 'rock':
            print("Player Wins")
            wins += 1
        elif our_move == 'paper':
            print("Tie")
            ties += 1
        elif our_move == 'scissors':
            print("Computer Wins")
            losses += 1
    elif player_move == 'scissors':
        if our_move == 'rock':
            print("Computer Wins")
            losses += 1
        elif our_move == 'paper':
            print("Player Wins")
            wins += 1
        elif our_move == 'scissors':
            print("Tie")  
            ties += 1
    else:
        print("Please enter a valid answer")
    #print 
    print(f"Total Player Wins: {wins} Total Player Losses: {losses} Total Ties: {ties} Total Games: {total_games} Computer Winrate: {losses/total_games:.1%}")
    #print(player_picks)