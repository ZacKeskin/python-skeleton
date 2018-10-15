# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

def question05(allowedAllocations, totalValue):

    # Extremely basic, quotient of the largest
    M = max(test)
    
    answer = totalValue // M

    if totalValue == M:
        return 1
    elif answer == 1:
        return 2
    else:
        return answer
