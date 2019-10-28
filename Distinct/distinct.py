def solution(A):
    a = len(A)
    count = 0
    A.sort()
    if a == 0:
        count = 0
    elif a > 0:
        count = 1
    for x in range(1,len(A)):
        if A[x] == A[x-1]:
            pass
        else:
            count+=1
    return count
