d = [
    'A',
    'B',
    'C',
    'D',
    'E',
    'F',
    'G',
    'H',
    'I',
    'J',
    'K',
    'L',
    'M',
    'N',
    'O',
    'P',
    'Q',
    'R',
    'S',
    'T',
    'U',
    'V',
    'W',
    'X',
    'Y',
    'Z',
    'a',
    'b',
    'c',
    'd',
    'e',
    'f',
    'g',
    'h',
    'i',
    'j',
    'k',
    'l',
    'm',
    'n',
    'o',
    'p',
    'q',
    'r',
    's',
    't',
    'u',
    'v',
    'w',
    'x',
    'y',
    'z',
    '0',
    '1',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
    '+',
    '/'
]
n = int(input())
nums = list(map(int, input().split(' ')))
ans = []
raw_bit = ''
for num in nums:
    s = bin(num)[2:]
    if len(s) != 8:
        s = '0' * (8 - len(s)) + s 
        raw_bit = raw_bit + s
i = 0
length = len(raw_bit)
# print(length)
while length % 6 != 0:
    raw_bit += '0'
    length += 1
# print(raw_bit)
while i < length:
	ans.append(d[int(raw_bit[i:i+6], 2)])
	i += 6
if n % 3 != 0:
	ans.append('=')
	n += 1
print(''.join(list(map(str, ans))))

	