def printProb(n):
    probs = [[0] * (6 * n + 1) for i in range(2)]
    flag = 0
    for i in range(6):
        probs[flag][i] = 1
    for i in range(2, n+1):
        for j in range(i):
            probs[1-flag][i] = 0
        for j in range(i, 6 * i + 1):
            probs[1-flag][i] = 0
            for k in range(1, min(j, 6) + 1):
                probs[1-flag][j] += probs[flag][j-k]
        flag = 1 - flag

    for i in range(n, 6 * n + 1):
        print('{}\'s P is {}'.format(i, probs[flag][i]/pow(6, n)))

print(printProb(10))

        