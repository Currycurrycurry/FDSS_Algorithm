# 构建除自己之外所有元素乘积的数组
# O(n^2)
def constructMults(A):
    B = []
    for i in range(len(A)):
        val = 1
        for j in range(len(A)):
            if i != j:
                val *= A[j]
        B.append(val)
    return B

# normal
def constructMults(A):
    sum_value = 1
    for a in A:
        sum_value *= a
    ans = []
    for a in A:
        ans.append(sum_value//a)

# O(n)
def constructMults(A):
    mults = [A[0]]
    for i in range(1, len(A)):
        mults.append(mults[i-1] * A[i])
    mults_reversed = [A[-1]] * len(A)
    for i in range(len(A)-2, -1, -1):
        mults_reversed[i] = mults_reversed[i+1] * A[i]
    res = [mults_reversed[1]]
    for i in range(1, len(A) - 1):
        res.append(mults[i-1] * mults_reversed[i+1])
    res.append(mults[-2])
    return res

A = [1, 2, 3, 4, 5]
print(constructMults(A))





    