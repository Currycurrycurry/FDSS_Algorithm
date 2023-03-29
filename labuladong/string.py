# 43. 字符串相乘
def multiply(self, num1: str, num2: str) -> str:
    num1_len = len(num1)
    num2_len = len(num2)
    res_len = num1_len + num2_len
    res = [0 for _ in range(res_len)] # 最大为a+b位
    for i in range(num1_len - 1, -1, -1):
        for j in range(num2_len - 1, -1, -1):
            val = int(num1[i]) * int(num2[j])
            target_digit_a, target_digit_b =  i + j, i + j + 1 # 乘积在 res 对应的索引位置
            tmp = val + res[target_digit_b]
            res[target_digit_b] = tmp % 10
            res[target_digit_a] += tmp // 10
    start_index = 0
    while start_index < res_len and res[start_index] == 0:
        start_index += 1

    return '0' if start_index == res_len else ''.join(list(map(str, res[start_index:])))