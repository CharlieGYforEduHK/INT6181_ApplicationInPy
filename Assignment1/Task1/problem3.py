from typing import List

# do not modify this function
def sat(li: List[int]):
    return sorted(li) == list(range(999)) and all(li[i] != i for i in range(len(li)))

def sol():
    """Find a permutation of [0, 1, ..., 998] such that the ith element is *not* i, for all i=0, 1, ..., 998."""
    # TODO: your implementation here
    result=[]
    for i in range(999):
        result.append(998 - i)
    result[998//2],result[-1] = result[-1],result[998//2]
    return result  # return a list


print(sat(sol()))
