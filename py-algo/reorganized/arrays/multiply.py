"""
Multiply

"""
def multiply(num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0": return "0"
        elif num1 == "1": return num2
        elif num2 == "1": return num1
        elif len(num2) > len(num1): return self.multiply(num2, num1)

        total_sum = 0
        outer_multiplier = 1
        for i in range(len(num2)-1, -1, -1):
            carry_over = 0
            sum_ = 0
            inner_multiplier = 1
            for j in range(len(num1)-1, -1, -1):
                prod = int(num2[i])*int(num1[j]) + carry_over
                if j != 0:
                    sum_ += (prod%10)*inner_multiplier
                    carry_over = prod//10
                else:
                    sum_ += prod*inner_multiplier

                inner_multiplier *= 10
            total_sum += sum_*outer_multiplier
            outer_multiplier *= 10
        return str(total_sum)


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to multiply
    print(multiply([]))
