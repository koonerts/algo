

class Solution:

    def reverse(self, x: int) -> int:
        if x >= 0:
            return int(''.join(list(reversed(str(x)))))
        else:
            return int('-' + ''.join(list(reversed(str(x)[1:]))))

    def firstUniqChar(self, s: str) -> int:
        char_map = {}
        for i, c in enumerate(s):
            char_map[c] = char_map.get(c, []) + [i]

        for key, val in char_map.items():
            if len(val) == 1:
                return val[0]

        return -1

    def isPalindrome(self, s: str) -> bool:
        if s == '': return True

        start, end = 0, len(s) - 1
        while start <= end:
            while (not s[start].isalnum()) and start < end:
                start += 1
            while (not s[end].isalnum()) and start < end:
                end -= 1

            if s[start].casefold() != s[end].casefold():
                return False

            start += 1
            end -= 1
        return True

    def myAtoi(self, s: str) -> int:
        if not s: return 0

        start, end = -1, -1
        for i, c in enumerate(s):
            if c in ['+', '-'] or c.isnumeric():
                start = i
                end = i+1
                while end < len(s) and s[end].isnumeric():
                    end += 1
                break
            elif c.isspace():
                continue
            else:
                return 0

        sign = '+'

        if s[start] == '+':
            start += 1
            if s[start] == '-':
                sign = '-'
                start += 1
        elif s[start] == '-':
            sign = '-'
            start += 1
            if s[start] == '-':
                sign = '-'
                start += 1

        if not s[start:end].isnumeric():
            return 0

        val = int(s[start:end])
        if val > 2**31:
            return 2**31
        elif val < (-2)**31:
            return (-2)**31
        else:
            return val

    # def strStr(self, haystack: str, needle: str) -> int:
    #     if needle == '': return 0
    #
    #     start_hay, start_needle = 0, 0
    #     for i, c in enumerate(haystack):
    #         if start_needle == len(needle):
    #             return start_hay
    #
    #         if haystack[i] == needle[start_needle]:
    #             start_needle += 1
    #         else:
    #             start_hay += 1
    #             start_needle = 0
    #             while start_hay < len(haystack) and haystack[start_hay] != needle[start_needle]:
    #


print(Solution().strStr('a', 'a'))