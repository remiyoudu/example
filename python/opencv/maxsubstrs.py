"计算0等于1最大子字符串个数"

strs = "110101111010010"

max_length = 0

begin = 0
l = 0

while begin < len(strs):
    for i in range(len(strs), begin, -1):
        new_strs = strs[begin:i]
        if new_strs.count("1") == new_strs.count("0"):
            l = len(new_strs)
            if l > max_length:
                max_length = l
            else:
                break
    begin += 1

print(max_length)
