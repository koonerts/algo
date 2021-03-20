package recursion

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

func PermuteInts(nums []int) (results [][]int) {
	if len(nums) <= 1 {return [][]int{nums}}

	var permute func(idx int) [][]int
	permute = func(idx int) [][]int {
		if idx == 0 {
			return [][]int{{nums[0]}}
		}
		permutations := permute(idx-1)
		pLen := len(permutations)
		var permutation []int
		for i := 0; i < pLen; i++ {
			permutation, permutations = permutations[0], permutations[1:]
			for j := 0; j <= len(permutation); j++ {
				newPermutation := make([]int, len(permutation))
				copy(newPermutation, permutation)
				newPermutation = append(newPermutation[:j], append([]int{nums[idx]}, newPermutation[j:]...)...)
				permutations = append(permutations, newPermutation)
			}
		}
		return permutations
	}
	return permute(len(nums)-1)
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

func StringPermutations(s string) (results []string) {
	if len(s) <= 1 {return []string{s}}

	var permute func(idx int) []string
	permute = func(idx int) []string {
		if idx == 0 {
			return []string{string(s[0])}
		}

		permutations := permute(idx-1)
		pLen := len(permutations)
		var permutation string
		for i := 0; i < pLen; i++ {
			permutation, permutations = permutations[0], permutations[1:]
			for j := 0; j <= len(permutation); j++ {
				permutations = append(permutations, permutation[0:j]+string(s[idx])+permutation[j:])
			}
		}
		return permutations
	}
	return permute(len(s)-1)
}


func Fib(n int) int {
	if n <= 1 {
		return n
	}

	return Fib(n-1) + Fib(n-2)
}