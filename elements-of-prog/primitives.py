
def parity(x):
    result = 0
    while x:
        result ^= x & 1
