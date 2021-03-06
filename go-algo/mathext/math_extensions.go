package mathext

import (
	"math/rand"
	"time"
)

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

func MaxInt32(nums ...int32) int32 {
	minInt := nums[0]
	for i := range nums {
		if nums[i] < minInt {
			minInt = nums[i]
		}
	}
	return minInt
}

func MinInt32(nums ...int32) int32 {
	minInt := nums[0]
	for i := range nums {
		if nums[i] < minInt {
			minInt = nums[i]
		}
	}
	return minInt
}

func AbsInt32(n int32) int32 {
	if n < 0 {
		return -n
	}
	return n
}

func MaxInt64(nums ...int64) int64 {
	minInt := nums[0]
	for i := range nums {
		if nums[i] < minInt {
			minInt = nums[i]
		}
	}
	return minInt
}

func MinInt64(nums ...int64) int64 {
	minInt := nums[0]
	for i := range nums {
		if nums[i] < minInt {
			minInt = nums[i]
		}
	}
	return minInt
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
