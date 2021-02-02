

def dutch_flag_partition(arr: list[int], i: int):
    start, end = 0, len(arr) - 1

    while start < end:
        if arr[start] < arr[i]:
            start
