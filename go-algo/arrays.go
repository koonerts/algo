package main

import (
	"fmt"
	"math"
	"sort"
	"strings"
	"time"
)

func TwoNumberSum(array []int, target int) []int {
	set := map[int]struct{}{}
	for _, num := range array {
		if _, exists := set[target-num]; exists {
			return []int{target - num, num}
		} else {
			set[num] = struct{}{}
		}
	}
	return []int{}
}

func IsValidSubsequence(array []int, sequence []int) bool {
	if len(sequence) > len(array) {
		return false
	}

	seqIdx := 0
	for _, num := range array {
		if sequence[seqIdx] == num {
			seqIdx++
		}
		if seqIdx >= len(sequence) {
			return true
		}
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
	for p1, p2 := 0, 0; p1 < len(array) && p2 < len(array); {
		if array[p1] != toMove {
			p1++
		}
		if array[p2] == toMove {
			p2++
		}
		if p2 < p1 {
			p2 = p1
		}
		if p1 < len(array) && p2 < len(array) && array[p1] == toMove && array[p2] != toMove {
			array[p1], array[p2] = array[p2], array[p1]
			p1++
			p2++
		}
	}
	return array
}

func IsMonotonic(array []int) bool {
	if len(array) <= 1 {
		return true
	}

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

type Block map[string]bool

func ApartmentHunting(blocks []Block, reqs []string) int {
	dist := map[int]map[string]int{}

	var traverse func(idx int, dir int, itemToFind string) int
	traverse = func(idx int, dir int, itemToFind string) int {
		if !(0 <= idx && idx < len(blocks)) {
			return math.MaxInt32
		} else if _, ok := dist[idx][itemToFind]; ok {
			return dist[idx][itemToFind]
		} else if blocks[idx][itemToFind] == true {
			return 0
		} else {
			return traverse(idx+dir, dir, itemToFind) + 1
			/*dist[itemToFind] = traverse(idx+dir, dir, itemToFind) + 1
			return dist[itemToFind]*/
		}
	}

	for i := range blocks {
		for _, req := range reqs {
			up := traverse(i, -1, req)
			down := traverse(i, 1, req)
			if dist[i] == nil {
				dist[i] = make(map[string]int)
			}
			dist[i][req] = min(up, down)
		}
	}

	idx, minDistAll := -1, math.MaxInt32
	for i, d := range dist {
		maxDistCurr := math.MinInt32
		for _, val := range d {
			maxDistCurr = max(val, maxDistCurr)
		}
		if maxDistCurr < minDistAll {
			idx = i
			minDistAll = maxDistCurr
		}
	}
	return idx
}

// TODO: Unfinished
func SubarraySort(array []int) []int {
	lo, hi := 0, len(array)-1
	loRet, hiRet := -1, -1
	for lo < hi {
		if array[lo] <= array[lo+1] {
			lo++
		} else {

		}
		if array[hi] >= array[hi-1] {
			hi--
		}
	}
	return []int{loRet, hiRet}
}

func LongestSubstringWithoutDuplication(str string) string {
	charFreq := make(map[byte]bool)
	lo, hi := 0, 0
	maxLo, maxHi := 0, 0
	for hi < len(str) {
		for charFreq[str[hi]] {
			delete(charFreq, str[lo])
			lo++
		}
		charFreq[str[hi]] = true
		if hi-lo+1 > maxHi-maxLo+1 {
			maxLo, maxHi = lo, hi
		}
		hi++
	}
	return str[maxLo : maxHi+1]
}

func IndexEqualsValue(array []int) int {
	lo, hi := 0, len(array)-1
	idx := -1
	for lo < hi {
		mid := (lo + hi) / 2
		if array[mid] == mid {
			idx = mid
			hi = mid - 1
		} else if array[mid] > mid {
			hi = mid - 1
		} else {
			lo = mid + 1
		}
	}
	return idx
}

func WaterArea(heights []int) int {

	lIdx, rIdx := 0, len(heights)-1
	lWall, rWall := heights[lIdx], heights[rIdx]
	// areas := make([]int, len(heights))
	area := 0
	for lIdx < rIdx {
		if heights[lIdx] < heights[rIdx] {
			//areas[lIdx] = lWall - heights[lIdx]
			lIdx++
			lWall = max(lWall, heights[lIdx])
			area += lWall - heights[lIdx]
		} else {
			rIdx--
			rWall = max(rWall, heights[rIdx])
			area += rWall - heights[rIdx]
		}
	}
	return area
}

type StringMeeting struct {
	Start string
	End   string
}

type DurationMeeting struct {
	Start time.Duration
	End   time.Duration
}

func NewDurationMeeting(startStr, endStr string) DurationMeeting {
	start, _ := time.ParseDuration(strings.Replace(startStr, ":", "h", 1) + "m")
	end, _ := time.ParseDuration(strings.Replace(endStr, ":", "h", 1) + "m")
	return DurationMeeting{start, end}
}

func NewStringMeeting(startDur, endDur time.Duration) StringMeeting {
	start := fmt.Sprintf("%d", int64(startDur.Hours())) + ":" + fmt.Sprintf("%d", int((startDur - time.Duration(startDur.Hours())*time.Hour).Minutes()))
	end := fmt.Sprintf("%d", int64(endDur.Hours())) + ":" + fmt.Sprintf("%d", int64((endDur - time.Duration(endDur.Hours())*time.Hour).Minutes()))
	if strings.HasSuffix(start, ":0") { start += "0" }
	if strings.HasSuffix(end, ":0") { end += "0" }
	return StringMeeting{start, end}
}

func getDurations(calendar1 []StringMeeting, dailyBounds1 StringMeeting,
	calendar2 []StringMeeting, dailyBounds2 StringMeeting, meetingDuration int,
	) (cd1, cd2 []DurationMeeting, bound DurationMeeting, meetingDur time.Duration) {
	for i := range calendar1 {
		cd1 = append(cd1, NewDurationMeeting(calendar1[i].Start, calendar1[i].End))
	}
	for i := range calendar2 {
		cd2 = append(cd2, NewDurationMeeting(calendar2[i].Start, calendar2[i].End))
	}
	b1 := NewDurationMeeting(dailyBounds1.Start, dailyBounds1.End)
	b2 := NewDurationMeeting(dailyBounds2.Start, dailyBounds2.End)
	bound = DurationMeeting{maxDuration(b1.Start, b2.Start), minDuration(b1.End, b2.End)}
	meetingDur = time.Minute*time.Duration(meetingDuration)
	return
}

func minDuration(durs ...time.Duration) time.Duration {
	min := durs[0]
	for i := range durs {
		if durs[i] < min {
			min = durs[i]
		}
	}
	return min
}

func maxDuration(durs ...time.Duration) time.Duration {
	max := durs[0]
	for i := range durs {
		if durs[i] > max {
			max = durs[i]
		}
	}
	return max
}

func CalendarMatching(calendar1 []StringMeeting, dailyBounds1 StringMeeting,
	calendar2 []StringMeeting, dailyBounds2 StringMeeting, meetingDuration int) []StringMeeting {
	cd1, cd2, bound, meetingDur := getDurations(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration)

	blocked := make([]DurationMeeting, 0, len(cd1)+len(cd2))
	for i,j := 0,0; i < len(cd1) || j < len(cd2); {
		if j >= len(cd2) || (i < len(cd1) && cd1[i].Start <= cd2[j].Start) {
			if len(blocked) == 0 || blocked[len(blocked)-1].End < cd1[i].Start {
				blocked = append(blocked, cd1[i])
			} else {
				blocked[len(blocked)-1].End = maxDuration(blocked[len(blocked)-1].End, cd1[i].End)
			}
			i++
		} else {
			if len(blocked) == 0 || blocked[len(blocked)-1].End < cd2[j].Start {
				blocked = append(blocked, cd2[j])
			} else {
				blocked[len(blocked)-1].End = maxDuration(blocked[len(blocked)-1].End, cd2[j].End)
			}
			j++
		}
	}
	if len(blocked) == 0 {
		return []StringMeeting{NewStringMeeting(bound.Start, bound.End)}
	}

	openings := make([]DurationMeeting, 0)
	if bound.Start < blocked[0].Start && blocked[0].Start-bound.Start >= meetingDur {
		openings = append(openings, DurationMeeting{bound.Start, blocked[0].Start})
	}

	prev := blocked[0]
	for i := 1; i < len(blocked); i++ {
		start := prev.End
		end := minDuration(blocked[i].Start, bound.End)
		if end - start >= meetingDur && start >= bound.Start && end <= bound.End {
			openings = append(openings, DurationMeeting{start, end})
		}
		prev = blocked[i]
	}

	if bound.End > blocked[len(blocked)-1].End && bound.End-blocked[len(blocked)-1].End >= meetingDur{
		openings = append(openings, DurationMeeting{blocked[len(blocked)-1].End, bound.End})
	}

	openingsStringMeetings := make([]StringMeeting, 0, len(openings))
	for i := range openings {
		openingsStringMeetings = append(openingsStringMeetings, NewStringMeeting(openings[i].Start, openings[i].End))
	}
	fmt.Println(blocked)
	return openingsStringMeetings
}
