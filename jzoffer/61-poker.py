def isSequent(cards):
    cards = sorted(cards)
    zero_cnt = 0
    blank_cnt = 0
    for i in range(len(cards)-1):
        if cards[i] == 0:
            zero_cnt += 1
        elif cards[i+1] > cards[i]:
            blank_cnt += cards[i+1] - cards[i] - 1
    return zero_cnt >= blank_cnt

print(isSequent([1, 2, 0, 0, 5]))

                                                                                                                                                                                                                                                                                                                                                                                                              