import random 

def play():
    user = input('Choose Rock(R), Scissors(S), or Paper(P): ').lower()
    computer = random.choice(['r', 's', 'p'])
    if user == computer :
        return 'It\'s a tie!'
    if who_wins(user, computer):
        return 'You Win!'
    return 'You Lost'

def who_wins(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

print(play())