class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity

    def get(self, key: int) -> int:
        pass

    def put(self, key: int, value: int) -> None:
        pass


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
