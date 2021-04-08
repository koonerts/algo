package mathext

import (
	"math/rand"
	"time"
)

func MaxInt(nums ...int) int {
	max := nums[0]
	for i := range nums {
		if nums[i] > max {
			max = nums[i]
		}
	}
	return max
}

func MinInt(nums ...int) int {
	min := nums[0]
	for i := range nums {
		if nums[i] < min {
			min = nums[i]
		}
	}
	return min
}

func AbsInt(n int) int {
	if n < 0 {
		return -n
	}
	return n
}

func MaxInt32(nums ...int32) int32 {
	max := nums[0]
	for i := range nums {
		if nums[i] > max {
			max = nums[i]
		}
	}
	return max
}

func MinInt32(nums ...int32) int32 {
	min := nums[0]
	for i := range nums {
		if nums[i] < min {
			min = nums[i]
		}
	}
	return min
}

func AbsInt32(n int32) int32 {
	if n < 0 {
		return -n
	}
	return n
}

func MaxInt64(nums ...int64) int64 {
	max := nums[0]
	for i := range nums {
		if nums[i] > max {
			max = nums[i]
		}
	}
	return max
}

func MinInt64(nums ...int64) int64 {
	min := nums[0]
	for i := range nums {
		if nums[i] < min {
			min = nums[i]
		}
	}
	return min
}

func AbsInt64(n int64) int64 {
	if n < 0 {
		return -n
	}
	return n
}

func Modulo(num, mod int) int {
	num %= mod
	if num < 0 {
		return num+mod
	}
	return num
}

func RandInt(lo, hi int) int {
	s1 := rand.NewSource(time.Now().UnixNano())
	r1 := rand.New(s1)
	return r1.Intn(hi - lo + 1) + lo
}
