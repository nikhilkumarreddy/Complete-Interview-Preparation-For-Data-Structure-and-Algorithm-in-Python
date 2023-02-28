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

def pair_sum_3(A, target_sum): #O(nlogn) #(1)
    A.sort()
    n = len(A)
    left = 0
    right = n-1
    count = 0
    while(left < right):
        current_sum = A[left] + A[right]
        if current_sum == target_sum:
            count +=1
            left +=1
            right -=1
        elif current_sum > target_sum:
            right -= 1
        else:
            left +=1
    return count





A = [1, 5, -1,3,3 , 7, 10]
print(pair_sum_3(A, 6))

