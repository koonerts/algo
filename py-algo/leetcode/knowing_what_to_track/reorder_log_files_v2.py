"""
Log Files V2

"""


def reorderLogFilesV2(logs: list[str]) -> list[str]:
    def get_key(log):
        _id, rest = log.split(" ", maxsplit=1)
        return (0, rest, _id) if rest[0].isalpha() else (1,)

    return sorted(logs, key=get_key)


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to reorderLogFilesV2
    print(reorderLogFilesV2([]))
