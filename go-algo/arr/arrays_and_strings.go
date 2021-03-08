package arr

import (
	"container/heap"
	"fmt"
	"go-algo/collection"
	"go-algo/mathext"
	"go-algo/strext"
	"math"
	"sort"
	"strconv"
	"strings"
	"time"
)

func IsNumeric(s string) bool {
	_, err := strconv.ParseFloat(s, 64)
	return err == nil
}

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
	mh := collection.NewMyMinHeap([]int{})
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
			dist[i][req] = mathext.MinInt(up, down)
		}
	}

	idx, minDistAll := -1, math.MaxInt32
	for i, d := range dist {
		maxDistCurr := math.MinInt32
		for _, val := range d {
			maxDistCurr = mathext.MaxInt(val, maxDistCurr)
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
			lIdx++
			lWall = mathext.MaxInt(lWall, heights[lIdx])
			area += lWall - heights[lIdx]
		} else {
			rIdx--
			rWall = mathext.MaxInt(rWall, heights[rIdx])
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
		maxSum = mathext.MaxInt(maxSum, currSum)
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
		maxLen = mathext.MaxInt(hi-lo+1, maxLen)
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
			lo = mathext.MaxInt(lo, charSet[s[hi]]+1)
		}
		maxLen = mathext.MaxInt(maxLen, hi-lo+1)
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
		sum := ival + jval + carryover
		if i > 0 || j > 0 {
			returnVal = strconv.FormatInt(int64(sum%10), 10) + returnVal
			carryover = sum / 10
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
	arr := make([]byte, mathext.MaxInt(i+1, j+1)+1)
	for i >= 0 || j >= 0 {
		iv, jv := '0', '0'
		if i >= 0 && a[i] == '1' {
			iv = '1'
		}
		if j >= 0 && b[j] == '1' {
			jv = '1'
		}

		result := iv + jv + carry
		if result == '1'*3 {
			arr[mathext.MaxInt(i, j)+1] = '1'
			carry = '1'
		} else if result == '1'*2+'0' {
			arr[mathext.MaxInt(i, j)+1] = '0'
			carry = '1'
		} else if result == '1'+'0'*2 {
			arr[mathext.MaxInt(i, j)+1] = '1'
			carry = '0'
		} else {
			arr[mathext.MaxInt(i, j)+1] = '0'
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
	char  byte
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
				if filteredS[hi].index-filteredS[lo].index+1 < minHi-minLo+1 {
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
		minSubString = s[minLo : minHi+1]
	}
	return
}

func isOneEditDistance(s string, t string) bool {
	if math.Abs(float64(len(s)-len(t))) > 1 {
		return false
	} else if len(s)+len(t) == 1 {
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

func moveZeroes(nums []int) {
	lo, hi := 0, 0
	for lo < len(nums) && hi < len(nums) {
		if nums[lo] != 0 {
			lo++
		}
		if nums[hi] == 0 {
			hi++
		}
		if lo > hi {
			hi = lo + 1
			continue
		}

		if hi < len(nums) && nums[lo] == 0 && nums[hi] != 0 {
			nums[lo], nums[hi] = nums[hi], nums[lo]
			lo++
			hi++
		}
	}
}

func lengthOfLongestSubstringKDistinct(s string, k int) (maxLen int) {
	if k == 0 {
		return 0
	}

	freq := map[uint8]int{}
	lo, hi := 0, 0
	for hi < len(s) {
		if len(freq) < k || freq[s[hi]] > 0 {
			freq[s[hi]] += 1
		} else {
			for len(freq) == k {
				if freq[s[lo]] == 1 {
					delete(freq, s[lo])
				} else {
					freq[s[lo]]--
				}
				lo++
			}
		}
		maxLen = mathext.MaxInt(maxLen, hi-lo+1)
		hi++
	}
	return
}

type IpType int

const (
	IPv4 IpType = iota + 1
	IPv6
)

func validIPAddress(IP string) string {
	var ipGroups []string
	var ipType IpType
	if strings.Contains(IP, ".") && strings.Contains(IP, ":") {
		return "Neither"
	} else if strings.Contains(IP, ".") {
		ipGroups = strings.Split(IP, ".")
		ipType = IPv4
	} else if strings.Contains(IP, ":") {
		ipGroups = strings.Split(IP, ":")
		ipType = IPv6
	}

	if ipType == IPv4 && validateIpv4Address(ipGroups) {
		return "IPv4"
	} else if ipType == IPv6 && validateIpv6Address(ipGroups) {
		return "IPv6"
	}
	return "Neither"
}

func validateIpv4Address(ipGroups []string) (isValid bool) {
	if len(ipGroups) != 4 {
		return
	}

	for _, ipSection := range ipGroups {
		ipSecNum, err := strconv.Atoi(ipSection)
		if err != nil || ipSecNum < 0 || ipSecNum > 255 {
			return
		}
		if len(ipSection) == 0 {
			return
		}
		if len(ipSection) > 1 && strings.HasPrefix(ipSection, "0") {
			return
		}
	}

	return true
}

func validateIpv6Address(ipGroups []string) (isValid bool) {
	if len(ipGroups) != 8 {
		return
	}

	var lowerCaseLow, lowerCaseHigh uint8 = 'a', 'f'
	var upperCaseLow, upperCaseHigh uint8 = 'A', 'F'

	for _, ipSection := range ipGroups {
		if len(ipSection) == 0 || len(ipSection) > 4 {
			return
		}

		for i := range ipSection {

			_, err := strconv.Atoi(string(ipSection[i]))
			if err != nil &&
				!((ipSection[i] >= lowerCaseLow && ipSection[i] <= lowerCaseHigh) ||
					(ipSection[i] >= upperCaseLow && ipSection[i] <= upperCaseHigh)) {
				return
			}
		}
	}

	return true
}

// TODO: Come back to
func subarraySum(nums []int, k int) (cnt int) {
	lo, hi := 0, 0
	sum := 0
	for hi < len(nums) {
		sum += nums[hi]
		for (sum >= k && k >= 0) || (sum <= k && k < 0) && lo < len(nums) {
			if sum == k {
				cnt++
			}
			sum -= nums[lo]
			lo++
		}
		hi++
	}
	return
}

func validPalindrome(s string) bool {
	if len(s) <= 2 {
		return true
	}

	deleteCnt := 0
	lo, hi := 0, len(s)-1
	for lo <= hi {
		if s[lo] == s[hi] {
			lo++
			hi--
		} else if deleteCnt != 0 {
			return false
		} else {
			if lo+1 <= hi && s[lo+1] == s[hi] && (lo+2 > hi-1 || s[lo+2] == s[hi-1]) {
				lo++
				deleteCnt++
			} else if hi-1 >= lo && s[lo] == s[hi-1] && (hi-2 < lo+1 || s[lo+1] == s[hi-2]) {
				hi--
				deleteCnt++
			} else {
				return false
			}
		}
	}
	return true
}

// TODO: Come back to and improve time complexity
func divide(dividend int, divisor int) (cnt int) {
	isNegative := false
	if dividend < 0 {
		isNegative = !isNegative
		dividend = -dividend
	}
	if divisor < 0 {
		isNegative = !isNegative
		divisor = -divisor
	}

	for dividend >= divisor {
		cnt++
		dividend -= divisor
	}

	if isNegative {
		cnt = -cnt
	}
	if cnt < -1<<31 {
		cnt = -1 << 31
	} else if cnt > 1<<31-1 {
		cnt = 1<<31 - 1
	}
	return
}

func binarySearchSifted(nums []int, target int) int {
	if len(nums) == 0 {
		return -1
	}

	lo, hi := 0, len(nums)-1
	for lo <= hi {
		mid := (lo + hi) / 2
		if nums[mid] == target {
			return mid
		} else if nums[lo] <= nums[mid] {
			if target < nums[mid] && target >= nums[lo] {
				hi = mid - 1
			} else {
				lo = mid + 1
			}
		} else {
			if target > nums[mid] && target <= nums[hi] {
				lo = mid + 1
			} else {
				hi = mid - 1
			}
		}
	}
	return -1
}

type SearchDirection int

const (
	Forward SearchDirection = iota + 1
	Backward
)

func binarySearchRange(nums []int, lo, hi, target int, dir SearchDirection) int {
	idx := -1
	for lo <= hi {
		mid := (lo + hi) / 2
		if nums[mid] == target {
			idx = mid
			if dir == Forward {
				lo = mid + 1
			} else {
				hi = mid - 1
			}
		} else if target < nums[mid] {
			hi = mid - 1
		} else {
			lo = mid + 1
		}
	}
	return idx
}
func searchRange(nums []int, target int) []int {
	results := []int{-1, -1}
	if len(nums) == 0 {
		return results
	}

	low := binarySearchRange(nums, 0, len(nums)-1, target, Backward)
	if low == -1 {
		return results
	}
	results[0] = low
	results[1] = low

	high := binarySearchRange(nums, low+1, len(nums)-1, target, Forward)
	if high != -1 {
		results[1] = high
	}
	return results
}

func merge(intervals [][]int) [][]int {
	if len(intervals) <= 1 {
		return intervals
	}

	start, end := 0, 1
	sort.Slice(intervals, func(i, j int) bool {
		return intervals[i][start] <= intervals[j][start]
	})

	results := [][]int{intervals[0]}
	for i := 1; i < len(intervals); i++ {
		prev := results[len(results)-1]
		if prev[end] < intervals[i][start] {
			results = append(results, intervals[i])
		} else {
			prev[start] = mathext.MinInt(prev[start], intervals[i][start])
			prev[end] = mathext.MaxInt(prev[end], intervals[i][end])
		}
	}
	return results
}

func findPeakElement(nums []int) int {
	if len(nums) == 1 || nums[0] > nums[1] {
		return 0
	} else if nums[len(nums)-1] > nums[len(nums)-2] {
		return len(nums) - 1
	}

	lo, hi := 0, len(nums)-1
	for lo <= hi {
		mid := (lo + hi) / 2
		if mid+1 <= hi && nums[mid] < nums[mid+1] {
			lo = mid + 1
		} else if mid-1 >= lo && nums[mid] < nums[mid-1] {
			hi = mid - 1
		} else {
			return mid
		}
	}
	return -1
}

func isBadVersion(version int) bool {
	return true
}

func firstBadVersion(n int) int {
	if n == 1 {
		return 1
	}

	lo, hi := 1, n
	isBadIdx := -1
	for lo <= hi {
		mid := (lo + hi) / 2
		if isBadVersion(mid) {
			isBadIdx = mid
			hi = mid - 1
		} else {
			lo = mid + 1
		}
	}
	return isBadIdx
}

func intersection(nums1 []int, nums2 []int) []int {
	if len(nums1) == 0 || len(nums2) == 0 {
		return []int{}
	} else if len(nums2) < len(nums1) {
		return intersection(nums2, nums1)
	}

	m1, m2 := map[int]struct{}{}, map[int]struct{}{}
	for i := 0; i < len(nums1) || i < len(nums2); i++ {
		if i < len(nums1) {
			m1[nums1[i]] = struct{}{}
		}
		if i < len(nums2) {
			m2[nums2[i]] = struct{}{}
		}
	}
	results := make([]int, 0, len(m1))
	for num := range m1 {
		if _, ok := m2[num]; ok {
			results = append(results, num)
		}
	}
	return results
}

func intersection2(nums1 []int, nums2 []int) (results []int) {
	if len(nums1) == 0 || len(nums2) == 0 {
		return []int{}
	} else if len(nums2) < len(nums1) {
		return intersection2(nums2, nums1)
	}
	sort.Ints(nums1)
	sort.Ints(nums2)

	for i, j := 0, 0; i < len(nums1) && j < len(nums2); {
		if nums1[i] == nums2[j] {
			results = append(results, nums1[i])
			i++
			j++
		} else {
			if nums1[i] < nums2[j] {
				i++
			} else {
				j++
			}
		}
	}
	return
}

func productExceptSelf(nums []int) []int {
	results, left, right := make([]int, len(nums)), make([]int, len(nums)), make([]int, len(nums))
	left[0], right[len(nums)-1] = 1, 1
	for i, j := 0, len(nums)-1; i < len(nums) && j >= 0; i, j = i+1, j-1 {
		if i > 0 {
			left[i] = left[i-1] * nums[i-1]
		}
		if j < len(nums)-1 {
			right[i] = right[i+1] * nums[i+1]
		}
	}
	for i := range results {
		results[i] = left[i] * right[i]
	}
	return results
}

func rotate(matrix [][]int) {

}

/*func strStr(haystack string, needle string) int {
	if needle == "" {return 0}
	else if len(needle) > len(haystack) {return -1}
	p1, p2 := 0, 0
	for i := range haystack {


	}
	return -1
}*/

func MostCommonWord(paragraph string, banned []string) string {
	paragraph = strings.ToLower(string(strext.RemoveNonAlphaNumeric([]byte(paragraph))))
	bannedSet := map[string]bool{}
	wordCnt := map[string]int{}
	maxWord, maxCount := "", 0
	n := len(paragraph)
	for _, word := range banned {
		bannedSet[word] = true
	}
	for lo, hi := 0, 0; hi <= n; hi++ {
		if hi == n || paragraph[hi] == ' ' {
			word := paragraph[lo:hi]
			if !bannedSet[word] {
				wordCnt[word] += 1
				if wordCnt[word] > maxCount {
					maxCount = wordCnt[word]
					maxWord = word
				}
			}
			lo = hi + 1
		}
	}
	return maxWord
}

func trap(height []int) int {
	if len(height) <= 1 {
		return 0
	}
	lo, hi := 0, len(height)-1
	sum, lmax, rmax := 0, height[lo], height[hi]

	for lo < hi {
		if height[lo] < height[hi] {
			lo++
			lmax = int(math.Max(float64(lmax), float64(height[lo])))
			sum += lmax - height[lo]
		} else {
			hi--
			rmax = int(math.Max(float64(rmax), float64(height[hi])))
			sum += rmax - height[hi]
		}
	}
	return sum
}

type LogType int

const (
	Letter LogType = iota + 1
	Digit
)

func reorderLogFiles(logs []string) []string {
	sort.SliceStable(logs, func(i, j int) bool {
		iIdIndex := strings.Index(logs[i], " ")
		jIdIndex := strings.Index(logs[j], " ")
		iLogType, jLogType := Letter, Letter
		if _, err := strconv.Atoi(logs[i][iIdIndex+1 : iIdIndex+2]); err == nil {
			iLogType = Digit
		}
		if _, err := strconv.Atoi(logs[j][jIdIndex+1 : jIdIndex+2]); err == nil {
			jLogType = Digit
		}

		if iLogType == Digit && jLogType == Digit {
			return i < j
		} else if iLogType != jLogType {
			return iLogType < jLogType
		} else {
			if logs[i][iIdIndex+1:] == logs[j][jIdIndex+1:] {
				return logs[i][:iIdIndex] <= logs[j][:jIdIndex]
			} else {
				return logs[i][iIdIndex+1:] < logs[j][jIdIndex+1:]
			}
		}
	})
	return logs
}

type PointHeap [][]int

func (p PointHeap) Len() int {
	return len(p)
}

func (p PointHeap) Less(i, j int) bool {
	return !less(p[i], p[j])
}

func (p PointHeap) Swap(i, j int) {
	p[i], p[j] = p[j], p[i]
}

func (p *PointHeap) Push(val interface{}) {
	*p = append(*p, val.([]int))
}

func (p *PointHeap) Pop() interface{} {
	val := (*p)[len(*p)-1]
	*p = (*p)[:len(*p)-1]
	return val
}

func getEuclideanDistanceToOrigin(p []int) float64 {
	return math.Sqrt(math.Pow(float64(p[0]), 2) + math.Pow(float64(p[1]), 2))
}

func less(p1, p2 []int) bool {
	return getEuclideanDistanceToOrigin(p1) < getEuclideanDistanceToOrigin(p2)
}

func kClosest(points [][]int, K int) [][]int {
	ph := &PointHeap{}
	for _, point := range points {
		if len(*ph) < K || less(point, (*ph)[0]) {
			heap.Push(ph, point)
			if len(*ph) > K {
				heap.Pop(ph)
			}
		}
	}
	return *ph
}

func kClosestUsingSort(points [][]int, K int) [][]int {
	sort.Slice(points, func(i, j int) bool {
		return less(points[i], points[j])
	})
	results := make([][]int, 0, K)
	for i := 0; i < K; i++ {
		results = append(results, points[i])
	}
	return results
}

func maxProfit(prices []int) int {
	if len(prices) <= 1 {
		return 0
	}
	maxRight := prices[len(prices)-1]
	maxP := 0
	for i := len(prices) - 2; i >= 0; i-- {
		if prices[i] > maxRight {
			maxRight = prices[i]
		}
		if maxRight-prices[i] > maxP {
			maxP = maxRight - prices[i]
		}
	}
	return maxP
}

func DivisibleSumPairs(n int32, k int32, ar []int32) int32 {
	var ways int32
	for i := range ar {
		for j := i + 1; j < len(ar); j++ {
			if float32(ar[i]+ar[j])/float32(k) == 1.0 {
				ways++
			}
		}
	}
	return ways
}

func MaxBinaryGap(N int) int {
	if N <= 4 {
		return 0
	}
	biStr := strconv.FormatInt(int64(N), 2)
	lo, hi, maxGap := 0, 0, 0
	for hi < len(biStr) {
		if hi > lo && biStr[lo] == '1' && biStr[hi] == '1' {
			if hi-lo-1 > maxGap {
				maxGap = hi - lo - 1
			}
			lo = hi
			hi++
		} else {
			if biStr[lo] != '1' {
				lo++
			}
			if hi <= lo {
				hi++
			}
			if hi < len(biStr) && biStr[hi] != '1' {
				hi++
			}
		}
	}
	return maxGap
}

func FindMissingInt(A []int) int {
	if len(A) == 1 {
		return 1
	}
	for i := range A {
		if mathext.AbsInt(A[i]) <= len(A) {
			A[mathext.AbsInt(A[i])-1] = -A[mathext.AbsInt(A[i])-1]
		}
	}
	for i := range A {
		if A[i] > 0 {
			return i + 1
		}
	}
	return -1
}

func MinTapeDiff(A []int) int {
	totalSum := 0
	for _, num := range A {
		totalSum += num
	}

	lSum, rSum := 0, totalSum
	minDiff := 1<<31 - 1

	for _, num := range A {
		lSum += num
		rSum -= num
		minDiff = mathext.MinInt(minDiff, mathext.AbsInt(lSum-rSum))
	}
	return minDiff
}

func RepeatedString(s string, n int64) int64 {
	if len(s) == 0 {
		return 0
	} else if len(s) == 1 {
		if s[0] == 'a' {
			return n
		}
		return 0
	} else if int(n) < len(s) {
		return getACount(s, int(n))
	}

	aCnt := getACount(s, len(s))
	aCnt *= n / int64(len(s))
	aCnt += getACount(s, int(n)%len(s))
	return aCnt
}

func getACount(s string, hi int) int64 {
	var aCnt int64
	for i := 0; i < hi; i++ {
		if s[i] == 'a' {
			aCnt++
		}
	}
	return aCnt
}

func RotateLeft(a []int32, d int32) []int32 {
	n := len(a)
	k := int(d) % n
	if k == 0 {
		return a
	}

	cntr, start, idx := 0, len(a)-1, len(a)-1
	var prev = a[idx]
	for cntr < len(a) {
		nextIdx := mathext.Modulo(idx-k, n)
		tmp := a[nextIdx]
		a[nextIdx] = prev
		prev = tmp
		idx = nextIdx
		cntr++
		if idx == start {
			idx--
			prev = a[idx]
			start = idx
		}
	}
	return a
}

func ArrayManipulation(n int32, queries [][]int32) int64 {
	if len(queries) == 0 {
		return 0
	}
	if len(queries) == 1 {
		return int64(queries[0][2])
	}
	vals := make([]int64, n)
	var maxVal int64
	for _, query := range queries {
		vals[query[0]-1] += int64(query[2])
		if query[1] < int32(len(vals)) {
			vals[query[1]] -= int64(query[2])
		}
	}
	var currVal int64
	for _, val := range vals {
		currVal += val
		maxVal = mathext.MaxInt64(maxVal, currVal)
	}
	return maxVal
}

func MinimumBribes(q []int32) {
	var bribeCnt int32
	for i := int32(len(q) - 1); i >= 0; i-- {
		if q[i]-(i+1) > 2 {
			fmt.Println("Too chaotic")
			return
		}
		for j := mathext.MaxInt32(q[i]-2, 0); j < i; j++ {
			if q[j] > q[i] {
				bribeCnt++
			}
		}
	}
	fmt.Println(bribeCnt)
}

func IsValidSherlockString(s string) string {
	charToFreqs := map[string]int{}

	for i := range s {
		charToFreqs[s[i:i+1]] += 1
	}

	maxFreq, minFreq := 0, 1<<31-1
	freqToChars := map[int][]string{}
	for c, v := range charToFreqs {
		if v > maxFreq {
			maxFreq = v
		}
		if v < minFreq {
			minFreq = v
		}
		freqToChars[v] = append(freqToChars[v], c)
	}
	fmt.Println(freqToChars)
	if len(freqToChars) == 1 {
		return "YES"
	} else if len(freqToChars) > 2 {
		return "NO"
	} else {
		lMax, lMin := len(freqToChars[maxFreq]), len(freqToChars[minFreq])
		if (lMax > 1 && lMin > 1) || (mathext.MinInt(lMax, lMin)+1 != mathext.MaxInt(lMax, lMin) && mathext.MinInt(lMax, lMin) > 1) {
			return "NO"
		} else if maxFreq-minFreq > 1 && lMin > 1 {
			return "NO"
		}
		return "YES"
	}
}

func SubStringsOfSizeKDistinct(s string, k int) []string {
	idx_map := map[byte]int{}
	lo, hi := 0, 0
	resMap := map[string]struct{}{}
	for hi < len(s) {
		if _, ok := idx_map[s[hi]]; ok {
			lo = mathext.MaxInt(lo, idx_map[s[hi]]+1)
		}
		for hi-lo+1 > k {
			lo++
		}
		if hi-lo+1 == k {
			resMap[s[lo:hi+1]] = struct{}{}
		}
		idx_map[s[hi]] = hi
		hi++
	}
	resList := make([]string, 0, len(resMap))
	for str := range resMap {
		resList = append(resList, str)
	}
	return resList
}

func NumberOfItems(str string, ranges [][]int) (res []int) {
	prefixSums := map[int]int{}
	currSum := 0
	for i := range str {
		if str[i] == '|' {
			prefixSums[i] = currSum
		} else {
			currSum += 1
		}
	}
	leftBounds, rightBounds := make([]int, len(str)), make([]int, len(str))
	lb, rb := -1, -1
	n := len(str)
	for i, j := 0, n-1; i < n; i, j = i+1, j-1 {

		if str[i] == '|' {
			lb = i
		}
		leftBounds[i] = lb

		if str[j] == '|' {
			rb = j
		}
		rightBounds[j] = rb
	}

	for _, r := range ranges {
		start := rightBounds[r[0]]
		end := leftBounds[r[1]]
		if start < end && start != -1 && end != -1 {
			res = append(res, prefixSums[end]-prefixSums[start])
		}
	}
	return
}

func UtilizationScaling(avgs []int, numInstances int) int {

	for i := 0; i < len(avgs); {
		actionTaken := false
		if avgs[i] < 25 && numInstances > 1 {
			numInstances = int(math.Ceil(float64(numInstances) / 2))
			i += 10
			actionTaken = true
		} else if avgs[i] > 60 && numInstances*2 < int(2*math.Pow(10, 8)) {
			numInstances *= 2
			i += 10
			actionTaken = true
		}
		if !actionTaken {
			i++
		}
	}
	return numInstances
}

func IncrementCounters(N int, A []int) []int {
	cntrs := make([]int, N)
	maxCntr := 0
	globalMax := 0
	for i := range A {
		if A[i] == N+1 {
			globalMax = maxCntr
		} else {
			cntrs[A[i]-1] = max(cntrs[A[i]-1]+1, globalMax+1)
			maxCntr = max(maxCntr, cntrs[A[i]-1])
		}
	}

	for i := range cntrs {
		if cntrs[i] < globalMax {
			cntrs[i] = globalMax
		}
	}
	return cntrs
}

func max(n1, n2 int) int {
	if n1 >= n2 {return n1}
	return n2
}