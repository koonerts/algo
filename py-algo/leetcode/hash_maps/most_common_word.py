"""
Common Word

"""


def mostCommonWord(paragraph: str, banned: list[str]) -> str:
    stop_list = ["!", "?", ",", ";", ".", " "]
    word_freq = {}

    word_chars = []
    max_word = (0, "")
    for c in paragraph.lower():
        if c in stop_list and word_chars:
            word = "".join(word_chars)
            if word not in banned:
                word_freq[word] = word_freq.get(word, 0) + 1
                max_word = max(max_word, (word_freq[word], word))
            word_chars = []
        elif c == "'":
            continue
        elif c != " ":
            word_chars.append(c)
    return max_word[1] if max_word[1] else "".join(word_chars)


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to mostCommonWord
    print(mostCommonWord([]))
