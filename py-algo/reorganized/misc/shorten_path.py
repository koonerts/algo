"""
Path

"""
def shortenPath(path):
    path_elements = path.split('/')
    stk = []

    for i in range(len(path_elements)):
        if path_elements[i] == '.':
            continue
        elif path_elements[i] == '..':
            if not stk or stk[-1] == '..':
                stk.append(path_elements[i])
            elif stk[-1] == '':
                continue
            else:
                stk.pop()
        elif path_elements[i] == '':
            if not stk:
                stk.append(path_elements[i])
        else:
            stk.append(path_elements[i])

    if len(stk) > 1:
        return '/'.join(stk)
    else:
        if stk and stk[0] == '':
            return '/'
        else:
            return stk[0]



# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to shortenPath
    print(shortenPath([]))
