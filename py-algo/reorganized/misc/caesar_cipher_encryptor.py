"""
Cipher Encryptor

"""
def caesarCipherEncryptor(string, key):
    lst = []
    key = key % 26
    for c in string:
        ord_val = ord(c) + key
        if ord_val > ord('z'):
            ord_val = (ord('a') - 1) + ord_val % ord('z')
        lst.append(chr(ord_val))
    return ''.join(lst)



# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to caesarCipherEncryptor
    print(caesarCipherEncryptor([]))
