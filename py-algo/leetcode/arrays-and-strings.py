import collections
import numpy as np
import string
from heapq import *

def print_matrix(matrix):
    print(np.array(matrix))

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0
        elif len(nums) == 1:
            return 1

        s, i = 0, 1
        while i < len(nums):
            if nums[s] == nums[i]:
                i += 1
            else:
                nums[s + 1] = nums[i]
                i += 1
                s += 1
        return s + 1

    def moveZeroes(self, nums: list[int]) -> None:
        """
        Given an array nums, write a function to move all 0's to the end of it while
        maintaining the relative order of the non-zero elements.

        Input: [0,1,0,3,12]
        Output: [1,3,12,0,0]
        """
        if len(nums) <= 1: return

        left, i = 0, 1
        while i < len(nums) and left < len(nums):
            if nums[left] == 0 and nums[i] != 0:
                nums[left], nums[i] = nums[i], nums[left]
                i += 1
                left += 1
            else:
                if nums[left] != 0:
                    left += 1
                    if i <= left:
                        i = left + 1

                elif nums[i] == 0:
                    i += 1
        print(nums)

    def sortArrayByParity(self, a: list[int]) -> list[int]:
        """
        Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.
        You may return any answer array that satisfies this condition.

        Input: [3,1,2,4]
        Output: [2,4,3,1]
        The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
        """
        i = 0
        p_even = 0
        while i < len(a):
            if a[i] % 2 == 1:
                for j in range(p_even, len(a)):
                    if a[j] % 2 == 0 and j > i:
                        v = a[j]
                        a[j] = a[i]
                        a[i] = v
                        p_even = j + 1
                        break
                    p_even += 1
            i += 1

        return a

    def sortedSquares(self, a: list[int]) -> list[int]:
        """
        Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.
        Input: [-4,-1,0,3,10]
        Output: [0,1,9,16,100]
        """

        ret = []
        l, r = 0, 0
        while r < len(a) and a[r] < 0:
            r += 1
        l = r - 1

        while len(ret) != len(a):
            if l < 0 or l >= len(a):
                ret.append(a[r] ** 2)
                r += 1
            elif r < 0 or r >= len(a):
                ret.append(a[l] ** 2)
                l -= 1
            else:
                if abs(a[l]) <= abs(a[r]):
                    ret.append(a[l] ** 2)
                    l -= 1
                else:
                    ret.append(a[r] ** 2)
                    r += 1

        return ret

    def heightChecker(self, heights: list[int]) -> int:
        """
        Students are asked to stand in non-decreasing order of heights for an annual photo.
        Return the minimum number of students that must move in order for all students to be standing in non-decreasing order of height.
        Notice that when a group of students is selected they can reorder in any possible way between themselves
        and the non selected students remain on their seats.

        Input: heights = [1,1,4,2,1,3]
        Output: 3

        Input: heights = [5,1,2,3,4]
        Output: 5
        """

        heights_sorted = sorted(heights)
        cnt = 0
        for i in range(len(heights)):
            if heights[i] != heights_sorted[i]:
                cnt += 1
        return cnt

    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        """
        Given a binary array, find the maximum number of consecutive 1s in this array if you can flip at most one 0.

        Input: [1,0,1,1,0]
        Output: 4
        Explanation: Flip the first zero will get the the maximum number of consecutive 1s.
        After flipping, the maximum number of consecutive 1s is 4.
        """
        if not nums or len(nums) == 0:
            return 0

        zero_val_indexes = []
        for i, v in enumerate(nums):
            if v == 0:
                zero_val_indexes.append(i)

        curr_max = len(nums) if len(zero_val_indexes) == 0 else 0
        print(zero_val_indexes)
        for i, v in enumerate(zero_val_indexes):
            start = 0 if i == 0 else zero_val_indexes[i - 1] + 1
            end = len(nums) if i + 1 >= len(zero_val_indexes) else zero_val_indexes[i + 1]
            length = len(range(start, end))
            print(start, end, length)
            if length > curr_max:
                curr_max = length
        return curr_max

    def thirdMax(self, nums: list[int]) -> int:
        """
        Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number.
        The time complexity must be in O(n).

        Input: [3, 2, 1]
        Output: 1
        Explanation: The third maximum is 1.

        Input: [2, 2, 3, 1]
        Output: 1
        Explanation: Note that the third maximum here means the third maximum distinct number.
                     Both numbers with value 2 are both considered as second maximum.
        """

        max_set = set()
        max_set.add(nums[0])
        curr_max = nums[0]
        for n in nums:
            if n > curr_max or len(max_set) < 3:
                max_set.add(n)

            if len(max_set) > 3:
                max_set.remove(min(max_set))

        if len(max_set) == 3:
            return min(max_set)
        else:
            return max(max_set)

    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        """
        Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
        Find all the elements of [1, n] inclusive that do not appear in this array.
        Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

        Input: [4,3,2,7,8,2,3,1]
        Output: [5,6]
        """
        for i in range(len(nums)):

            new_index = abs(nums[i]) - 1
            if nums[new_index] > 0:
                nums[new_index] *= -1

        return [i + 1 for i in range(len(nums)) if nums[i] > 0]

    def singleNumber(self, nums: list[int]) -> int:
        xor = 0
        for num in nums:
            xor ^= num
        return xor

    def rotate_with_extra_space(self, nums: list[int], k: int) -> None:
        if not nums: return nums
        k = k % len(nums)
        nums_copy = nums[-k:] + nums[:-k]
        for i in range(len(nums)):
            nums[i] = nums_copy[i]

        # def rotate_in_place(self, nums: list[int], k: int) -> None:
        #     if not nums: return nums
        #     k = k % len(nums)
        #
        #     temp, cnt, i = -1, 0, 0
        #     while cnt < len(nums):

    def containsDuplicate(self, nums: list[int]) -> bool:
        set_ = set()
        for num in nums:
            if num in set_:
                return False
            else:
                set_.add(num)
        return True

    def plusOne(self, digits: list[int]) -> list[int]:
        carry_over = 1
        for i in range(len(digits) - 1, -1, -1):
            val = digits[i] + 1 + carry_over
            carry_over = val // 10
            if carry_over > 0:
                digits[i] = 0
            else:
                digits[i] = val

        if carry_over > 0:
            digits.insert(0, 1)
        return digits

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_map = {}
        for i, num in enumerate(nums):
            if num_map.get(target - num):
                return [i, num_map.get(target - num)]
            else:
                num_map[num] = i
        return []

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []
        nums.sort()

        i = 0
        while i < len(nums):
            start, end = i + 1, len(nums) - 1

            while start < end:
                val = nums[i] + nums[start] + nums[end]
                if val == 0:
                    result.append([nums[i], nums[start], nums[end]])
                    start += 1
                    end -= 1

                    while start < end and nums[start] == nums[start - 1]:
                        start += 1
                elif val < 0:
                    start += 1
                else:
                    end -= 1

            i += 1
        return result

    def threeSumClosest(self, nums: list[int], target: int) -> int:
        if len(nums) == 3: return sum(nums)

        nums.sort()
        closest_sum = float('inf')
        for i in range(len(nums)):
            left, right = i + 1, len(nums) - 1
            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
                if curr_sum == target:
                    return curr_sum
                else:
                    if abs(curr_sum - target) < abs(closest_sum - target):
                        closest_sum = curr_sum

                    if curr_sum < target:
                        left += 1
                    else:
                        right -= 1
        return closest_sum

    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        pass

    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        pass

    def longestPalindrome(self, s: str) -> str:
        left, right = 0, 0
        isValid = True

    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) == 1:
            return

        i, left, right = 0, 0, len(nums) - 1
        while i < right:
            if nums[i] == 0:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
                i += 1
            elif nums[i] == 1:
                i += 1
            else:
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1
        print(nums)

    def maxArea(self, heights: list[int]) -> int:
        if not heights or len(heights) <= 1:
            return 0

        def compute_area(x, y):
            if not (0 <= x < len(heights)) or not (0 <= y < len(heights)):
                return 0

            height = min(heights[x], heights[y])
            width = y - x
            return height * width

        left, right, max_area = 0, len(heights) - 1, 0
        while left <= right:
            max_area = max(max_area, compute_area(left, right))
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        return max_area

    def intToRoman(self, num: int) -> str:
        digits = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C',
                  90: 'XC', 50: 'L', 40: 'XL', 10: 'X',
                  9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}

    def missingNumber(self, nums: list[int]) -> int:
        i = 0
        while i < len(nums):
            while nums[i] < len(nums) and nums[i] != i:
                val = nums[i]
                nums[i], nums[val] = nums[val], nums[i]
            i += 1

        for i in range(len(nums)):
            if nums[i] != i:
                return i
        return len(nums)

    def trap(self, heights: list[int]) -> int:
        pass

    def minWindow(self, s: str, t: str) -> str:
        char_freq = collections.Counter(t)
        char_index_map = {key: collections.deque() for key in char_freq}
        left, matched_cnt, min_substr = -1, 0, ''

        for i, c in enumerate(s):
            if c in char_freq:
                if left < 0:
                    left = i

                char_freq[c] = char_freq.get(c, 0) - 1
                if char_freq[c] == 0:
                    matched_cnt += 1
                    if matched_cnt == len(char_freq):
                        if (i - left + 1) < len(min_substr):
                            min_substr = s[left:i + 1]

    def maxProfit(self, prices: list[int]) -> int:
        if len(prices) == 1: return 0

        profit = 0
        peak, valley = 0, 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                peak = i
                if i == len(prices) - 1:
                    profit += prices[peak] - prices[valley]
            else:
                if peak > valley:
                    profit += prices[peak] - prices[valley]
                valley = i
        return profit

    def rotate(self, nums: list[int], k: int) -> None:
        if not nums or k == 0: return

        k = k % len(nums)
        idx, prev, temp = 0, nums[0], 0
        for _ in range(len(nums)):
            idx = ((idx + k) % len(nums))
            temp = nums[idx]
            nums[idx] = prev
            prev = temp

    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        if len(nums2) < len(nums1):
            return self.intersect(nums2, nums1)

        n2_freq = collections.Counter(nums2)
        result = []
        for i in range(len(nums1)):
            if nums1[i] in n2_freq:
                result.append(nums1[i])
                if n2_freq[nums1[i]] == 1:
                    del n2_freq[nums1[i]]
                else:
                    n2_freq[nums1[i]] -= 1
        return result

    def isValidSudoku(self, board: list[list[str]]) -> bool:
        pass

    def reverse(self, x: int) -> int:
        reversed_x = 0
        is_neg, x = x < 0, abs(x)

        while x != 0:
            r = x % 10
            reversed_x = reversed_x * 10 + r
            x = x // 10

        if is_neg:
            reversed_x = -reversed_x

        return 0 if not (-2 ** 31 - 1 <= reversed_x <= 2 ** 31 - 1) else reversed_x

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
                end = i + 1
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
        if val > 2 ** 31:
            return 2 ** 31
        elif val < (-2) ** 31:
            return (-2) ** 31
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

            if logs[i][id_sep_index + 1:id_sep_index + 2].isnumeric():
                digit_logs.append(logs[i])
            else:
                if not letter_logs:
                    letter_logs.append(logs[i])
                else:
                    log_data = logs[i][id_sep_index + 1:]

                    for j in range(len(letter_logs)):
                        ll_id_sep_index = str.index(letter_logs[j], ' ')
                        ll_log_data = letter_logs[j][ll_id_sep_index + 1:]

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
            return (0, rest, _id) if rest[0].isalpha() else (1,)

        return sorted(logs, key=get_key)

    def repeatedString(s, n):
        pass

    def numUniqueEmails(self, emails: list[str]) -> int:
        def clean_email(email: str):
            local, domain = email.split("@")
            ignore_idx = local.find('+')
            if ignore_idx >= 0:
                local = local[:ignore_idx].replace('.', '')
            else:
                local = local.replace('.', '')

            return local, domain

        email_set = set()
        for email in emails:
            local, domain = clean_email(email)
            email_set.add((local, domain))
        print(email_set)
        return len(email_set)

    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0

        char_idx = {}

        l, r = 0, 0
        max_len = 0
        while r < len(s):
            if s[r] in char_idx:
                l = max(l, char_idx[s[r]])
            char_idx[s[r]] = r + 1
            max_len = max(max_len, r - l + 1)
            r += 1
        return max_len

    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0": return "0"
        elif num1 == "1": return num2
        elif num2 == "1": return num1
        elif len(num2) > len(num1): return self.multiply(num2, num1)

        total_sum = 0
        outer_multiplier = 1
        for i in range(len(num2)-1, -1, -1):
            carry_over = 0
            sum_ = 0
            inner_multiplier = 1
            for j in range(len(num1)-1, -1, -1):
                prod = int(num2[i])*int(num1[j]) + carry_over
                if j != 0:
                    sum_ += (prod%10)*inner_multiplier
                    carry_over = prod//10
                else:
                    sum_ += prod*inner_multiplier

                inner_multiplier *= 10
            total_sum += sum_*outer_multiplier
            outer_multiplier *= 10
        return str(total_sum)

    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        if len(s) <= 2:
            return len(s)

        char_freq = collections.defaultdict(lambda: 0)
        l, max_substr_len = 0, 0
        for r, c in enumerate(s):
            char_freq[c] += 1
            while len(char_freq) > 2:
                if char_freq[s[l]] == 1:
                    del char_freq[s[l]]
                else:
                    char_freq[s[l]] -= 1
                l += 1
            max_substr_len = max(max_substr_len, r - l + 1)
        return max_substr_len

    def findMissingRanges(self, nums: list[int], lower: int, upper: int) -> list[str]:
        if lower == upper and lower not in nums:
            return [str(lower)]
        elif not nums:
            return [f'{lower}->{upper}']

        result = []
        for i, num in enumerate(nums):
            if i == 0:
                if lower < num:
                    if lower + 1 == num:
                        result.append(str(lower))
                    else:
                        result.append(f'{lower}->{num - 1}')
            else:
                diff = num - nums[i - 1]
                if diff == 2:
                    result.append(str(num - 1))
                elif diff > 2:
                    result.append(f'{nums[i - 1] + 1}->{num - 1}')

            if i == len(nums) - 1 and num < upper:
                if num + 1 == upper:
                    result.append(str(upper))
                else:
                    result.append(f'{num + 1}->{upper}')
        return result

    def nextClosestTime(self, time: str) -> str:
        valid_digits = [int(c) for c in time if c != ':']
        valid_digits.sort()

        new_time = ''
        for i in range(len(time) - 1, -1, -1):
            if time[i] == ':':
                new_time = ':' + new_time
                continue

            val = next((d for d in valid_digits if d > int(time[i])), valid_digits[0])
            new_time = str(val) + new_time
            if val != valid_digits[0]:
                return time[:i] + new_time

    def expressiveWords(self, s: str, words: list[str]) -> int:
        pass

    def maxDistToClosest(self, seats: list[int]) -> int:
        prev = None
        max_dist = 0

        for i in range(len(seats)):
            if seats[i] == 1:
                if prev is None:
                    max_dist = i
                else:
                    mid = (prev + i) // 2
                    max_dist = max(max_dist, mid - prev)
                prev = i
            elif i == len(seats) - 1:
                dist = len(seats) - 1 - prev
                max_dist = max(max_dist, dist)

        return max_dist

    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        stack = []
        next_number = collections.defaultdict(lambda: -1)

        for num in nums2:
            while stack and num > stack[-1]:
                next_number[stack.pop()] = num
            stack.append(num)

        return list(map(lambda x: next_number[x], nums1))

    def isMajorityElement(self, nums: list[int], target: int) -> bool:
        if not nums: return False

        def binary_search_low():
            low = -1
            start, end = 0, len(nums) - 1
            while start <= end:
                mid = (start + end) // 2
                if nums[mid] == target:
                    low = mid
                    end = mid - 1
                elif nums[mid] > target:
                    end = mid - 1
                else:
                    start = mid + 1
            return low

        def binary_search_high():
            high = -1
            start, end = 0, len(nums) - 1
            while start <= end:
                mid = (start + end) // 2
                if nums[mid] == target:
                    high = mid
                    start = mid + 1
                elif nums[mid] > target:
                    end = mid - 1
                else:
                    start = mid + 1
            return high

        lower = binary_search_low()
        if lower == -1: return False
        higher = binary_search_high()

        cnt = higher - lower + 1
        return cnt > len(nums) / 2

    def isValidSubsequence(self, array, seq):
        seq_idx = 0
        for num in array:
            if seq_idx >= len(seq): return True

            if num == seq[seq_idx]:
                seq_idx += 1
        return False

    def two_way_merge(self, arr1, arr2):
        i, j = 0, 0
        result = []
        while i < len(arr1) or j < len(arr2):
            if i >= len(arr1):
                result.append(arr2[j])
                j += 1
            elif j >= len(arr2):
                result.append(arr1[i])
                i += 1
            else:
                if arr1[i] <= arr2[j]:
                    result.append(arr1[i])
                    i += 1
                else:
                    result.append(arr2[j])
                    j += 1
        return result

    def calculate(self, s: str) -> int:
        stk = []
        opening_paren_indexes = []

        for c in s:
            if c == ")":
                val = str(eval(''.join(stk[opening_paren_indexes[-1]+1:])))
                while len(stk) > opening_paren_indexes[-1]:
                    stk.pop()
                stk.append(val)
                opening_paren_indexes.pop()
            elif c == '(':
                stk.append(c)
                opening_paren_indexes.append(len(stk)-1)
            else:
                stk.append(c)
        return eval(''.join(stk))

    def findBall(self, grid: list[list[int]]) -> list[int]:
        LEFT, RIGHT = -1, 1
        ret = [-1]*len(grid[0])

        def traverse(x, y) -> int:
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] != -1 and grid[x][y] != 1:
                return grid[x][y]
            elif x > len(grid)-1:
                return y*10
            elif grid[x][y] == LEFT and y == 0 \
                    or grid[x][y] == RIGHT and y == len(grid[0])-1 \
                    or grid[x][y] == RIGHT and grid[x][y+1] == LEFT \
                    or grid[x][y] == LEFT and grid[x][y-1] == RIGHT:
                return -1
            else:
                grid[x][y] = traverse(x+1, y + grid[x][y])
                return grid[x][y]

        for i in range(len(ret)):
            ret[i] = traverse(0, i)//10
        print_matrix(grid)
        return ret

    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0: return 0

        freq, lo = {}, 0
        max_len = 0
        for hi, v in enumerate(s):
            if len(freq) < k or v in freq:
                freq[v] = freq.get(v, 0) + 1
            else:
                while len(freq) >= k:
                    if freq[s[lo]] == 1:
                        del freq[s[lo]]
                    else:
                        freq[s[lo]] -= 1
                    lo += 1
                freq[v] = freq.get(v, 0) + 1
            max_len = max(max_len, hi-lo+1)
        return max_len

    def turnstile(self, num_worker: int, arr_time: list[int], direction: list[int]) -> list[int]:

        time_map = {i:[] for i in range(arr_time[-1]+2)}
        LOAD, UNLOAD = 0, 1
        for i, time in enumerate(arr_time):
            time_map[time].append(i)

        previously_used_action = (None, None)
        res = [-1]*num_worker
        for time, workers in time_map.items():
            if len(workers) == 1:
                res[workers[0]] = time
                previously_used_action = (time, direction[workers[0]])
            else:
                prev_time, prev_action = previously_used_action
                if prev_time is None or time-prev_time > 1:
                    previously_used_action = self.add_to_dock(res, time_map, time, workers, direction, UNLOAD)
                elif time-prev_time == 1:
                    if prev_action == UNLOAD:
                        previously_used_action = self.add_to_dock(res, time_map, time, workers, direction, UNLOAD)
                    else:
                        previously_used_action = self.add_to_dock(res, time_map, time, workers, direction, LOAD)
        return res

    def add_to_dock(self, res, time_map, time, workers, direction, action):
        if workers:
            worker_idx = 0
            for i in range(len(workers)):
                if direction[workers[i]] == action:
                    worker_idx = i
                    break
            res[workers[worker_idx]] = time
            previously_used_action = (time, direction[workers[worker_idx]])
            for i, worker in enumerate(workers):
                if i != worker_idx:
                    time_map[time+1].append(worker)
            return previously_used_action
        return None, None


def top_mentioned(k: int, keywords: list[str], reviews: list[str]) -> list[str]:
    kw_freq = collections.defaultdict(lambda: 0)
    heap = []
    for _, review in enumerate(reviews):
        words = [w for w in review.lower().translate(str.maketrans('', '', string.punctuation)).split(" ") if w in keywords]
        for _, word in enumerate(words):
            kw_freq[word] += 1

    for word, count in kw_freq.items():
        if len(heap) < k or (count > heap[0][0] or (count == heap[0][0] and word < heap[0][1])):
            if len(heap) == k:
                heappop(heap)
            heappush(heap, (count, word))

    print(kw_freq)
    return [w[1] for w in heap]




def num_pairs_divisible_by_60(times: list[int]) -> int:
    complement = collections.Counter()
    ans = 0
    for t in times:
        if (-t % 60) in complement:
            ans += complement[-t % 60]
        complement[t % 60] += 1
    return ans

[30,20,150,100,40]