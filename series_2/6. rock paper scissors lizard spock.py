a = str(input())
b = str(input())

if a == b:
    print('draw')
elif a == 'rock' and (b == 'lizard' or b == 'scissors'):
    print('player1 wins')
elif a == 'paper' and (b == 'rock' or b == 'Spock'):
    print('player1 wins')
elif a == 'scissors' and (b == 'paper' or b == 'lizard'):
    print('player1 wins')
elif a == 'lizard' and (b == 'Spock' or b == 'paper'):
    print('player1 wins')
elif a == 'Spock' and (b == 'scissors' or b == 'rock'):
    print('player1 wins')
else:
    print('player2 wins')