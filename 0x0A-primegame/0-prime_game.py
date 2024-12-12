#!/usr/bin/python3
"""Solution to the prime game problem.
    Author: Bismark -K
"""


def isWinner(x, nums):
    """Determines who the winner of a prime game of x rounds is.
    """
    if x < 1 or not nums:
        return None
    winnerIsMaria, winnerIsBen = 0, 0

    n = max(nums)
    prm = [True for _ in range(1, n + 1, 1)]
    prm[0] = False
    for i, is_prime in enumerate(prm, 1):
        if i == 1 or not is_prime:
            continue
        for j in range(i + i, n + 1, i):
            prm[j - 1] = False

    for _, n in zip(range(x), nums):
        prm_cnts = len(list(filter(lambda x: x, prm[0: n])))
        winnerIsBen += prm_cnts % 2 == 0
        winnerIsMaria += prm_cnts % 2 == 1
    if winnerIsMaria == winnerIsBen:
        return None
    return 'Maria' if winnerIsMaria > winnerIsBen else 'Ben'
