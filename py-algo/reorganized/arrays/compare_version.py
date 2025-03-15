"""
Version

"""
def compareVersion(version1: str, version2: str) -> int:
        v1_list = list(map(int, version1.split('.')))
        v2_list = list(map(int, version2.split('.')))

        for i in range(max(len(v1_list), len(v2_list))):
            v1_val, v2_val = 0, 0
            if i < len(v1_list): v1_val = v1_list[i]
            if i < len(v2_list): v2_val = v2_list[i]

            if v1_val < v2_val:
                return -1
            elif v1_val > v2_val:
                return 1
        return 0


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to compareVersion
    print(compareVersion([]))
