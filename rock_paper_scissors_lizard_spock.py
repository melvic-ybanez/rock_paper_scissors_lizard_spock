'''
Created on Sep 14, 2014

@author: melvic

It's very simple

Scissors cuts paper
Paper covers rock
Rock crushes lizard
Lizard poisons Spock
Spock smashes scissors
Scissors decapitates lizard
Lizard eats paper
Paper disproves Spock
Spock vaporizes rock

And as it always has been

Rock crushes scissors
'''

def winner(shape1, shape2):
    res = (shape1 - shape2) % 5
    if res > 2:
        return shape2
    elif res > 0:
        return shape1
    else:
        return None
    
def normalize(x):
    xs = {0: 0, 1: 2, 2: 4, 3: 3, 4: 1}
    return xs[x - 1]
    
if __name__ == '__main__':
    print '1 - Rock'
    print '2 - Paper'
    print '3 - Scissors'
    print '4 - Lizard'
    print '5 - Spock'
    
    shape1 = raw_input("Player 1's Shape: ")
    shape2 = raw_input("Player 2's Shape: ")
    
    shape1 = normalize(int(shape1))
    shape2 = normalize(int(shape2))
    
    names = {0:'Rock', 1: 'Spock', 2: 'Paper', 3: 'Lizard', 4: 'Scissors'}
    winner = winner(shape1, shape2)
    
    if winner == None:
        print 'Draw'
    else:
        print names[winner] + ' wins'
    