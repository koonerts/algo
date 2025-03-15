"""
Top_mentioned

"""


import collections
from collections import defaultdict
import string
def top_mentioned(k: int, keywords: list[str], reviews: list[str]) -> list[str]:
    kw_freq = collections.defaultdict(lambda: 0)
    heap = []
    for _, review in enumerate(reviews):
        words = [w for w in review.lower().translate(str.maketrans('', '', string.punctuation)).split(" ") if w in keywords]
        for _, word in enumerate(words):
            kw_freq[word] += 1

    for word, count in kw_freq.items():
        if len(heap) < k or (count > heap[0][0] or (count == heap[0][0] and word < heap[0][1])):
            if len(heap) == k:
                heappop(heap)
            heappush(heap, (count, word))

    print(kw_freq)
    return [w[1] for w in heap]





# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to top_mentioned
    print(top_mentioned([]))
