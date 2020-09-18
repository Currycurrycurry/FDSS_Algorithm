def myPow(x, n):
    is_positive = True if n > 0 else False
    
    def cal_postive_pow(x, n):
        if n == 1:
            return x
        if n == 0:
            return 1
        result = cal_postive_pow(x, n//2)
        result *= result
        if n % 2 == 1:
            result *= x
        return result

    if is_positive:
        return cal_postive_pow(x, n)
    else:
        return 1 / cal_postive_pow(x, -n)