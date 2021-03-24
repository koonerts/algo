package collection

import "math/rand"

type RandomizedSet struct {
	Kvp  map[int]int
	Vals []int
}


/** Initialize your data structure here. */
func NewRandomizedSet() RandomizedSet {
	return RandomizedSet{Kvp: map[int]int{}, Vals:[]int{}}
}


/** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
func (rs *RandomizedSet) Insert(val int) bool {
	if _, ok := rs.Kvp[val]; ok {
		return false
	} else {
		rs.Vals = append(rs.Vals, val)
		rs.Kvp[val] = len(rs.Vals)-1
		return true
	}
}


/** Removes a value from the set. Returns true if the set contained the specified element. */
func (rs *RandomizedSet) Remove(val int) bool {
	if idx, ok := rs.Kvp[val]; !ok {
		return false
	} else {
		n := len(rs.Vals)
		rs.Kvp[rs.Vals[n-1]] = idx
		delete(rs.Kvp, val)
		rs.Vals[idx], rs.Vals[n-1] = rs.Vals[n-1], rs.Vals[idx]
		rs.Vals = rs.Vals[:n-1]
		return true
	}
}


/** Get a random element from the set. */
func (rs *RandomizedSet) GetRandom() int {
	i := rand.Intn(len(rs.Vals))
	return rs.Vals[i]
}


/**
 * Your RandomizedSet object will be instantiated and called as such:
 * obj := NewLRUCache();
 * param_1 := obj.Insert(val);
 * param_2 := obj.Remove(val);
 * param_3 := obj.GetRandom();
 */