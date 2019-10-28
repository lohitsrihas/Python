def solution(A):
    B = []
    a = len(A)
    count = 0
    B.append(A[0])
    for x in range(len(A)):
        for y in range(len(B)):
            if A[x] == B[y]:
                count+=1
        if count == 0:
            B.append(A[x])
        else: count = 0
    return len(B)