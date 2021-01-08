

def caesarCipherEncryptor(string, key):
    lst = []
    key = key % 26
    for c in string:
        ord_val = ord(c) + key
        if ord_val > ord('z'):
            ord_val = (ord('a') - 1) + ord_val % ord('z')
        lst.append(chr(ord_val))
    return ''.join(lst)


def runLengthEncoding(string):
    if not string: return string

    chr, cnt = string[0], 1
    res = []
    for i in range(1, len(string)):
        if string[i] != string[i-1] or cnt == 9:
            res.append(str(cnt) + chr)
            chr, cnt = string[i], 1
        else:
            cnt += 1
    res.append(str(cnt)+chr)
    return "".join(res)


print(runLengthEncoding('AAAAAAAAAAAAABBCCCCDD'))