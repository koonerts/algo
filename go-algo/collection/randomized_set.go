package collection

import (
	"math/rand"
	"time"
)

type RandomizedSet struct {
	set  map[int]int
	nums []int
}

/** Initialize your data structure here. */
func Constructor() RandomizedSet {
	return RandomizedSet{map[int]int{}, []int{}}
}

/** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
func (rs *RandomizedSet) Insert(val int) bool {
	if _, ok := rs.set[val]; ok {
		return false
	}
	rs.nums = append(rs.nums, val)
	rs.set[val] = len(rs.nums) - 1
	return true
}

/** Removes a value from the set. Returns true if the set contained the specified element. */
func (rs *RandomizedSet) Remove(val int) bool {
	if idx, ok := rs.set[val]; ok {
		n := len(rs.nums)
		rs.set[rs.nums[n-1]] = idx
		delete(rs.set, val)
		rs.nums[idx], rs.nums[n-1] = rs.nums[n-1], rs.nums[idx]
		rs.nums = rs.nums[:n-1]
		return true
	}
	return false
}


/** Get a random element from the set. */
func (rs *RandomizedSet) GetRandom() int {
	rand.Seed(time.Now().UnixNano())
	return rs.nums[rand.Intn(len(rs.nums))]
}
