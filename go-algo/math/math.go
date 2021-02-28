package math

func MaxInt(nums ...int) int {
	maxInt := nums[0]
	for i := range nums {
		if nums[i] > maxInt {
			maxInt = nums[i]
		}
	}
	return maxInt
}

func MinInt(nums ...int) int {
	minInt := nums[0]
	for i := range nums {
		if nums[i] < minInt {
			minInt = nums[i]
		}
	}
	return minInt
}

func AbsInt(n int) int {
	if n < 0 {
		return -n
	}
	return n
}