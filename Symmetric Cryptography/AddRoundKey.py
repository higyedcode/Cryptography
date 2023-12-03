from pwn import xor
state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]


def add_round_key(s, k):
    # return xor(s,k)
    return [[els^elk for els,elk in zip(sline, kline)]for sline,kline in zip(s,k)]

result = add_round_key(state, round_key)
result_string = bytes(sum(result, []))
# print(add_round_key(state, round_key))
print(result_string)

