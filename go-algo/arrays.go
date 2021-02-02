package main

import (
	"math"
	"sort"
)


func TwoNumberSum(array []int, target int) []int {
	set := map[int]struct{}{}
	for _, num := range array {
		if _, exists := set[target-num]; exists {
			return []int{target-num, num}
		} else {
			set[num] = struct{}{}
		}
	}
	return []int{}
}


func IsValidSubsequence(array []int, sequence []int) bool {
	if len(sequence) > len(array) { return false }

	seqIdx := 0
	for _, num := range array {
		if sequence[seqIdx] == num {
			seqIdx++
		}
		if seqIdx >= len(sequence) { return true }
	}
	return false
}


func MinimumWaitingTime(queries []int) int {
	if len(queries) <= 1 {
		return 0
	}

	sort.Ints(queries)
	waitTime := queries[0]
	waitSum := waitTime

	for i := 1; i < len(queries); i++ {
		waitTime += queries[i]
		waitSum += waitTime
	}
	return waitSum
}


func FindThreeLargestNumbers(array []int) []int {
	mh := NewMinHeap([]int{})
	for _, num := range array {
		if mh.Length() < 3 {
			mh.Insert(num)
		} else if num > mh.Peek() {
			mh.Insert(num)
			mh.Remove()
		}
	}

	return (*mh)[:]
}


func ThreeNumberSum(array []int, target int) [][]int {
	results := [][]int{}
	sort.Ints(array)

	for i := range array {
		for j, k := i+1, len(array)-1; j < k; {
			sum := array[i] + array[j] + array[k]
			if sum == target {
				results = append(results, []int{array[i], array[j], array[k]})
				j += 1
				k -= 1
			} else if sum < target {
				j += 1
			} else {
				k -= 1
			}
		}
	}

	return results
}


func SmallestDifference(array1, array2 []int) []int {
	sort.Ints(array1)
	sort.Ints(array2)

	result := []int{math.MaxInt32, math.MaxInt32, math.MaxInt32}
	i, j := 0, 0
	for {
		if i >= len(array1) || j >= len(array2) {
			break
		}
		diff := int(math.Abs(float64(array1[i] - array2[j])))
		if diff < result[2] {
			result[0], result[1], result[2] = array1[i], array2[j], diff
		}

		if array1[i] <= array2[j] {
			i++
		} else {
			j++
		}
	}
	return result[:2]
}


func MoveElementToEnd(array []int, toMove int) []int {
	for p1,p2 := 0,0; p1 < len(array) && p2 < len(array); {
		if array[p1] != toMove { p1++ }
		if array[p2] == toMove { p2++ }
		if p2 < p1 { p2 = p1 }
		if p1 < len(array) && p2 < len(array) && array[p1] == toMove && array[p2] != toMove {
			array[p1], array[p2] = array[p2], array[p1]
			p1++
			p2++
		}
	}
	return array
}


func IsMonotonic(array []int) bool {
	if len(array) <= 1 { return true }

	idx := 0
	var isIncreasing bool
	for idx < len(array)-1 {
		if array[idx] == array[idx+1] {
			idx++
		} else {
			isIncreasing = array[idx] < array[idx+1]
			break
		}
	}

	for idx < len(array)-1 {
		if (isIncreasing && array[idx] > array[idx+1]) || (!isIncreasing && array[idx] < array[idx+1]) {
			return false
		}
		idx++
	}
	return true
}