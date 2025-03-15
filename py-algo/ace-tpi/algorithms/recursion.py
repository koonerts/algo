def gcd(num1, num2):
    if num1 == num2:
        return num1
    elif num1 < num2:
        return gcd(num1, num2 - num1)
    else:
        return gcd(num1 - num2, num2)
