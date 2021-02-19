package main

import (
	"fmt"
	"math"
	"sort"
	"strconv"
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
	start := fmt.Sprintf("%d", int64(startDur.Hours())) + ":" + fmt.Sprintf("%d", int((startDur-time.Duration(startDur.Hours())*time.Hour).Minutes()))
	end := fmt.Sprintf("%d", int64(endDur.Hours())) + ":" + fmt.Sprintf("%d", int64((endDur-time.Duration(endDur.Hours())*time.Hour).Minutes()))
	if strings.HasSuffix(start, ":0") {
		start += "0"
	}
	if strings.HasSuffix(end, ":0") {
		end += "0"
	}
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
	meetingDur = time.Minute * time.Duration(meetingDuration)
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
	for i, j := 0, 0; i < len(cd1) || j < len(cd2); {
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
		if end-start >= meetingDur && start >= bound.Start && end <= bound.End {
			openings = append(openings, DurationMeeting{start, end})
		}
		prev = blocked[i]
	}

	if bound.End > blocked[len(blocked)-1].End && bound.End-blocked[len(blocked)-1].End >= meetingDur {
		openings = append(openings, DurationMeeting{blocked[len(blocked)-1].End, bound.End})
	}

	openingsStringMeetings := make([]StringMeeting, 0, len(openings))
	for i := range openings {
		openingsStringMeetings = append(openingsStringMeetings, NewStringMeeting(openings[i].Start, openings[i].End))
	}
	fmt.Println(blocked)
	return openingsStringMeetings
}

type Direction int

const (
	Left Direction = iota + 1
	Right
	Down
)

func WaterfallStreams(array [][]float64, source int) []float64 {
	flow(array, 0, source, 100, Down)
	return array[len(array)-1]
}

func getFlowDirections(array [][]float64, x, y int, flowDir Direction) (validFlows []Direction) {
	if x < 0 || x >= len(array) || y < 0 || y >= len(array[0]) {
		return
	}

	blockedLeft := y == 0 || array[x][y-1] == 1
	blockedRight := y == len(array[0])-1 || array[x][y+1] == 1
	blockedDown := array[x+1][y] == 1
	switch flowDir {
	case Left:
		if !blockedDown {
			validFlows = append(validFlows, Down)
		} else if !blockedLeft {
			validFlows = append(validFlows, Left)
		}
	case Right:
		if !blockedDown {
			validFlows = append(validFlows, Down)
		} else if !blockedRight {
			validFlows = append(validFlows, Right)
		}
	case Down:
		if !blockedDown {
			validFlows = append(validFlows, Down)
		} else {
			if !blockedLeft {
				validFlows = append(validFlows, Left)
			}
			if !blockedRight {
				validFlows = append(validFlows, Right)
			}
		}
	}
	return
}

func flow(array [][]float64, x, y int, amount float64, flowDir Direction) {
	if x == len(array)-1 {
		array[x][y] += amount
	} else {
		validFlows := getFlowDirections(array, x, y, flowDir)
		if len(validFlows) > 0 {
			for _, dir := range validFlows {
				xidx, yidx, amt := x, y, amount
				switch dir {
				case Left:
					if flowDir == Down {
						amt /= 2
					}
					yidx--
				case Right:
					if flowDir == Down {
						amt /= 2
					}
					yidx++
				case Down:
					xidx++
				}
				flow(array, xidx, yidx, amt, dir)
			}
		}
	}
}

func MaxSumSubArraySizeK(nums []int, k int) (maxSum int) {
	lo, hi := 0, 0
	currSum := 0
	for hi < len(nums) {
		if hi-lo+1 > k {
			currSum -= nums[lo]
			lo++
		}
		currSum += nums[hi]
		maxSum = max(maxSum, currSum)
		hi++
	}

	return
}

func LongestSubstringLengthWithKDistinct(text string, k int) (maxLen int) {
	charFreq := map[uint8]int{}

	lo, hi := 0, 0
	for hi < len(text) {
		if _, ok := charFreq[text[hi]]; !ok && len(charFreq) == k {
			for len(charFreq) == k {
				if charFreq[text[lo]] == 1 {
					delete(charFreq, text[lo])
				} else {
					charFreq[text[lo]]--
				}
				lo++
			}
		}

		charFreq[text[hi]]++
		maxLen = max(hi-lo+1, maxLen)
		hi++
	}
	return
}

func ContainsPermutation(text, pattern string) (contains bool) {
	charFreq := map[uint8]int{}
	totalCnt := len(pattern)
	for i := range pattern {
		charFreq[pattern[i]]++
	}

	lo, hi := 0, 0
	for hi < len(text) {
		if cnt, ok := charFreq[text[hi]]; ok {
			if cnt == 0 {
				for charFreq[text[hi]] == 0 {
					charFreq[text[lo]]++
					totalCnt++
					lo++
				}
			} else {
				charFreq[text[hi]]++
				totalCnt--
			}
			if totalCnt == 0 {
				return true
			}
		} else {
			for lo <= hi {
				if _, ok := charFreq[text[lo]]; ok {
					charFreq[text[lo]]++
					totalCnt++
				}
				lo++
			}
		}
		hi++
	}
	return
}

func FindAnagramStartingIndices(text, pattern string) (indices []int) {
	if len(text) == 0 || len(pattern) == 0 {
		return
	}

	cf := map[uint8]int{}
	totalCnt := len(pattern)
	for i := range pattern {
		cf[pattern[i]]++
	}

	lo, hi := 0, 0
	for hi < len(text) {
		if cnt, ok := cf[text[hi]]; ok {
			if cnt == 0 {
				for cf[text[hi]] == 0 && lo < hi {
					cf[text[lo]]++
					lo++
					totalCnt++
				}
				cf[text[hi]]--
				totalCnt--
			} else {
				cf[text[hi]]--
				totalCnt--
			}

			if totalCnt == 0 {
				indices = append(indices, lo)
				cf[text[lo]]++
				cf[text[hi]]++
				lo++
				totalCnt++
			}
		} else {
			for lo <= hi {
				if _, ok := cf[text[lo]]; ok {
					cf[text[lo]]++
					totalCnt++
				}
			}
		}

		hi++
	}

	return
}

/*func SmallestSubstringContainingPattern(str, pattern string) (ss string) {
	if len(str) == 0 || len(pattern) == 0 {
		return
	}

	pLen := len(pattern)
	cf := map[uint8]int{}
	for i := range pattern {
		cf[pattern[i]]++
	}

	lo, hi := 0, 0
	for hi < len(str) {
		if cnt, ok := cf[str[hi]]; ok {
			if cnt == 0 && str[lo] == str[hi] {
				lo++
			} else {
				cf[str[hi]]--
				pLen--
			}
		}
	}
}*/

func TournamentWinner(competitions [][]string, results []int) (winner string) {
	wins := map[string]int{}

	maxWins := 0
	for i := range results {
		w := 0
		if results[i] == 0 {
			w = 1
		}
		wins[competitions[i][w]]++
		if wins[competitions[i][w]] > maxWins {
			maxWins = wins[competitions[i][w]]
			winner = competitions[i][w]
		}
	}

	return
}

func NonConstructibleChange(coins []int) (change int) {
	sort.Ints(coins)
	return
}

func lengthOfLongestSubstringWithoutDups(s string) (maxLen int) {
	lo, hi := 0, 0
	charSet := map[uint8]int{}
	for hi < len(s) {
		if _, ok := charSet[s[hi]]; ok {
			lo = max(lo, charSet[s[hi]]+1)
		}
		maxLen = max(maxLen, hi-lo+1)
		charSet[s[hi]] = hi
		hi++
	}
	return
}

func myAtoi(s string) (val int) {
	if len(s) == 0 {
		return
	}

	idx := 0
	for idx < len(s) && s[idx] == ' ' {
		idx++
	}
	if idx == len(s) {
		return
	}

	var isNegative bool
	if s[idx] == '-' || s[idx] == '+' {
		if s[idx] == '-' {
			isNegative = true
		}
		idx++
	}
	if idx == len(s) || !IsNumeric(string(s[idx])) {
		return
	}
	numStart, numEnd := idx, idx
	for numEnd < len(s) && IsNumeric(string(s[numEnd])) {
		numEnd++
	}
	num, _ := strconv.ParseInt(s[numStart:numEnd], 10, 64)
	if isNegative {
		num = -num
	}

	if num > math.MaxInt32 {
		val = math.MaxInt32
	} else if num < math.MinInt32 {
		val = math.MinInt32
	} else {
		val = int(num)
	}

	return
}

func romanToInt(s string) (val int) {
	rn := map[string]int{"I": 1, "IV": 4, "V": 5, "IX": 9, "X": 10, "XL": 40, "L": 50, "XC": 90, "C": 100, "CD": 400, "D": 500, "CM": 900, "M": 1000}

	i := 0
	for i < len(s) {
		if i+1 < len(s) && rn[s[i:i+2]] != 0 {
			val += rn[s[i:i+2]]
			i += 2
		} else {
			val += rn[s[i:i+1]]
			i++
		}
	}
	return
}

func threeSum(nums []int) (sums [][]int) {
	sort.Ints(nums)

	for i := 0; i < len(nums)-2; {
		j, k := i+1, len(nums)-1
		for j < k {
			iv, jv, kv := nums[i], nums[j], nums[k]
			sum := iv + jv + kv
			if sum == 0 {
				sums = append(sums, []int{iv, jv, kv})
				j++
				k--

				for j < k && nums[j-1] == nums[j] {
					j++
				}
				for j < k && nums[k] == nums[k+1] {
					k--
				}
			} else if sum > 0 {
				k--
			} else {
				j++
			}
		}
		i++
		for i < len(nums)-2 && nums[i-1] == nums[i] {
			i++
		}
	}

	return
}

func removeDuplicates(nums []int) int {
	if len(nums) == 2 && nums[0] == nums[1] {
		return 1
	}

	i := 0
	for j := 1; j < len(nums); j++ {
		if nums[i] != nums[j] {
			i++
			nums[i] = nums[j]
		}
	}
	fmt.Println(nums)
	return i + 1
}

func nextPermutation(nums []int) {
	firstDecreasingIdx := -1
	for i := len(nums) - 2; i >= 0; i-- {
		if nums[i] < nums[i+1] {
			firstDecreasingIdx = i
			break
		}
	}

	if firstDecreasingIdx == -1 {
		sort.Ints(nums)
		return
	}

	for i := firstDecreasingIdx + 1; i < len(nums); i++ {
		if nums[i] > nums[firstDecreasingIdx] && (i == len(nums)-1 || nums[i+1] <= nums[firstDecreasingIdx]) {
			nums[i], nums[firstDecreasingIdx] = nums[firstDecreasingIdx], nums[i]
			break
		}
	}

	for i, j := firstDecreasingIdx+1, len(nums)-1; i < j; i, j = i+1, j-1 {
		nums[i], nums[j] = nums[j], nums[i]
	}
	return
}

func multiplyStrings(num1 string, num2 string) string {
	if num1 == "0" || num2 == "0" {
		return "0"
	}
	l1, l2 := len(num1), len(num2)
	res := make([]byte, l1+l2)
	for i := l1 - 1; i >= 0; i-- {
		for j := l2 - 1; j >= 0; j-- {
			val := (num1[i] - '0') * (num2[j] - '0')
			res[i+j+1] += val
			if res[i+j+1] >= 10 {
				res[i+j] += res[i+j+1] / 10
				res[i+j+1] %= 10
			}
		}
	}
	if res[0] == 0 {
		res = res[1:]
	}
	for i := range res {
		res[i] += '0'
	}
	return string(res)
}


func addStrings(num1, num2 string) string {
	i, j := len(num1)-1, len(num2)-1
	carryover := 0
	returnVal := ""
	for i >= 0 || j >= 0 {
		ival, jval := 0, 0
		if i >= 0 {
			ival, _ = strconv.Atoi(string(num1[i]))
		}
		if j >= 0 {
			jval, _ = strconv.Atoi(string(num2[j]))
		}
		sum := ival+jval+carryover
		if i > 0 || j > 0 {
			returnVal = strconv.FormatInt(int64(sum%10), 10) + returnVal
			carryover = sum/10
		} else {
			returnVal = strconv.FormatInt(int64(sum), 10) + returnVal
		}

		i--
		j--
	}
	return returnVal
}


func groupAnagrams(strs []string) (groups [][]string) {
	groupsDict := map[string][]string{}
	for _, str := range strs {
		chars := make([]byte, 26)
		for i := range str {
			chars[str[i]-'a']++
		}
		idStr := string(chars)
		if _, ok := groupsDict[idStr]; ok {
			groupsDict[idStr] = append(groupsDict[idStr], str)
		} else {
			groupsDict[idStr] = []string{str}
		}
	}

	for _, g := range groupsDict {
		groups = append(groups, g)
	}
	return
}


func addBinary(a string, b string) string {
	i, j := len(a)-1, len(b)-1
	carry := '0'
	arr := make([]byte, max(i+1,j+1)+1)
	for i >= 0 || j >= 0 {
		iv, jv := '0', '0'
		if i >= 0 && a[i] == '1' {
			iv = '1'
		}
		if j >= 0 && b[j] == '1' {
			jv = '1'
		}

		result := iv+jv+carry
		if result == '1'*3 {
			arr[max(i,j)+1] = '1'
			carry = '1'
		} else if result == '1'*2 + '0' {
			arr[max(i,j)+1] = '0'
			carry = '1'
		} else if result == '1' + '0'*2 {
			arr[max(i,j)+1] = '1'
			carry = '0'
		} else {
			arr[max(i,j)+1] = '0'
			carry = '0'
		}

		if i <= 0 && j <= 0 {
			if carry == '1' {
				arr[0] = '1'
			} else {
				arr = arr[1:]
			}
		}
		i--
		j--
	}
	return string(arr)
}

type CharIndexTuple struct {
	char byte
	index int
}
func minWindow(s string, t string) (minSubString string) {
	charFreq := map[uint8]int{}
	for i := range t {
		charFreq[t[i]] += 1
	}

	filteredS := []CharIndexTuple{}
	for i := range s {
		if _, ok := charFreq[s[i]]; ok {
			filteredS = append(filteredS, CharIndexTuple{s[i], i})
		}
	}

	lo, hi := 0, 0
	patternLen := len(charFreq)
	minLo, minHi := math.MinInt32, math.MaxInt32
	for hi < len(filteredS) {
		tup := filteredS[hi]
		charFreq[tup.char]--

		if charFreq[tup.char] == 0 {
			patternLen--
		}

		if patternLen == 0 {
			for charFreq[filteredS[lo].char] <= 0 && lo <= hi {
				if filteredS[hi].index - filteredS[lo].index + 1 < minHi - minLo + 1 {
					minLo, minHi = filteredS[lo].index, filteredS[hi].index
				}

				charFreq[filteredS[lo].char]++
				lo++
				if charFreq[filteredS[lo-1].char] == 1 {
					break
				}
			}
			patternLen++
		}
		hi++
	}
	if minLo != math.MinInt32 {
		minSubString = s[minLo:minHi+1]
	}
	return
}

func isOneEditDistance(s string, t string) bool {
	if math.Abs(float64(len(s) - len(t))) > 1 {
		return false
	} else if len(s) + len(t) == 1 {
		return true
	} else if len(t) < len(s) {
		return isOneEditDistance(t, s)
	} else if s == t[:len(s)] {
		return len(s) != len(t)
	}

	diffCnt := 0
	for i, j := 0, 0; i < len(s) && j < len(t); {
		if len(s) == len(t) {
			if s[i] != t[i] {
				diffCnt++
			}
			i++
		} else {
			if s[i] != t[j] {
				diffCnt++
				j++
			} else {
				i++
				j++
			}
		}
	}
	return diffCnt == 1
}

func productExceptSelf(nums []int) []int {
	products := make([]int, len(nums))

	return products
}