# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

# modify this function, and create other functions below as you wish
def question01(portfolios):

    N = len(portfolios)
    combinations = np.zeros(N*(N-1))

    ## Loop over all combinations
    i = 0
    for p in portfolios:
        for q in portfolios:
            if p != q:
                i+=1
                combinations[i] = p ^ q

    answer = max(combinations)
    return answer
