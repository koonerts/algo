package main


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

func permute(nums []int) (results [][]int) {
	var permuteRecursive func(i int, permutation []int)
	permuteRecursive = func(i int, permutation []int) {
		if len(permutation) == len(nums) {
			results = append(results, permutation)
			return
		}

		if i > 0 && nums[i] == nums[i-1] {
			permuteRecursive(i+1, append(permutation, nums[i]))
		} else {
			for j := 0; j <= len(permutation); j++ {
				cp := make([]int, len(permutation[:j]))
				copy(cp, permutation[:j])
				cp = append(cp, nums[i])
				cp = append(cp, permutation[j:]...)
				permuteRecursive(i+1, cp)
			}
		}
	}

	permuteRecursive(0, []int{})
	return
}
