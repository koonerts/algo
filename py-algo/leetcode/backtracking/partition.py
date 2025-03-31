"""
Partition

"""
def partition(s):
        results = []
        n = len(s)
def isPalindrome(str_val):
            if len(str_val) == 0:
                return False
            lo, hi = 0, len(str_val)-1
            while lo < hi:
                if str_val[lo] != str_val[hi]:
                    return False
                lo += 1
                hi -= 1
            return True
def dfs(idx, curr_str, curr_path):
            if idx >= len(s) and curr_str == '':
                results.append(curr_path.copy())
                return
            elif idx >= len(s):
                return

            for i in range(idx+1, n+1):
                if isPalindrome(s[idx:i]):
                    curr_path.append(curr_str + s[idx:i])
                    dfs(i, '', curr_path)
                    curr_path.pop()

        dfs(0, "", [])
        return results


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to partition
    print(partition([]))
