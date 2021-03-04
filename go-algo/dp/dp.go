package dp

import (
	"fmt"
	math2 "go-algo/mathext"
	"go-algo/slice"
	"math"
	"sort"
	"strconv"
)

func knapsackZeroOne(weights []int, profits []int, capacity int) {
	rows := len(weights) + 1
	cols := capacity + 1
	maxProfits := make([][]int, rows)
	for row := range maxProfits {
		maxProfits[row] = make([]int, cols)
	}

	for i := 1; i < rows; i++ {
		for j := 1; j < cols; j++ {
			itemWeight, itemProfit := weights[i-1], profits[i-1]

			profitWith := 0
			if itemWeight <= j {
				profitWith = itemProfit + maxProfits[i-1][j-itemWeight]
			}

			profitWithout := maxProfits[i-1][j]
			maxProfits[i][j] = math2.MaxInt(profitWith, profitWithout)
		}
	}
	slice.PrintSlice(maxProfits)

	maxProfit := maxProfits[rows-1][cols-1]
	fmt.Println(maxProfit)

	chosenItems := []int{}
	currProfit, currCapacity := maxProfit, capacity
	for i := rows - 1; i > 0; i-- {
		if currProfit <= 0 || currCapacity <= 0 {
			break
		}
		if currProfit != maxProfits[i-1][currCapacity] {
			chosenItems = append(chosenItems, i-1)
			currProfit -= profits[i-1]
			currCapacity -= weights[i-1]
		}
	}
	fmt.Println(chosenItems)
}

func KnapsackZeroOneOptimized(weights []int, profits []int, capacity int) {
	rows := len(weights) + 1
	cols := capacity + 1
	maxProfits := make([]int, cols)

	for i := 1; i < rows; i++ {
		for j := cols - 1; j > 0; j-- {
			itemWeight, itemProfit := weights[i-1], profits[i-1]

			profitWith := 0
			if itemWeight <= j {
				profitWith = itemProfit + maxProfits[j-itemWeight]
			}

			profitWithout := maxProfits[j-1]
			maxProfits[j] = math2.MaxInt(profitWith, profitWithout)
		}
	}
	fmt.Println(maxProfits)
}

func CanPartitionEqualSubsets(nums []int) bool {
	sum := 0
	for i := range nums {
		sum += nums[i]
	}
	if sum%2 == 1 {
		return false
	}

	rows := len(nums) + 1
	cols := (sum / 2) + 1
	dp := make([][]bool, rows)
	for i := range dp {
		dp[i] = make([]bool, cols)
		dp[i][0] = true
		if i == 0 {
			for j := range dp[i] {
				dp[i][j] = true
			}
		}
	}
	slice.PrintSlice(dp)
	fmt.Println()

	for i := 1; i < rows; i++ {
		for j := 1; j < cols; j++ {

			if dp[i-1][j] {
				dp[i][j] = dp[i-1][j]
			} else {
				remainder := j - nums[i-1]
				if remainder >= 0 {
					dp[i][j] = dp[i-1][remainder]
				}
			}
		}
	}
	slice.PrintSlice(dp)
	return dp[rows-1][cols-1]
}

func CanPartitionTargetSubsets(nums []int, target int) bool {
	dp := make([]bool, target+1)
	dp[0] = true

	for i := range nums {
		for j := target; j > 0; j-- {
			if !dp[j] && j-nums[i] >= 0 && dp[j-nums[i]] {
				dp[j] = true
			}
		}
	}
	slice.PrintSlice(dp)
	return dp[target]
}

func MinimumSubsetDiffPartition(nums []int) int {
	sum := 0
	for _, num := range nums {
		sum += num
	}
	var target int
	if sum%2 == 1 {
		target = (sum + 1) / 2
	} else {
		target = sum / 2
	}

	dp := make([]bool, target+1)
	dp[0] = true

	for i := range nums {
		for j := target; j > 0; j-- {
			if !dp[j] && j-nums[i] >= 0 && dp[j-nums[i]] {
				dp[j] = true
			}
		}
	}
	slice.PrintSlice(dp)

	var canPartitionNum int
	for i := len(dp) - 1; i >= 0; i-- {
		if dp[i] {
			canPartitionNum = i
			break
		}
	}

	return int(math.Abs(float64(canPartitionNum) - float64(sum-canPartitionNum)))
}

func CountSubsets(nums []int, target int) int {
	dp := make([]int, target+1)
	dp[0] = 1
	for i := 1; i < len(dp); i++ {
		if nums[0] == i {
			dp[i] = 1
		}
	}

	for i := 1; i < len(nums); i++ {
		for j := target; j >= 0; j-- {
			if j >= nums[i] {
				dp[j] += dp[j-nums[i]]
			}
		}
	}
	slice.PrintSlice(dp)
	return dp[target]
}

func KnapsackUnlimited(weights []int, profits []int, capacity int) int {
	rows := len(weights) + 1
	cols := capacity + 1
	maxProfits := make([][]int, rows)
	for row := range maxProfits {
		maxProfits[row] = make([]int, cols)
	}

	for i := 1; i < rows; i++ {
		for j := 1; j < cols; j++ {
			itemWeight, itemProfit := weights[i-1], profits[i-1]

			profitWith := 0
			if itemWeight <= j {
				profitWith = itemProfit + maxProfits[i][j-itemWeight]
			}

			profitWithout := maxProfits[i-1][j]
			maxProfits[i][j] = math2.MaxInt(profitWith, profitWithout)
		}
	}
	slice.PrintSlice(maxProfits)

	maxProfit := maxProfits[rows-1][cols-1]
	return maxProfit
}

func RodCuttingProfit(lengths []int, prices []int, maxLen int) (int, []int) {
	dp := make([][]int, len(lengths)+1)
	for i := range dp {
		dp[i] = make([]int, maxLen+1)
	}

	for i := 1; i < len(dp); i++ {
		for j := 1; j <= maxLen; j++ {
			profitWith, profitWithout := 0, 0
			if lengths[i-1] <= j {
				profitWith = prices[i-1] + dp[i][j-lengths[i-1]]
			}
			profitWithout = dp[i-1][j]
			dp[i][j] = math2.MaxInt(profitWith, profitWithout)
		}
	}

	var rods []int
	currProfit := dp[len(dp)-1][maxLen]
	currLen := maxLen
	i := maxLen

	for i > 0 && currLen > 0 && currProfit > 0 {
		if dp[i][currLen] != dp[i-1][currLen] {
			rods = append(rods, lengths[i-1])
			currProfit -= prices[i-1]
			currLen -= lengths[i-1]
		} else {
			i--
		}
	}
	return dp[len(dp)-1][maxLen], rods
}

func CoinChangeUnlimited(denoms []int, total int) int {
	ways := make([]int, total+1)
	ways[0] = 1

	for i := range denoms {
		for j := 1; j <= total; j++ {
			if j >= denoms[i] {
				ways[j] += ways[j-denoms[i]]
			}
		}
	}
	slice.PrintSlice(ways)
	return ways[total]
}

func MinCoinChainUnlimited(denoms []int, total int) int {
	ways := make([]int, total+1)
	for i := range ways {
		if i == 0 {
			ways[i] = 0
		} else {
			ways[i] = math.MaxInt32
		}
	}

	for i := range denoms {
		for j := 1; j <= total; j++ {
			if j >= denoms[i] {
				without, with := ways[j], math.MaxInt32
				if ways[j-denoms[i]] != math.MaxInt32 {
					with = ways[j-denoms[i]] + 1
				}

				if math2.MinInt(without, with) != math.MaxInt32 {
					ways[j] = math2.MinInt(without, with)
				}
			}
		}
	}
	slice.PrintSlice(ways)
	return ways[total]
}

func MaxRibbonCut(lengths []int, n int) int {
	cuts := make([]int, n+1)
	sort.Ints(lengths)
	for i := 1; i <= n; i++ {
		if i < lengths[0] {
			continue
		} else if i > lengths[0] {
			cuts[i] = 0
		} else {
			cuts[i] = 1
		}
	}

	for i := range lengths {
		for j := 1; j <= n; j++ {
			with, without := 0, cuts[j]
			if j-lengths[i] > 0 && cuts[j-lengths[i]] != 0 {
				with = cuts[j-lengths[i]] + 1
			}

			cuts[j] = math2.MaxInt(with, without)
		}
	}

	slice.PrintSlice(cuts)
	return cuts[n]
}

func Fib(n int) int {
	if n <= 1 {
		return n
	}

	dp := make([]int, n+1)
	dp[0], dp[1] = 0, 1

	for i := 2; i <= n; i++ {
		dp[i] = dp[i-1] + dp[i-2]
	}
	return dp[n]
}

func MinJumps(nums []int) int {
	dp := make([]int, len(nums))
	for i := range dp {
		dp[i] = math.MaxInt32
	}

	var traverse func(idx int) int
	traverse = func(idx int) int {
		if idx >= len(nums)-1 {
			return 0
		} else {
			if dp[idx] == math.MaxInt32 {
				for i := 1; i <= nums[idx]; i++ {
					cnt := traverse(idx+i) + 1
					dp[idx] = math2.MinInt(dp[idx], cnt)
				}
			}
			return dp[idx]
		}
	}
	return traverse(0)
}

func MinJumpsTabulated(nums []int) int {
	dp := make([]int, len(nums))
	for i := range dp {
		dp[i] = math.MaxInt32
	}
	dp[0] = 0

	for i := range dp {
		for j := 1; j <= nums[i] && j+i < len(nums); j++ {
			dp[i+j] = math2.MinInt(dp[i+j], dp[i]+1)
		}
	}
	return dp[len(nums)-1]
}

func MaxStealProfit(profits []int) int {
	dp := make([]int, len(profits)+1)
	dp[0] = 0
	dp[1] = profits[0]

	for i := 2; i < len(dp); i++ {
		dp[i] = math2.MaxInt(dp[i-1], profits[i-1]+dp[i-2])
	}
	slice.PrintSlice(dp)
	return dp[len(profits)]
}

func LongestPalindromicSubsequenceTabulated(text string) (maxLen int) {
	dp := make([][]int, len(text)+1)
	for i := range dp {
		dp[i] = make([]int, len(text)+1)
		dp[i][i] = 1
	}

	for i := len(text) - 1; i >= 0; i-- {
		for j := i + 1; j < len(text); j++ {
			if text[i] == text[j] {
				dp[i][j] = 2 + dp[i+1][j-1]
			} else {
				dp[i][j] = math2.MaxInt(dp[i+1][j], dp[i][j-1])
			}
		}
	}

	return dp[0][len(text)-1]
}

func LongestPalindromicSubsequenceRecursive(text string) int {
	dp := make([][]int, len(text))
	for i := range dp {
		dp[i] = make([]int, len(text))
		for j := range dp[i] {
			dp[i][j] = -1
		}
		dp[i][i] = 1
	}

	var find func(lo, hi int) int
	find = func(lo, hi int) int {
		if lo > hi {
			return 0
		} else {
			if dp[lo][hi] == -1 {
				if text[lo] == text[hi] {
					dp[lo][hi] = 2 + find(lo+1, hi-1)
				} else {
					dp[lo][hi] = math2.MaxInt(find(lo+1, hi), find(lo, hi-1))
				}
			}

			return dp[lo][hi]
		}
	}

	return find(0, len(text)-1)
}

func LongestPalindromicSubstring(text string) (int, string) {
	n := len(text)
	dp := make([][]bool, n)
	for i := range dp {
		dp[i] = make([]bool, n)
		dp[i][i] = true
	}

	maxSsLen := 1
	maxSs := text[:1]
	for i := n - 1; i >= 0; i-- {
		for j := i + 1; j < n; j++ {
			if text[i] == text[j] {
				ssLen := j - i + 1
				if ssLen == 2 || dp[i+1][j-1] {
					if ssLen > maxSsLen {
						maxSs = text[i : j+1]
						maxSsLen = ssLen
					}
					dp[i][j] = true
				}
			}
		}
	}
	slice.PrintSlice(dp)
	return maxSsLen, maxSs
}

func PalindromicSubstringCount(text string) int {
	n := len(text)
	dp := make([][]bool, n)

	cnt := 0
	for i := range dp {
		dp[i] = make([]bool, n)
		dp[i][i] = true
		cnt++
	}

	for i := n - 1; i >= 0; i-- {
		for j := i + 1; j < n; j++ {
			if text[i] == text[j] {
				ssLen := j - i + 1
				if ssLen == 2 || dp[i+1][j-1] {
					dp[i][j] = true
					cnt++
				}
			}
		}
	}
	slice.PrintSlice(dp)
	return cnt
}

func MinDeleteCountToMakePalindrome(text string) (length int) {
	return len(text) - LongestPalindromicSubsequenceTabulated(text)
}

func LongestCommonSubstringLength(s1, s2 string) int {
	dp := make([][]int, len(s1)+1)
	for i := range dp {
		dp[i] = make([]int, len(s2)+1)
	}

	maxLen := 0
	for i := 1; i <= len(s1); i++ {
		for j := 1; j <= len(s2); j++ {
			if s1[i-1] == s2[j-1] {
				dp[i][j] = 1 + dp[i-1][j-1]
				maxLen = math2.MaxInt(maxLen, dp[i][j])
			}
		}
	}

	slice.PrintSlice(dp)
	return maxLen
}

func LongestCommonSubsequenceLength(s1, s2 string) int {
	dp := make([][]int, len(s1)+1)
	for i := range dp {
		dp[i] = make([]int, len(s2)+1)
	}

	maxLen := 0
	for i := 1; i <= len(s1); i++ {
		for j := 1; j <= len(s2); j++ {
			if s1[i-1] == s2[j-1] {
				dp[i][j] = 1 + dp[i-1][j-1]
			} else {
				dp[i][j] = math2.MaxInt(dp[i-1][j], dp[i][j-1])
			}
			maxLen = math2.MaxInt(maxLen, dp[i][j])
		}
	}
	slice.PrintSlice(dp)
	return maxLen
}

func LongestCommonSubsequence(s1 string, s2 string) string {
	dp := make([][]string, len(s1)+1)
	for i := range dp {
		dp[i] = make([]string, len(s2)+1)
	}

	for i := 1; i <= len(s1); i++ {
		for j := 1; j <= len(s2); j++ {
			if s1[i-1] == s2[j-1] {
				dp[i][j] = dp[i-1][j-1] + string(s1[i-1])
			} else {
				if len(dp[i-1][j]) >= len(dp[i][j-1]) {
					dp[i][j] = dp[i-1][j]
				} else {
					dp[i][j] = dp[i][j-1]
				}
			}
		}
	}

	return dp[len(s1)][len(s2)]
}

func MaxSumIncreasingSubsequence(array []int) (maxSum int, nums []int) {
	if len(array) == 0 {
		return
	}

	sums := make([]int, len(array))
	indexes := make([]int, len(array))
	for i := range array {
		sums[i] = array[i]
		indexes[i] = -1
	}

	maxSum = array[0]
	maxIdx := 0
	for i := 1; i < len(array); i++ {
		for j := 0; j < i; j++ {
			if array[i] > array[j] && sums[i] < sums[j]+array[i] {
				sums[i] = sums[j] + array[i]
				indexes[i] = j
			}
		}

		if sums[i] > sums[maxIdx] {
			maxIdx = i
		}
	}

	maxSum = sums[maxIdx]
	for maxIdx != -1 {
		nums = append(nums, array[maxIdx])
		maxIdx = indexes[maxIdx]
	}
	slice.ReverseSlice(nums)

	return
}

func decodeWays(s string) (ways int) {
	if len(s) == 0 || s[0] == '0' {
		return
	}

	dp := make([]int, len(s))
	dp[0] = 1
	for i := 1; i < len(s); i++ {
		if s[i] != '0' {
			dp[i] = dp[i-1]
		}

		twoDig, _ := strconv.Atoi(s[i-1 : i+1])
		if twoDig >= 10 && twoDig <= 26 {
			if i == 1 {
				if s[i] == '0' {
					dp[i] = 1
				} else {
					dp[i] = 2
				}
			} else {
				dp[i] += dp[i-2]
			}
		}
	}
	return dp[len(s)-1]
}

func longestPalindrome(s string) string {
	if len(s) <= 1 {
		return s
	}
	dp := make([][]bool, len(s))
	for i := range dp {
		dp[i] = make([]bool, len(s))
		dp[i][i] = true
	}

	maxss, maxssLen := string(s[0]), 1
	for i := len(s) - 1; i >= 0; i-- {
		for j := i + 1; j < len(s); j++ {
			if s[i] == s[j] {
				ssLen := j - i + 1
				if ssLen == 2 || dp[i+1][j-1] {
					if ssLen > maxssLen {
						maxssLen = ssLen
						maxss = s[i : j+1]
					}
					dp[i][j] = true
				}
			}
		}
	}
	return maxss
}

/*func wordBreak(s string, wordDict []string) (canSegment bool) {
	if len(wordDict) == 0 {
		return true
	} else if len(s) == 0 {
		return false
	}

	var trySegment func(s string) bool
	trySegment = func(s string) bool {
		if s == "" {
			return true
		}
	}

	return
}*/
