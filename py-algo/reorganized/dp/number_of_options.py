"""
Number_of_options

"""
def number_of_options(a, b, c, d, target):
    sources = [a, b, c, d]

    @lru_cache(None)
def dfs(count, i):
        if count > target: return 0

        if i == 4:
            return 1

        return sum([dfs(count + sources[i][j], i + 1) for j in range(len(sources[i]))])

    return dfs(0, 0)


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to number_of_options
    print(number_of_options([]))
