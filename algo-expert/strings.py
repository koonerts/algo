

def caesarCipherEncryptor(string, key):
    lst = []
    for c in string:
        ord_val = ord(c) + key
        if ord_val > ord('z'):
            ord_val = ord_val + ord('a') % ord('z')
        lst.append(chr(ord_val))
    return ''.join(lst)

print(caesarCipherEncryptor('ovmqkwtujqmfkao', 52))