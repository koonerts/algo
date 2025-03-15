"""
Length Encoding

"""


def runLengthEncoding(string):
    if not string:
        return string

    chr, cnt = string[0], 1
    res = []
    for i in range(1, len(string)):
        if string[i] != string[i - 1] or cnt == 9:
            res.append(str(cnt) + chr)
            chr, cnt = string[i], 1
        else:
            cnt += 1
    res.append(str(cnt) + chr)
    return "".join(res)


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to runLengthEncoding
    print(runLengthEncoding([]))
