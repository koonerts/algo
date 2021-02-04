package main

import (
	"fmt"
	"math"
	"sort"
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
			maxProfits[i][j] = max(profitWith, profitWithout)
		}
	}
	printSlice(maxProfits)

	maxProfit := maxProfits[rows-1][cols-1]
	fmt.Println(maxProfit)

	chosenItems := []int{}
	currProfit, currCapacity := maxProfit, capacity
	for i := rows-1; i > 0; i-- {
		if currProfit <= 0 || currCapacity <= 0 {break}
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
		for j := cols-1; j > 0; j-- {
			itemWeight, itemProfit := weights[i-1], profits[i-1]

			profitWith := 0
			if itemWeight <= j {
				profitWith = itemProfit + maxProfits[j-itemWeight]
			}

			profitWithout := maxProfits[j-1]
			maxProfits[j] = max(profitWith, profitWithout)
		}
	}
	fmt.Println(maxProfits)
}

func CanPartitionEqualSubsets(nums []int) bool {
	sum := 0
	for i := range nums {sum += nums[i]}
	if sum%2 == 1 {return false}

	rows := len(nums)+1
	cols := (sum/2) + 1
	dp := make([][]bool, rows)
	for i := range dp {
		dp[i] = make([]bool, cols)
		dp[i][0] = true
		if i == 0 {
			for j := range dp[i] {
				dp[i][j]=true
			}
		}
	}
	printSlice(dp)
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
	printSlice(dp)
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
	printSlice(dp)
	return dp[target]
}

func MinimumSubsetDiffPartition(nums []int) int {
	sum := 0
	for _, num := range nums {sum += num}
	var target int
	if sum % 2 == 1 {
		target = (sum+1)/2
	} else {
		target = sum/2
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
	printSlice(dp)

	var canPartitionNum int
	for i := len(dp)-1; i >= 0; i-- {
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
	printSlice(dp)
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
			maxProfits[i][j] = max(profitWith, profitWithout)
		}
	}
	printSlice(maxProfits)

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
			dp[i][j] = max(profitWith, profitWithout)
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
	printSlice(ways)
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
					with = ways[j-denoms[i]]+1
				}

				if min(without, with) != math.MaxInt32 {
					ways[j] = min(without, with)
				}
			}
		}
	}
	printSlice(ways)
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
			if j - lengths[i] > 0 && cuts[j - lengths[i]] != 0 {
				with = cuts[j - lengths[i]] + 1
			}

			cuts[j] = max(with, without)
		}
	}

	printSlice(cuts)
	return cuts[n]
}


func Fib(n int) int {
	if n <= 1 { return n }

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
					dp[idx] = min(dp[idx], cnt)
				}
			}
			return dp[idx]
		}
	}
	return traverse(0)
}

func MaxStealProfit(profits []int) int {
	dp := make([]int, len(profits)+1)
	dp[0] = 0
	dp[1] = profits[0]

	for i := 2; i < len(dp); i++ {
		dp[i] = max(dp[i-1], profits[i-1] + dp[i-2])
	}
	printSlice(dp)
	return dp[len(profits)]
}
