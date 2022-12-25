"""
An arcade game player wants to climb to the top of the leaderboard and track their
ranking. The game uses Dense Ranking, so its leaderboard works like this:
1. The player with the highest score is ranked number 1 on the leaderboard.
2. Players who have equal scores receive the same ranking number, and the next
player(s) receive the immediately following ranking number.

EXAMPLE::
ranked = [100,90,90,80]
player = [70,80,105]
The ranked players will have rank, - 1,2,2,3, respectively.
If the player's scores are 70,80,105.
Their rankings after each game are 4th, 3rd and 1st
output = [4,3,1]


ALGO::from HackerRank Discussions
remove duplicates from ranked
set ranked index to last item
loop through player scores
    - while player score is better/same as ranked at index, decrement ranked index
    - add ranked index+2 to the answer
"""
import math


def climbingLeaderboard(ranked, player):
    """solution from HackerRank discussions.
    did not work for all the test cases"""
    player_rank = []
    position = 0
    ranked_new = sorted(list(set(ranked)), reverse=True)
    for i in player:
        head = 0
        tail = len(ranked_new) - 1
        if i >= ranked_new[0]:
            player_rank.append(1)
            continue
        if i <= ranked_new[-1]:
            player_rank.append(len(ranked_new) + 1)
            continue

        while tail - head > 1:
            mid = math.floor((tail - head) / 2) + head
            if i <= ranked_new[mid]:
                head = mid
            else:
                tail = mid
            if tail - head == 1:
                break

        if i == ranked_new[head]:
            position = head + 1
        if ranked_new[head] > i > ranked_new[tail]:
            position = head + 2
        if i <= ranked_new[tail]:
            position = head + 3
        player_rank.append(position)

    return player_rank


def climbingLeaderboard2(ranked, player):
    player_ranks = [-1] * len(player)
    if ranked[0] < player[-1]:
        player_ranks[-1] = 1
    start = 0
    end = len(player)
    if player_ranks[-1] == 1:
        end = len(player) - 1
    ranked_set = list(sorted(set(ranked), reverse=True))

    ranked_dict = {}

    for idx, x in enumerate(ranked_set):
        ranked_dict[idx + 1] = x
    print(ranked_dict)
    dict_keys = list(ranked_dict.keys())
    r_start = len(dict_keys) - 1

    for x in range(start, end):
        found = 0
        for y in range(r_start, -1, -1):
            rk = dict_keys[y]
            if player[x] < ranked_dict[rk]:
                player_ranks[x] = rk + 1
                ranked_dict[rk + 1] = player[x]
                found = 1
                r_start = y
                break
        if found == 0:
            player_ranks[x] = 1

    return player_ranks
