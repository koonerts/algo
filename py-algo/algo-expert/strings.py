from collections import deque

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


def balancedBrackets(string):
    bracket_map = {'}':'{', ']':'[', ')':'('}
    open_brackets = {'{','[','('}
    stk = []
    for c in string:
        if c not in bracket_map and c not in open_brackets:
            continue
        elif c not in bracket_map:
            stk.append(c)
        else:
            if not stk or stk[-1] != bracket_map[c]:
                return False
            stk.pop()
    return len(stk) == 0


def shortenPath(path):
    path_elements = path.split('/')
    stk = []

    for i in range(len(path_elements)):
        if path_elements[i] == '.':
            continue
        elif path_elements[i] == '..':
            if not stk or stk[-1] == '..':
                stk.append(path_elements[i])
            elif stk[-1] == '':
                continue
            else:
                stk.pop()
        elif path_elements[i] == '':
            if not stk:
                stk.append(path_elements[i])
        else:
            stk.append(path_elements[i])

    if len(stk) > 1:
        return '/'.join(stk)
    else:
        if stk and stk[0] == '':
            return '/'
        else:
            return stk[0]


print(shortenPath("/foo/../test/../test/../foo//bar/./baz"))