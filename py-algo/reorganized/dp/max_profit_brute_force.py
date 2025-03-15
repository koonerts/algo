"""
Max_profit_brute_force

"""
def max_profit_brute_force(prices: list[int]) -> int:
        max_profit = 0
        for i, price in enumerate(prices):
            for j in range(i + 1, len(prices)):
                if prices[j] - price > max_profit:
                    max_profit = prices[j] - price
        return max_profit


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to max_profit_brute_force
    print(max_profit_brute_force([]))
