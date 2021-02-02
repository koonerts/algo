from collections import defaultdict

def is_disjoint(list1, list2):
    l1_set = set(list1)
    for num in list2:
        if num in l1_set:
            return False
    return True


def find_symmetric(my_list):
    map_ = {}
    for pair in my_list:
        if pair[0] not in map_:
            map_[pair[0]] = [pair]
        else:
            map_[pair[0]].append(pair)

    result = []
    for pair in my_list:
        if pair[1] in map_:
            if [pair[1], pair[0]] in map_[pair[1]]:
                result.append(pair)
    return result


def trace_path(my_dict: dict):  # A Map object
    result = []
    for source, dest in my_dict.items():
        if dest not in my_dict:
            result.append([source, dest])
            break

    while len(result) < len(my_dict):
        for source, dest in my_dict.items():
            if dest == result[-1][0]:
                result.append([source,dest])
                break
    result.reverse()
    return result


def find_pair(my_list):
    sum_map = {}
    for i in range(len(my_list)):
        for j in range(i+1, len(my_list)):
            sum_ = my_list[i] + my_list[j]
            if sum_ in sum_map:
                return [[my_list[i], my_list[j]], sum_map[sum_]]
            else:
                sum_map[sum_] = [my_list[i], my_list[j]]


def is_formation_possible(lst: list[str], word: str):
    word_set = set()
    for w in lst:
        start_idx = word.find(w)
        if start_idx != -1:
            end_idx = start_idx + len(w)

            if start_idx == 0 or end_idx == len(word):
                if start_idx == 0:
                    if word[end_idx:] in word_set:
                        return True
                else:
                    if word[:start_idx] in word_set:
                        return True
                word_set.add(w)
    return False


def findSum(lst, k):
    num_set = set()
    for num in lst:
        if k - num in num_set:
            return [num, k-num]
        else:
            num_set.add(num)


def findFirstUnique(lst):
    freq_map = defaultdict(lambda:0)
    for num in lst:
        freq_map[num] += 1
    return next((key for key in freq_map if freq_map[key] == 1))


print(findFirstUnique([4, 5, 1, 2, 0, 4]))