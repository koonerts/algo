"""
Uniq Char

"""
def firstUniqChar(s: str) -> int:
        char_map = {}
        for i, c in enumerate(s):
            char_map[c] = char_map.get(c, []) + [i]

        for key, val in char_map.items():
            if len(val) == 1:
                return val[0]

        return -1


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to firstUniqChar
    print(firstUniqChar([]))
