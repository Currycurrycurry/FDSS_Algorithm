try:
    M, n = list(map(int, input().split(' ')))
    S = list(map(int, input().split(' ')))
    if M == 0 or n == 0:
        print(0)
    else:
        S = sorted(S)
        res = 0
        i = 0
        if S[0] > M: 
            print(0)
        else:
            while M > 0 and i >= 0:
                M -= S[i]
                i += 1
                res += 1
            print(res)
except Exception:
    print(0)

