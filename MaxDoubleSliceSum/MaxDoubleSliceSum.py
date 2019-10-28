def solution(A):
    a = len(A)
    z = a-1
    x = 0
    tsum = []
    sub_A = []
    xsub_A = []
    zsub_A = []
    for i in range(x+1,a-1):
        sub_A.append(A[i])
    y = sub_A.index(min(sub_A))
    tsum.append(sum(sub_A)-sub_A[y])
    for i in range(y):
        xsub_A.append(sub_A[i])
    for i1 in range(len(sub_A)-1,y,-1):
        zsub_A.append(sub_A[i1]) #reversed z array
    tsum.append(sum(xsub_A)+sum(zsub_A))
    for i in range(len(xsub_A)):
        j = 0
        for j in range(len(zsub_A)):
            tsum.append(sum(xsub_A)+sum(zsub_A))
            if i == 0:
                del zsub_A[0]
        del xsub_A[0]
    return max(tsum)