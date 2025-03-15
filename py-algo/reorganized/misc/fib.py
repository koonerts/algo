"""
Fib

"""
def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    return n + fib(n-2)


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to fib
    print(fib([]))
