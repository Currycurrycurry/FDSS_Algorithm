def checkValid(n, pre, arr, square):
    if n == len(arr):
        if (1+pre) in square:
            print(arr)
            return True
    else:
        for i in range(1, n+1):
            if i in arr:
                continue
            if (i+pre) in square and checkValid(n, i, arr+[i], square):
                return True
    return False

if __name__ == '__main__':
    n = 2
    while True:
        square = [x * x for x in range(1, n)]
        if checkValid(n, 1, [1], square):
            break
        n += 1