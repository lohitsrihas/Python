def solution(A):
    # write your code in Python 3.6
    east = []
    west = []
    count = 0
    for x in range(len(A)):
        if A[x] == 0:
            east.append(x)
        else:
            west.append(x)
    for x in range(len(east)):
        for y in range(len(west)):
            if east[x] < west[y]:
                count+=1
            else:
                pass
    return count