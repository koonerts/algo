from collections import Counter
import re

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

    def strStr(self, haystack: str, needle: str) -> int:
        pass

    def minWindow(self, s: str, t: str) -> str:
        left, right = 0, 0
        char_freq = {}

        ret_str = ''
        while right < len(s):
            if s[right] in t:
                char_freq[s[right]] = char_freq.get(s[right], 0) + 1

    def compareVersion(self, version1: str, version2: str) -> int:
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

    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        stop_list = ["!", "?", ",", ";", ".", ' ']
        word_freq = {}

        word_chars = []
        max_word = (0, '')
        for c in paragraph.lower():
            if c in stop_list and word_chars:
                word = ''.join(word_chars)
                if word not in banned:
                    word_freq[word] = word_freq.get(word, 0) + 1
                    max_word = max(max_word, (word_freq[word], word))
                word_chars = []
            elif c == "'":
                continue
            elif c != ' ':
                word_chars.append(c)
        return max_word[1] if max_word[1] else ''.join(word_chars)

    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        digit_logs = []
        letter_logs = []

        i = 0
        while i < len(logs):
            id_sep_index = str.index(logs[i], ' ')

            if logs[i][id_sep_index+1:id_sep_index+2].isnumeric():
                digit_logs.append(logs[i])
            else:
                if not letter_logs:
                    letter_logs.append(logs[i])
                else:
                    log_data = logs[i][id_sep_index+1:]

                    for j in range(len(letter_logs)):
                        ll_id_sep_index = str.index(letter_logs[j], ' ')
                        ll_log_data = letter_logs[j][ll_id_sep_index+1:]

                        if log_data < ll_log_data:
                            letter_logs.insert(j, logs[i])
                            break
                        elif log_data == ll_log_data:
                            log_id = logs[i][:id_sep_index]
                            ll_log_id = letter_logs[j][:ll_id_sep_index]

                            if log_id < ll_log_id:
                                letter_logs.insert(j, logs[i])
                                break
                        elif j == len(letter_logs) - 1:
                            letter_logs.append(logs[i])
                            break
            i += 1
        return letter_logs + digit_logs

    def reorderLogFilesV2(self, logs: list[str]) -> list[str]:
        def get_key(log):
            _id, rest = log.split(" ", maxsplit=1)
            return (0, rest, _id) if rest[0].isalpha() else (1, )

        return sorted(logs, key=get_key)




print(Solution().reorderLogFiles(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]))