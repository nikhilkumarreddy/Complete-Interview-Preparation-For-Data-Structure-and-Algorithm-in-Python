def pair_sum(A, target_sum):  #TC = O(N^2) SC = O(N)

    n = len(A)
    count = 0
    for i in range(0, n):
        for j in range(i+1, n):
            if A[i] + A[j] == target_sum:
                count +=1
    return count

def pair_sum_2(A, target_sum): #O(N) sc = O(N)
    n = len(A)
    set_ = set()
    count = 0
    for i in range(0, n):
        if target_sum - A[i] in set_:
            count +=1
        set_.add(A[i])
    return count


A = [1, 5, -1,3,3 , 7, 10]
print(pair_sum_2(A, 6))

