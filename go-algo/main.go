package main

import (
	"fmt"
)

func main() {
	pLn()
}

func pLn(i ...interface{}) {
	if len(i) == 1 {
		fmt.Println(i[0])
	} else {
		fmt.Println(i)
	}
}


func distinctMaxHeaps(n int) int {
	
}

func comb(n, k int) int {
	memo := map[int]map[int]int{}
	var helper func(n, k int) int
	helper = func(n, k int) int {
		if n == 0 || k == 0 {
			return 1
		}
		if memo[n] == nil {
			memo[n] = map[int]int{}
		}
		if _, ok := memo[n][k]; !ok {
			memo[n][k] = helper(n-1, k) + helper(n, k-1)
		}
		return memo[n][k]
	}
	return helper(n, k)
}