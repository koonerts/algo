package dp

import (
	"fmt"
	"go-algo/mathext"
	"go-algo/slice"
	"math"
	"sort"
	"strconv"
)

func MinEditDistance(str1, str2 string) (minDist int) {
	dp := make([][]int, len(str1)+1)
	for i := range dp {
		dp[i] = make([]int, len(str2)+1)
	}

	for i := 1; i <= len(str1); i++ {
		for j := 1; j <= len(str2); j++ {
			deletionCost := dp[i-1][j] + 1
			insertionCost := dp[i][j-1] + 1
			editCost := dp[i-1][j-1]
			if str1[i-1] != str2[j-1] {
				editCost++
			}
			dp[i][j] = mathext.MinInt(deletionCost, insertionCost, editCost)
		}
	}
	return dp[len(str1)][len(str2)]
}

func MinEditDistanceOpt(str1, str2 string) (minDist int) {
	dp := make([][]int, 2)
	for i := range dp {
		dp[i] = make([]int, len(str2)+1)
	}

	for i := 1; i <= len(str1); i++ {
		for j := 1; j <= len(str2); j++ {
			dp[1][j] = 0
			deletionCost := dp[0][j] + 1
			insertionCost := dp[1][j-1] + 1
			editCost := dp[0][j-1]
			if str1[i-1] != str2[j-1] {
				editCost++
			}
			dp[1][j] = mathext.MinInt(deletionCost, insertionCost, editCost)
		}
		copy(dp[0], dp[1])
	}
	return dp[1][len(str2)]
}

func KnapsackZeroOne(weights []int, profits []int, capacity int) (maxProfit int) {
	rows, cols := len(weights)+1, capacity+1
	dp := make([][]int, rows)
	for i := range dp {
		dp[i] = make([]int, cols)
		if i > 0 {
			for j := range dp[i] {
				dp[i][j] = -1
			}
		}
	}

	// row-1 == itemIdx
	// col == currentCapacity
	var findProfit func(row, col int) int
	findProfit = func(row, col int) int {
		if row <= 0 || col <= 0 {
			return 0
		}

		if dp[row][col] == -1 {
			itemWeight, itemProfit := weights[row-1], profits[row-1]
			profitWith, profitWithout := 0, findProfit(row-1, col)
			if col >= itemWeight {
				profitWith = itemProfit + findProfit(row-1, col-itemWeight)
			}
			dp[row][col] = mathext.MaxInt(profitWith, profitWithout)
		}
		return dp[row][col]
	}

	maxProfit = findProfit(rows-1, cols-1)
	var itemsChosen []int
	currCap := cols - 1
	currRow := rows - 1
	for currCap > 0 && currRow > 0 {
		if dp[currRow][currCap] != dp[currRow-1][currCap] && currCap-weights[currRow-1] >= 0 {
			itemsChosen = append(itemsChosen, currRow-1)
			currCap -= weights[currRow-1]
		}
		currRow--
	}
	fmt.Println(itemsChosen)
	return maxProfit
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
			maxProfits[j] = mathext.MaxInt(profitWith, profitWithout)
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
			maxProfits[i][j] = mathext.MaxInt(profitWith, profitWithout)
		}
	}
	slice.PrintSlice(maxProfits)

	maxProfit := maxProfits[rows-1][cols-1]
	return maxProfit
}

func RodCuttingProfit(lengths []int, prices []int, maxLen int) (maxProfit int, rodLengths []int) {
	dp := make([][]int, len(lengths)+1)
	for i := range dp {
		dp[i] = make([]int, maxLen+1)
	}

	for rodIdx := 1; rodIdx < len(dp); rodIdx++ {
		for currMaxLen := 1; currMaxLen < len(dp[0]); currMaxLen++ {
			rodLen, rodProf := lengths[rodIdx-1], prices[rodIdx-1]
			profWith, profWithout := 0, dp[rodIdx-1][currMaxLen]
			if currMaxLen >= rodLen {
				profWith = rodProf + dp[rodIdx-1][currMaxLen-rodLen]
			}
			dp[rodIdx][currMaxLen] = mathext.MaxInt(profWith, profWithout)
		}
	}
	maxProfit = dp[len(dp)-1][len(dp[0])-1]
	return maxProfit, rodLengths
}

func RodCuttingProfitOpt(lengths []int, prices []int, maxLen int) (maxProfit int, rodLengths []int) {
	dp := make([][]int, 2)
	for i := range dp {
		dp[i] = make([]int, maxLen+1)
	}

	for rodIdx := 1; rodIdx < len(dp); rodIdx++ {
		for currMaxLen := 1; currMaxLen < len(dp[0]); currMaxLen++ {
			dp[0][currMaxLen] = 0
			rodLen, rodProf := lengths[rodIdx-1], prices[rodIdx-1]
			profWith, profWithout := 0, dp[0][currMaxLen]
			if currMaxLen >= rodLen {
				profWith = rodProf + dp[0][currMaxLen-rodLen]
			}
			dp[1][currMaxLen] = mathext.MaxInt(profWith, profWithout)
		}
		copy(dp[0], dp[1])
	}
	maxProfit = dp[1][maxLen]
	return maxProfit, rodLengths
}

func CoinChangeUnlimited(denoms []int, total int) int {
	if total == 0 {
		return 1
	}
	ways := make([]int, total+1)
	ways[0] = 1

	sort.Ints(denoms)
	for _, denom := range denoms {
		for currAmt := denom; currAmt <= total; currAmt++ {
			ways[currAmt] += ways[currAmt-denom]
		}
	}
	return ways[total]
}

type CakeInfo struct {
	weight, profit int
	profitPerLb    float64
}

func CakeThiefUnlimited(weightToProfits [][]int, cap int) (maxProfit int) {
	r, c := len(weightToProfits), cap
	dp := make([][]int, r+1)
	for i := range dp {
		dp[i] = make([]int, c+1)
	}

	for i := 1; i <= r; i++ {
		for j := 1; j <= c; j++ {
			itemWeight, itemProfit := weightToProfits[i-1][0], weightToProfits[i-1][1]
			profitWith, profitWithout := 0, dp[i-1][j]
			if itemWeight <= j {
				profitWith = itemProfit + dp[i][j-itemWeight]
			}
			dp[i][j] = mathext.MaxInt(profitWith, profitWithout)
		}
	}
	slice.PrintSlice(dp)
	return dp[r][c]
}

func CakeThiefUnlimitedOpt(weightToProfits [][]int, cap int) (maxProfit int) {
	dp := make([]int, cap+1)
	weight, profit := 0, 1
	for currCap := range dp {
		if currCap == 0 {
			continue
		}

		currentMaxProfit := 0
		for _, item := range weightToProfits {
			if item[weight] <= currCap {
				currentMaxProfit = mathext.MaxInt(currentMaxProfit, item[profit]+dp[currCap-item[weight]])
			}
		}
		dp[currCap] = currentMaxProfit
	}
	return dp[cap]
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

				if mathext.MinInt(without, with) != math.MaxInt32 {
					ways[j] = mathext.MinInt(without, with)
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

			cuts[j] = mathext.MaxInt(with, without)
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
					dp[idx] = mathext.MinInt(dp[idx], cnt)
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
			dp[i+j] = mathext.MinInt(dp[i+j], dp[i]+1)
		}
	}
	return dp[len(nums)-1]
}

func MaxStealProfit(profits []int) int {
	dp := make([]int, len(profits)+1)
	dp[0] = 0
	dp[1] = profits[0]

	for i := 2; i < len(dp); i++ {
		dp[i] = mathext.MaxInt(dp[i-1], profits[i-1]+dp[i-2])
	}
	slice.PrintSlice(dp)
	return dp[len(profits)]
}

func LongestPalindromicSubsequenceTabulated(text string) (maxLen int) {
	dp := make([][]int, len(text)+1)
	for i := range dp {
		dp[i] = make([]int, len(text)+1)
		if i > 0 {
			dp[i][i] = 1
		}
	}

	for i := len(text); i >= 1; i-- {
		for j := i + 1; j <= len(text); j++ {
			if text[i-1] == text[j-1] {
				dp[i][j] = 2 + dp[i+1][j-1]
			} else {
				dp[i][j] = mathext.MaxInt(dp[i+1][j], dp[i][j-1])
			}
		}
	}
	slice.PrintSlice(dp)
	return dp[1][len(text)]
}

func LongestPalindromicSubsequenceTabulatedOpt(text string) (maxLen int) {
	dp := make([][]int, 2)
	for i := range dp {
		dp[i] = make([]int, len(text)+1)
	}

	for i := len(text); i >= 1; i-- {
		for j := i + 1; j <= len(text); j++ {
			dp[1][j] = 0
			if j == i+1 {
				dp[1][j-1] += 1
			}
			if text[i-1] == text[j-1] {
				dp[1][j] = 2 + dp[0][j-1]
			} else {
				dp[1][j] = mathext.MaxInt(dp[0][j], dp[1][j-1])
			}
		}
		copy(dp[0], dp[1])
	}
	return dp[0][len(text)]
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
					dp[lo][hi] = mathext.MaxInt(find(lo+1, hi), find(lo, hi-1))
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

func LongestCommonSubstringLength(s1, s2 string) (maxLen int) {
	n1, n2 := len(s1), len(s2)
	dp := make([][]int, 2)
	for i := range dp {
		dp[i] = make([]int, n2+1)
	}

	for s1Idx := 1; s1Idx <= n1; s1Idx++ {
		for s2Idx := 1; s2Idx <= n2; s2Idx++ {
			dp[1][s2Idx] = 0
			if s1[s1Idx-1] == s2[s2Idx-1] {
				dp[1][s2Idx] = 1 + dp[0][s2Idx-1]
				maxLen = mathext.MaxInt(maxLen, dp[1][s2Idx])
			}
		}
		copy(dp[0], dp[1])
	}
	return maxLen
}

func LongestCommonSubsequenceLength(s1, s2 string) (maxLen int) {
	dp := make([][]int, 2)
	dp[0] = make([]int, len(s2)+1)

	for i := 1; i <= len(s1); i++ {
		dp[1] = make([]int, len(s2)+1)
		for j := 1; j <= len(s2); j++ {
			if s1[i-1] == s2[j-1] {
				dp[1][j] = 1 + dp[0][j-1]
			}
			dp[1][j] = mathext.MaxInt(dp[1][j], dp[0][j], dp[1][j-1])
		}
		dp[0] = dp[1]
	}
	return dp[1][len(s2)]
}

func LongestCommonSubsequenceLength2(s1, s2 string) (maxLen int) {
	dp := make([][]int, 2)
	for i := range dp {
		dp[i] = make([]int, len(s2)+1)
	}

	for i := 1; i <= len(s1); i++ {
		for j := 1; j <= len(s2); j++ {
			dp[1][j] = 0
			if s1[i-1] == s2[j-1] {
				dp[1][j] = 1 + dp[0][j-1]
			}
			dp[1][j] = mathext.MaxInt(dp[1][j], dp[0][j], dp[1][j-1])
		}
		copy(dp[0], dp[1])
	}
	return dp[1][len(s2)]
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

func DecodeWays(s string) (ways int) {
	if s[0] == '0' {return 0}
	if len(s) == 1 {return 1}

	dp := make([]int, len(s)+1)
	dp[0] = 1
	dp[1] = 1

	for i := 2; i <= len(s); i++ {
		if s[i-1] != '0' {
			dp[i] = dp[i-1]
		}
		twoDig, _ := strconv.Atoi(s[i-2:i])
		if twoDig >= 10 && twoDig <= 26 {
			dp[i] += dp[i-2]
		}
	}
	return dp[len(s)]
}

func LongestPalindrome(s string) string {
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

func WaysToPermuteUnderLimit(p1, p2, p3, p4 []int, budget int) (ways int) {
	allPrices := [][]int{p1, p2, p3, p4}
	for i := range allPrices {
		sort.Ints(allPrices[i])
	}

	var tryPermute func(idx, remainingBudget int)
	tryPermute = func(idx, remainingBudget int) {
		if remainingBudget == 0 {

		}
	}
	tryPermute(0, budget)
	return
}

func NumberOfWaysToTraverseGraph(width int, height int) (ways int) {
	dp := make([][]int, height)
	for i := range dp {
		dp[i] = make([]int, width)
		for j := range dp[i] {
			dp[i][j] = -1
		}
	}

	var traverse func(x, y int) int
	traverse = func(x, y int) int {
		if x == 0 && y == 0 {
			return 1
		} else if x < 0 || y < 0 {
			return 0
		}

		if dp[x][y] == -1 {
			dp[x][y] = 0
			dp[x][y] += traverse(x, y-1)
			dp[x][y] += traverse(x-1, y)
		}
		return dp[x][y]
	}
	traverse(height-1, width-1)
	return dp[height-1][width-1]
}

func NumberOfWaysToTraverseGraphTabulated(width, height int) (ways int) {
	dp := make([][]int, height+1)
	for i := range dp {
		dp[i] = make([]int, width+1)
	}
	dp[1][1] = 1
	for i := 1; i < height+1; i++ {
		for j := 1; j < width+1; j++ {
			if i == 1 && j == 1 {
				continue
			}
			dp[i][j] = dp[i-1][j] + dp[i][j-1]
		}
	}
	return dp[height][width]
}

func StaircaseTraversal(height int, maxSteps int) (ways int) {
	if maxSteps <= 1 {
		return maxSteps
	}
	dp := make([]int, height+1)

	var traverse func(idx int) int
	traverse = func(idx int) int {
		if idx < 0 {
			return 0
		} else if idx == 0 {
			return 1
		}

		if dp[idx] == 0 {
			for step := maxSteps; step >= 1; step-- {
				dp[idx] += traverse(idx - step)
			}
		}
		return dp[idx]
	}
	traverse(height)
	return dp[height]
}

func StaircaseTraversalTabulated(height, maxSteps int) (ways int) {
	if maxSteps <= 1 {
		return maxSteps
	}
	dp := make([]int, height+1)
	dp[0] = 1
	dp[1] = 1
	for i := 2; i <= height; i++ {
		for step := maxSteps; step >= 1; step-- {
			if i-step < 0 {
				continue
			}
			dp[i] += dp[i-step]
		}
	}
	return dp[height]
}

func MaxProfitWithKTransactions(prices []int, k int) (maxProfit int) {
	dp := make([][]int, k+1)
	for i := range dp {
		dp[i] = make([]int, len(prices))
	}

	return maxProfit
}

func WordBreak(s string, wordDict []string) bool {
	dp := make([]bool, len(s)+1)
	dp[0] = true

	for i := 1; i < len(s)+1; i++ {
		for _, word := range wordDict {
			if i-len(word) >= 0 && s[i-len(word):i] == word && dp[i-len(word)] {
				dp[i] = true
				break
			}
		}
	}
	return dp[len(s)]
}

func RobHouses(nums []int) int {
	if len(nums) <= 2 {
		return mathext.MaxInt(nums...)
	}

	curr, prev, prevX2 := 0, nums[0], 0
	for i := 1; i < len(nums); i++ {
		curr = mathext.MaxInt(prev, prevX2+nums[i])
		prevX2 = prev
		prev = curr
	}
	return curr
}

// TODO: Come back to
func MaximalSquare(matrix [][]byte) int {
	return -1
}

func CatalanNumber(n int) uint64 {
	catNums := make([]uint64, n+1)
	catNums[0] = 1

	for j := 1; j <= n; j++ {
		var num uint64
		for i := 0; i < j; i++ {
			num += catNums[i] * catNums[j-1-i]
		}
		catNums[j] = num
	}
	return catNums[n]
}

func MaxWeightedSchedule(schedule [][]int) (maxUtility int) {
	start, end, util := 0, 1, 2
	maxEndTime := 0
	for _, class := range schedule {
		maxEndTime = mathext.MaxInt(maxEndTime, class[end])
	}

	n := len(schedule)
	dp := make([][]int, n+1)
	for i := range dp {
		dp[i] = make([]int, maxEndTime+1)
	}

	for scIdx := 1; scIdx <= n; scIdx++ {
		for currTime := 1; currTime < len(dp[0]); currTime++ {
			class := schedule[scIdx-1]
			utilityWith, utilityWithout := 0, dp[scIdx-1][currTime]
			if class[end] <= currTime {
				utilityWith = class[util] + dp[scIdx-1][class[start]]
			}
			dp[scIdx][currTime] = mathext.MaxInt(utilityWith, utilityWithout)
		}
	}
	fmt.Println(dp[n])
	return dp[n][len(dp[0])-1]
}

func MaxWeightedScheduleOpt(schedule [][]int) (maxUtility int) {
	start, end, util := 0, 1, 2
	maxEndTime := 0
	for _, class := range schedule {
		maxEndTime = mathext.MaxInt(maxEndTime, class[end])
	}

	dp := make([]int, maxEndTime+1)
	n := len(schedule)
	for scIdx := 0; scIdx < n; scIdx++ {
		//for currTime := 1; currTime <= maxEndTime; currTime++ {
		for currTime := maxEndTime; currTime >= 1; currTime-- {
			class := schedule[scIdx]
			utilityWith, utilityWithout := 0, dp[currTime]
			if class[end] <= currTime {
				utilityWith = class[util] + dp[class[start]]
			}
			dp[currTime] = mathext.MaxInt(utilityWith, utilityWithout)
		}
	}
	fmt.Println(dp)
	return dp[maxEndTime]
}

func MinMatrixMultiplications(dims []int) (minCnt int) {
	dp := make([][]int, len(dims))
	for i := range dp {
		dp[i] = make([]int, len(dims))
	}

	for l := 2; l < len(dims); l++ {
		for i := 1; i < len(dims)-l+1; i++ {
			j := i + l - 1
			dp[i][j] = 1<<31 - 1
			for cut := i; cut < j; cut++ {
				cost := dp[i][cut] + dp[cut+1][j] + (dims[i-1] * dims[cut] * dims[j])
				dp[i][j] = mathext.MinInt(cost, dp[i][j])
			}
		}
	}
	slice.PrintSlice(dp)
	return
}

func MinPathSum(grid [][]int) (maxSum int) {
	sums := make([][]int, len(grid))
	for i := range sums {
		sums[i] = make([]int, len(grid[i]))
		copy(sums[i], grid[i])
	}

	for i := range sums {
		for j := range sums[i] {
			if i == 0 && j == 0 {
				continue
			}
			if i == 0 {
				sums[i][j] += sums[i][j-1]
				continue
			}
			if j == 0 {
				sums[i][j] += sums[i-1][j]
				continue
			}
			sums[i][j] += mathext.MinInt(sums[i-1][j], sums[i][j-1])
		}
	}
	n, m := len(sums), len(sums[0])
	return sums[n-1][m-1]
}

func MinPathSumOpt(grid [][]int) (maxSum int) {
	sums := make([]int, len(grid))
	for i := range grid {
		for j := range grid[i] {
			if i == 0 && j == 0 {
				sums[j] = grid[i][j]
				continue
			}
			if i == 0 {
				sums[j] += grid[i][j-1] + sums[j-1]
				continue
			}
			if j == 0 {
				sums[j] += grid[i-1][j]
				continue
			}
			sums[j] += mathext.MinInt(grid[i-1][j], grid[i][j-1])
		}
	}
	n := len(sums)
	return sums[n-1]
}

func LongestIncreasingSubsequence(nums []int) (maxLen int) {
	dp := make([]int, len(nums))
	for i := range dp {
		dp[i] = 1
	}

	for i := 1; i < len(nums); i++ {
		for j := 0; j < i; j++ {
			if nums[i] > nums[j] && dp[i] <= dp[j] {
				dp[i] = 1 + dp[j]
				maxLen = mathext.MaxInt(maxLen, dp[i])
			}
		}
	}
	return maxLen
}
