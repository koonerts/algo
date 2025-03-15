"""
Order

"""


from collections import deque
def alienOrder(words: list[str]) -> str:
        in_deg = {c:0 for word in words for c in word}
        adj_graph = {c:[] for word in words for c in word}
        for i in range(len(words)):
            for l in range(i+1, len(words)):
                word = words[i]
                next_word = words[l]
                if word == next_word:
                    continue
                j, k = 0, 0
                while j < len(word) and k < len(next_word):
                    if word[j] == next_word[k]:
                        j += 1
                        k += 1
                        if k >= len(next_word):
                            return ""
                    elif next_word[k] not in adj_graph[word[j]]:
                        adj_graph[word[j]].append(next_word[k])
                        in_deg[next_word[k]] += 1
                        break
                    else:
                        break

        que = deque([])
        for char, in_degree in in_deg.items():
            if in_degree == 0:
                que.append(char)

        result = ""
        while que:
            char = que.popleft()
            result += char
            for child in adj_graph[char]:
                in_deg[child] -= 1
                if in_deg[child] == 0:
                    que.append(child)

        if len(result) != len(in_deg):
            return ""
        return result


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to alienOrder
    print(alienOrder([]))
