def hash_function(obj):
    temp1 = 0
    s = str(obj)
    mid = len(s) // 2
    for i in range(mid):
        temp1 += ord(s[i]) * ord(s[-(i + 1)])

    if len(s) % 2 != 0:
        temp1 += ord(s[mid])

    temp2 = 0
    for i in range(len(s)):
        result = 0
        multiply = i + 1
        result += ord(s[i])*multiply

        if i%2 == 0:
            temp2 += result
        else:
            temp2 -= result

    return (temp1 * temp2) % 123456791

print(hash_function('python'))