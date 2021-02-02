package main

import (
	"fmt"
	"math"
)


func max(nums ...int) int {
	maxInt := math.MinInt32
	for i := range nums {
		if nums[i] > maxInt {
			maxInt = nums[i]
		}
	}
	return maxInt
}

func printSlice(iMatrix interface{}) {
	switch matrix := iMatrix.(type) {
	case [][]bool:
		for _, value := range matrix {
			fmt.Println(value)
		}
	case [][]string:
		for _, value := range matrix {
			fmt.Println(value)
		}
	case [][]int:
		for _, value := range matrix {
			fmt.Println(value)
		}
	case []bool:
		fmt.Println(matrix)
	case []string:
		fmt.Println(matrix)
	case []int:
		fmt.Println(matrix)
	}

}

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