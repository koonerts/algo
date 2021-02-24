package main

import (
	"sort"
)

func letterCombinations(digits string) (results []string) {
	if digits == "" {
		return
	}
	digitMap := map[byte]string {
		'2':"abc", '3':"def", '4':"ghi", '5':"jkl",
		'6':"mno", '7':"pqrs", '8':"tuv", '9':"wxyz",
	}

	var permute func(digitIdx int, permutation []byte)
	permute = func(digitIdx int, permutation []byte) {
		if len(permutation) == len(digits) {
			results = append(results, string(permutation))
			return
		}

		for i := range digitMap[digits[digitIdx]] {
			permute(digitIdx+1, append(permutation, digitMap[digits[digitIdx]][i]))
		}
	}
	permute(0, []byte{})
	return results
}

// TODO: Come back to
func permute(nums []int) (results [][]int) {
	var permuteRecursive func(i, j int, permutation []int)
	permuteRecursive = func(i, j int, permutation []int) {
		if len(permutation) == len(nums) {
			results = append(results, permutation)
			return
		}

		sort.Ints(nums)
		if i > 0 && nums[i] == permutation[j] {
			permuteRecursive(i+1, j+1, append(permutation, nums[i]))
		} else {
			for k := 0; k <= len(permutation); k++ {
				cp := make([]int, len(permutation[:k]))
				copy(cp, permutation[:k])
				cp = append(cp, nums[i])
				cp = append(cp, permutation[k:]...)
				permuteRecursive(i+1, k, cp)
			}
		}
	}

	permuteRecursive(0, 0, []int{})
	return
}


/*func removeInvalidParentheses(s string) (results []string) {
	extraClose, extraOpen := 0, 0


	var backtrack func(i, openCnt, closedCnt int, parens string)
	backtrack = func(i, openCnt, closedCnt int, parens string) {
		if i >= len(s) && openCnt == closedCnt {
			results = append(results, parens)
			return
		}

		if s[i] == ')' && openCnt == closedCnt {
			backtrack(i+1, openCnt, closedCnt, parens)

			parens += ")"
			for j := len(parens)-3; j >= 1; j-- {
				if parens[j]
			}
		}

	}
	backtrack(0, 0, 0, []string{})
}*/
