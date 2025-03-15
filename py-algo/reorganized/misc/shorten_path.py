"""
Shorten Path

Write a function that takes in a non-empty string representing a valid Unix-shell path and returns a shortened version of that path.

A path is a notation that represents the location of a file or directory in a file system.
- A path can be an absolute path, starting from the root directory `/`, or a relative path, starting from the current directory `.`.
- The segments in a path are separated by the `/` character, and the path may end with a `/` character.
- `.` in a path represents the current directory, and `..` represents the parent directory.

For example, the path `/foo/../bar/./baz` should be shortened to `/bar/baz`.
"""


def shortenPath(path):
    """
    Shortens a Unix-shell path by resolving '.', '..' and removing unnecessary slashes.
    
    Args:
        path (str): A string representing a file system path
        
    Returns:
        str: A shortened version of the path
    """
    is_absolute = path[0] == '/'
    path_elements = path.split("/")
    stk = []

    for element in path_elements:
        if element == "" or element == ".":
            continue
        elif element == "..":
            if not stk or stk[-1] == "..":
                if not is_absolute:
                    stk.append(element)
            elif stk and stk[-1] != "":
                stk.pop()
        else:
            stk.append(element)

    if is_absolute:
        return "/" + "/".join(stk)
    elif not stk:
        return "."
    else:
        return "/".join(stk)


# Example usage
if __name__ == "__main__":
    # Examples of path shortening
    paths = [
        "/foo/../bar/./baz",         # should be "/bar/baz"
        "foo/../bar/./baz",          # should be "bar/baz"
        "../../foo/bar/baz",         # should be "../../foo/bar/baz"
        "/",                         # should be "/"
        "/foo/./bar/",               # should be "/foo/bar"
        "./foo/bar",                 # should be "foo/bar"
        ".",                         # should be "."
        "..",                        # should be ".."
    ]
    
    for p in paths:
        print(f"Original: {p}")
        print(f"Shortened: {shortenPath(p)}")
        print()