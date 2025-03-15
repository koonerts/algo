"""
Prime

"""
def isPrime(n, currPrimes) -> bool:
        if n == 2:
            return True
        else:
            for cp in currPrimes:
                if n % cp == 0:
                    return False
            return True


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to isPrime
    print(isPrime([]))
