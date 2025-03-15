"""
Test_lru_cache

"""


def test_lru_cache():
    lc = LRUCache(2)
    lc.put(1, 1)
    lc.put(2, 2)
    print(lc.get(1))
    lc.put(3, 3)
    print(lc.get(2))
    lc.put(4, 4)
    print(lc.get(1))
    print(lc.get(3))
    print(lc.get(4))


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to test_lru_cache
    print(test_lru_cache([]))
