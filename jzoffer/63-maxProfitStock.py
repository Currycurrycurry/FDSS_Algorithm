# jz
def max_profit_k_1(stocks):
    if len(stock) < 2:
        return 
    maxP = [0] * len(stocks)
    minNum = stocks[0]
    if stock[1] > stocks[0]:
        maxP[1] = (stocks[1] - stocks[0])
    else:
        minNum = stocks[0]
    for i in range(2, len(stocks)):
        if stocks[i] < minNum:
            minNum = stocks[i]
        else:
            maxP[i] = max(maxP[i-1], stocks[i] - minNum)
    return maxP[-1]

# lbld
def max_profit_k_1_general(stocks):
    x = 0
    y = -float('inf')
    for stock in stocks:
        x = max(x, y + stock)
        y = max(y, -stock)
    return x

stocks = [9, 11, 8, 5, 7, 12, 16, 14]
print(max_profit_k_1_general(stocks))
print(max_profit_k_1_general(stocks))




