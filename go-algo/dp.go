package main

import (
	"fmt"
)


func max(n1, n2 int) int {
	if n1 >= n2 {
		return n1
	}
	return n2
}

func printMatrix(iMatrix interface{}) {
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

			profitWithout := maxProfits[i-1][j-1]
			maxProfits[i][j] = max(profitWith, profitWithout)
		}
	}
	_ = PrettyPrint(maxProfits)

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
	printMatrix(dp)
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
	printMatrix(dp)
	return dp[rows-1][cols-1]
}