package recursion

import "go-algo/mathext"

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
		if digitIdx == len(digits) {
			results = append(results, string(permutation))
			return
		}

		for i := range digitMap[digits[digitIdx]] {
			permutation[digitIdx] = digitMap[digits[digitIdx]][i]
			permute(digitIdx+1, permutation)
		}
	}
	permute(0, make([]byte, len(digits)))
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

func MaxConcatLengthWithUniqueChars(arr []string) (maxLen int) {
	var dfs func(idx int, currStr string)
	dfs = func(idx int, currStr string) {
		uniqCnt := getUniqueCharacterCount(currStr)
		maxLen = mathext.MaxInt(maxLen, uniqCnt)
		if idx >= len(arr) {
			return
		}
		dfs(idx+1, currStr+arr[idx])
		dfs(idx+1, currStr)
	}
	dfs(0, "")
	return maxLen
}

func getUniqueCharacterCount(str string) int {
	chars := make([]byte, 26)
	cnt := 0
	for i := range str {
		if chars[str[i]-'a'] != 0 {return -1}
		chars[str[i]-'a'] += 1
		cnt += 1
	}
	return cnt
}

func ShortestPalindrome(str string) string {
	n := len(str)
	i := 0
	for j := n - 1; j >= 0; j-- {
		if str[i] == str[j] {
			i++
		}
	}
	if i == n {
		return str
	}
	rev := []byte(str[i:])
	for j, k := 0, len(rev)-1; j < k; j, k = j+1, k-1 {
		rev[j], rev[k] = rev[k], rev[j]
	}
	return string(rev) + ShortestPalindrome(str[:i]) + str[i:]
}
