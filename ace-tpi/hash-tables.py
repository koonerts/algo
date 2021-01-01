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


print(trace_path({
    "NewYork": "Chicago",
    "Boston": "Texas",
    "Missouri": "NewYork",
    "Texas": "Missouri"
}))
