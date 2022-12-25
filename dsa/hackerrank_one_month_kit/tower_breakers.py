"""
Two players are playing a game of Tower Breakers! Player 1 always moves first,
and both players always play optimally.The rules of the game are as follows:
1. Initially there are n towers.
2. Each tower is of height m.
3. The players move in alternating turns.
4. In each turn, a player can choose a tower of height x and reduce its height to y,
where 1<=y<x and y evenly divides x.
5. If the current player is unable to make a move, they lose the game.
Given the values of n and m, determine which player will win. If the first player
wins, return 1. Otherwise, return 2.

EXAMPLE::
n = 2 ...and... m = 6
There are 2 towers, each 6 units tall. Player 1 has a choice of two moves:
- remove 3 pieces from a tower to leave 3 as 6 modulo 3 == 0
- remove 5 pieces to leave 1
Let Player 1 remove 3. Now the towers are 3 and 6 units tall.
Player 2 matches the move. Now the towers are both 3 units tall.
Now Player 1 has only one move.
Player 1 removes 2 pieces leaving 1. Towers are 1 and 2 units tall.
Player 2 matches again. Towers are both 1 unit tall.
Player 1 has no move and loses. Return 2.

n is 2 and m is 2 answer is P2
n is 1 and m is 4 answer is P1
n is 1 and m is 7 answer is P1
n is 3 and m is 7 answer is P1
"""


def towerBreakers(nTowers, mHeight):
    """
    :param nTowers: number of towers
    :param mHeight: height of each tower
    """
    # if height == 1, the game is immediately over. P1 has no moves; P2 wins
    if mHeight == 1:
        return 2
    else:
        # if towers is odd, P1 can take the first tower down to 1, effectively
        # making themselves P2 and the tower numbers even,
        # which means they are now in the position to mimic
        # the original P2's moves for the remaining towers
        # and win the game. The original p.1 wins
        if nTowers % 2 == 1:
            return 1
        else:
            # if towers are divisible by 2. P2 mimics P1's moves; P2 wins
            return 2
