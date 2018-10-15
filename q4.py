# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np


def question04(rows, numberMachines):

    ## Convert to ndarray and replace str(X) with int(0)    
    rows = np.array(rows)
    rows[rows=='X']=0

    ## Sort
    rows = np.sort(a=rows.astype(int),kind='heapsort')
    
    ## Rows with N contiguous 'X's
    new_rows = rows[rows[:,numberMachines-1]==0]

    ## Minimum row
    try:
        return np.min(new_rows[:,numberMachines:].sum(axis=1))
    except:
        return 0
