package arr

import (
	"bytes"
	"container/heap"
	"fmt"
	"github.com/itroot/keysort"
	"go-algo/collection"
	"go-algo/ext/fmtext"
	"go-algo/ext/mathext"
	"go-algo/ext/strext"
	"math"
	"math/rand"
	"regexp"
	"sort"
	"strconv"
	"strings"
	"time"
)

type Direction int

const (
	Left Direction = iota + 1
	Right
	Down
	Up
)

type Point struct {
	x, y int
}

func maxAreaOfIsland(grid [][]int) int {
	if len(grid) == 0 {
		return 0
	}

	que := [][]int{}
	rows, cols := len(grid), len(grid[0])
	maxArea := 0
	dirs := [][]int{{0, 1}, {1, 0}, {0, -1}, {-1, 0}}

	var isValidPoint = func(x, y int) bool {
		return x >= 0 && x < rows && y >= 0 && y < cols
	}

	var max = func(nums ...int) int {
		currMax := nums[0]
		for _, num := range nums {
			if num > currMax {
				currMax = num
			}
		}
		return currMax
	}

	var computeIslandArea = func(x, y int) int {
		area := 0
		que = append(que, []int{x, y})

		for len(que) > 0 {
			area++
			n := len(que)
			currX, currY := que[n-1][0], que[n-1][1]
			que = que[:n-1]

			for _, dir := range dirs {
				newX, newY := currX+dir[0], currY+dir[1]
				if isValidPoint(newX, newY) && grid[newX][newY] == 1 {
					grid[newX][newY] = 0
					que = append(que, []int{newX, newY})
				}
			}
		}
		return area
	}

	for x := 0; x < rows; x++ {
		for y := 0; y < cols; y++ {
			if grid[x][y] == 1 {
				grid[x][y] = 0
				maxArea = max(maxArea, computeIslandArea(x, y))
			}
		}
	}

	return maxArea
}

func DecodeString(s string) string {
	stk := []byte{}
	openIndexes := []int{}
	repeatIndexes := []int{}

	var isNumber = func(b byte) bool {
		return b >= '0' && b <= '9'
	}

	for i := range s {
		ch := s[i]
		if ch == ']' {
			n, m := len(openIndexes), len(repeatIndexes)
			openIdx, repeatIdx := openIndexes[n-1], repeatIndexes[m-1]
			openIndexes, repeatIndexes = openIndexes[:n-1], repeatIndexes[:m-1]

			repeatCnt, _ := strconv.Atoi(string(stk[repeatIdx:openIdx]))
			repeatBytes := bytes.Repeat(stk[openIdx+1:], repeatCnt)
			stk = stk[:repeatIdx]
			stk = append(stk, repeatBytes...)
		} else {
			stk = append(stk, ch)
			n := len(stk)
			if ch == '[' {
				openIndexes = append(openIndexes, n-1)
			} else if isNumber(s[i]) && (i == 0 || !isNumber(s[i-1])) {
				repeatIndexes = append(repeatIndexes, n-1)
			}
		}
	}

	return string(stk)
}

// TODO:
func maxKSumCombinations(n1, n2 []int, k int) (results []int) {
	if k == 0 {
		return results
	}
	n1Heap := collection.NewIntMaxHeap(n1)
	n2Heap := collection.NewIntMaxHeap(n2)

	n1Val, n2Val := n1Heap.HeapPop(), n2Heap.HeapPop()
	for len(results) < k {
		results = append(results, n1Val+n2Val)
		if len(results) == k {
			break
		}

		if n1Val+n2Heap.Peek() >= n2Val+n1Heap.Peek() {
			n2Val = n2Heap.HeapPop()
		} else {
			n1Val = n1Heap.HeapPop()
		}
	}
	return results
}

func LongestConsecutive(nums []int) int {
	if len(nums) == 0 {
		return 0
	}
	numSet := map[int]bool{}
	for _, num := range nums {
		numSet[num] = true
	}

	maxConsec := 1
	for num := range numSet {
		if !numSet[num-1] {
			l := 1
			for numSet[num+1] {
				l++
				num += 1
			}
			maxConsec = mathext.MaxInt(maxConsec, l)
		}
	}
	return maxConsec
}

func Subsets(nums []int) [][]int {
	results := [][]int{}
	sort.Ints(nums)
	var traverse func(idx int, set []int)
	traverse = func(idx int, set []int) {
		temp := make([]int, len(set))
		copy(temp, set)
		results = append(results, temp)
		for j := idx; j < len(nums); j++ {
			set = append(set, nums[j])
			traverse(j+1, set)
			set = set[:len(set)-1]
		}
	}
	traverse(0, []int{})
	return results
}

func NextGreater(nums []int) []int {
	n := len(nums)
	results := make([]int, n)
	stk := []int{}
	for i := n - 1; i >= 0; i-- {
		for len(stk) > 0 && stk[len(stk)-1] <= nums[i] {
			stk = stk[:len(stk)-1]
		}

		val := -1
		if len(stk) > 0 {
			val = stk[len(stk)-1]
		}
		results[i] = val
		stk = append(stk, nums[i])
	}
	return results
}

func topKFrequent(nums []int, k int) []int {
	freqMap := map[int]int{}
	keys := []int{}
	for _, num := range nums {
		freqMap[num] += 1
		if freqMap[num] == 1 {
			keys = append(keys, num)
		}
	}

	var partition func(left, right, pivotIdx int) int
	partition = func(left, right, pivotIdx int) int {
		pivotFreq := freqMap[keys[pivotIdx]]
		keys[pivotIdx], keys[right] = keys[right], keys[pivotIdx]

		newPivotIdx := left
		for i := left; i < right; i++ {
			if freqMap[keys[i]] < pivotFreq {
				keys[newPivotIdx], keys[i] = keys[i], keys[newPivotIdx]
				newPivotIdx++
			}
		}

		keys[newPivotIdx], keys[right] = keys[right], keys[newPivotIdx]
		return newPivotIdx
	}

	var quickSelect func(left, right, kthSmallestIdx int)
	quickSelect = func(left, right, kthSmallestIdx int) {
		if left == right {
			return
		}

		rand.Seed(time.Now().UnixNano())
		pivotIdx := rand.Intn((right+1)-left) + left
		pivotIdx = partition(left, right, pivotIdx)

		if kthSmallestIdx == pivotIdx {
			return
		} else if kthSmallestIdx < pivotIdx {
			quickSelect(left, pivotIdx-1, kthSmallestIdx)
		} else {
			quickSelect(pivotIdx+1, right, kthSmallestIdx)
		}
	}

	n := len(nums)
	quickSelect(0, n-1, n-k)
	return keys[n-k:]
}

func MinimumAreaRectangle(points [][]int) int {
	pointSet := map[Point]bool{}
	for _, point := range points {
		pointSet[Point{point[0], point[1]}] = true
	}

	minArea := 1<<31 - 1
	for i := 0; i < len(points); i++ {
		for j := i + 1; j < len(points); j++ {
			p1 := Point{points[i][0], points[i][1]}
			p2 := Point{points[j][0], points[j][1]}
			if p1.x == p2.x || p1.y == p2.y {
				continue
			} else if !pointSet[Point{p1.x, p2.y}] || !pointSet[Point{p2.x, p1.y}] {
				continue
			}

			area := mathext.AbsInt(p1.x-p2.x) * mathext.AbsInt(p1.y-p2.y)
			minArea = mathext.MinInt(minArea, area)
		}
	}
	return minArea
}

func nonRepeatingCharacters(str string) string {
	b := []byte{}
	freq := map[byte]int{}
	que := []byte{}

	for i := range str {
		freq[str[i]] += 1
		if freq[str[i]] == 1 {
			que = append(que, str[i])
		}

		for len(que) > 0 && freq[que[0]] >= 2 {
			que = que[1:]
		}

		if len(que) > 0 {
			b = append(b, que[0])
		} else {
			b = append(b, '#')
		}
	}
	return string(b)
}

func slidingMaximum(nums []int, k int) []int {
	que := []int{}
	lo, hi := 0, 0
	res := []int{}
	for hi < len(nums) {
		if hi-lo+1 > k {
			if que[0] == nums[lo] {
				que = que[1:]
			}
			lo++
		}

		for len(que) > 0 && nums[hi] > que[len(que)-1] {
			que = que[:len(que)-1]
		}

		que = append(que, nums[hi])
		if hi-lo+1 == k {
			res = append(res, que[0])
		}
		hi++
	}
	return res
}

func prevSmaller(nums []int) []int {
	stk := []int{}
	res := []int{}

	for i, num := range nums {
		for len(stk) > 0 && stk[len(stk)-1] >= num {
			stk = stk[:len(stk)-1]
		}

		if i == 0 || len(stk) == 0 {
			res = append(res, -1)
		} else {
			res = append(res, stk[len(stk)-1])
		}
		stk = append(stk, num)
	}
	return res
}

func isPalindrome(A string) int {
	reg := regexp.MustCompile("[\\w]+")
	str := strings.ToLower(strings.Join(reg.FindAllString(A, -1), ""))
	for i, j := 0, len(str)-1; i < j; i, j = i+1, j-1 {
		if str[i] != str[j] {
			return 0
		}
	}
	return 1
}

func ConcentricMatrix(n int) [][]int {
	l := 2*n - 1
	matrix := [][]int{}
	for i := 1; i <= l; i++ {
		row := []int{}
		for j := 1; j <= l; j++ {
			row = append(row, mathext.MaxInt(mathext.AbsInt(n-i)+1, mathext.AbsInt(n-j)+1))
		}
		matrix = append(matrix, row)
	}
	return matrix
}

func RearrangeArr(nums []int) []int {
	n := len(nums)
	for i := range nums {
		nums[i] += (nums[nums[i]] % n) * n
	}

	fmt.Println(nums)
	for i := range nums {
		nums[i] /= n
	}
	return nums
}

func ReverseInt(n int) int {
	isNeg := n < 0
	if isNeg {
		n = -n
	}

	rev := 0
	for n > 0 {
		lastDig := n % 10
		rev = rev*10 + lastDig
		n /= 10
	}

	if isNeg {
		rev = -rev
	}
	if rev > 1<<31-1 || rev < -1<<31 {
		rev = 0
	}
	return rev
}

func PossibleSubsets(strList []string) {
	n := len(strList)
	for i := 0; i < (1 << n); i++ {
		for j := 0; j < n; j++ {
			if (i & (1 << j)) > 0 {
				fmt.Print(strList[j] + " ")
			}
		}
		fmt.Println()
	}
}

type Interval struct {
	start, end int
}

func CanSchedule(schedule []Interval, job Interval) (canInsert bool) {
	if len(schedule) == 0 {
		return true
	}

	// sort by start
	sort.Slice(schedule, func(i, j int) bool {
		return schedule[i].start < schedule[j].start
	})

	lo, hi := 0, len(schedule)-1
	for lo <= hi {
		mid := (hi + lo) / 2
		if canInsertBeforeMid(schedule, job, mid) || canInsertAfterMid(schedule, job, mid) {
			return true
		} else if job.start < schedule[mid].start {
			hi = mid - 1
		} else {
			lo = mid + 1
		}
	}
	return false
}

func canInsertBeforeMid(schedule []Interval, job Interval, mid int) bool {
	return job.end <= schedule[mid].start && (mid == 0 || schedule[mid-1].end <= job.start)
}

func canInsertAfterMid(schedule []Interval, job Interval, mid int) bool {
	return job.start >= schedule[mid].end && (mid == len(schedule)-1 || schedule[mid+1].start >= job.end)
}

func SumHammingDistance(nums []int) int {
	sumHammingDist := 0
	for i := range nums {
		for j := i + 1; j < len(nums); j++ {
			xor := nums[i] ^ nums[j]
			cnt := 0
			for xor > 0 {
				cnt++
				xor = xor & (xor - 1)
			}

			sumHammingDist += cnt * 2
		}
	}
	return sumHammingDist % 1000000007
}

func PrimeSum(n int) []int {
	primes := make([]bool, n+1)
	for i := range primes {
		primes[i] = true
	}
	primes[0], primes[1] = false, false

	for i := 2; i*i <= n; i++ {
		if !primes[i] {
			continue
		}

		for j := i * i; j <= n; j += i {
			primes[j] = false
		}
	}

	res := []int{-1, -1}
	for i, j := 0, len(primes)-1; i <= j; {
		skip := false
		if !primes[i] {
			i++
			skip = true
		}
		if !primes[j] {
			j--
			skip = true
		}
		if skip {
			continue
		}

		sum := i + j
		if sum == n {
			res[0], res[1] = i, j
			break
		} else if sum > n {
			j--
		} else {
			i++
		}
	}

	return res
}

func FindDigitsInBinary(n int) string {
	if n == 0 {
		return "0"
	}

	b := []string{}
	for n > 0 {
		b = append(b, strconv.Itoa(n%2))
		n /= 2
	}
	for i, j := 0, len(b)-1; i < j; i, j = i+1, j-1 {
		b[i], b[j] = b[j], b[i]
	}
	return strings.Join(b, "")
}

func Sieve(n int) []int {
	primes := map[int]bool{}
	for i := 2; i <= n; i++ {
		primes[i] = true
	}

	for i := 3; i*i <= n; i++ {
		if i%2 == 0 {
			primes[i] = false
		}
	}

	for i := 2; i <= n; i++ {
		for f := 2; i*f <= n; f++ {
			primes[i*f] = false
		}
	}

	res := []int{}
	for i := 2; i <= n; i++ {
		if primes[i] {
			res = append(res, i)
		}
	}
	return res
}

func ValidateStackSequences(pushed []int, popped []int) bool {
	stk := []int{}
	for _, num := range pushed {
		stk = append(stk, num)
		for len(popped) > 0 && len(stk) > 0 && stk[len(stk)-1] == popped[0] {
			stk = stk[:len(stk)-1]
			popped = popped[1:]
		}
	}
	return len(popped) == 0
}

// TODO
func FindIndexExtraChar(str1, str2 string) int {
	return -1
}

func IsRectangleOverlap(rec1 []int, rec2 []int) bool {
	if rec1[0] == rec1[2] || rec1[1] == rec1[3] || rec2[0] == rec2[2] || rec2[1] == rec2[3] {
		return false
	}
	if rec1[0] >= rec2[2] || rec2[0] >= rec1[2] {
		return false
	}
	if rec1[1] >= rec2[3] || rec2[1] >= rec1[3] {
		return false
	}
	return true
}

func countOfAtoms(formula string) string {
	stk := []byte{}
	i := 0
	for i < len(formula) {
		b := formula[i]
		if b != ')' {
			stk = append(stk, b)
			i++
			continue
		}
	}

	return ""
}

func coverPoints(A []int, B []int) int {
	if len(A) == 0 || len(B) == 0 || len(A) != len(B) {
		return 0
	}
	cnt := 0
	x, y := A[0], B[0]
	n := len(A)
	for i := 1; i < n; i++ {
		x2, y2 := A[i], B[i]
		d1, d2 := mathext.AbsInt(x-x2), mathext.AbsInt(y-y2)
		cnt += d1 + d2
		if x != x2 && y != y2 {
			cnt -= mathext.MinInt(d1, d2)
		}
		x, y = x2, y2
	}
	return cnt
}

func MaxSubArrayLen(nums []int, k int) int {
	maxLen := 0
	sumLens := map[int]int{}
	sum := 0
	for i, num := range nums {
		sum += num
		if sum == k {
			maxLen = i + 1
		} else if loIdx, ok := sumLens[sum-k]; ok {
			maxLen = mathext.MaxInt(maxLen, i-loIdx)
		}

		if _, ok := sumLens[sum]; !ok {
			sumLens[sum] = i
		}
	}

	return maxLen
}

// TODO:
func AddOperators(num string, target int) (results []string) {
	if len(num) == 0 {
		return results
	}

	n := len(num)
	var dfs func(idx, currentVal int, str string)
	dfs = func(idx, currentVal int, str string) {
		currNum, _ := strconv.Atoi(string(num[idx]))
		newStrMulti := str + "*" + string(num[idx])
		newStrPlus := str + "+" + string(num[idx])
		newStrMinus := str + "-" + string(num[idx])

		if idx == n-1 {
			if currentVal*currNum == target {
				results = append(results, newStrMulti)
			}
			if currentVal+currNum == target {
				results = append(results, newStrPlus)
			}
			if currentVal-currNum == target {
				results = append(results, newStrMinus)
			}
			return
		}

		dfs(idx+1, currentVal*currNum, newStrMulti)
		dfs(idx+1, currentVal+currNum, newStrPlus)
		dfs(idx+1, currentVal-currNum, newStrMinus)
	}

	initVal, _ := strconv.Atoi(string(num[0]))
	dfs(1, initVal, string(num[0]))
	return results
}

func MinDifficulty(jobDifficulty []int, d int) (minDiff int) {
	n := len(jobDifficulty)
	if n < d {
		return -1
	}
	sort.Ints(jobDifficulty)
	i := 0
	for d > 1 && i < n-1 {
		minDiff += jobDifficulty[i]
		i++
		d--
	}

	minDiff += jobDifficulty[n-1]
	return minDiff
}

func SpiralOrder(matrix [][]int) []int {
	m, n := len(matrix), len(matrix[0])
	total := m * n
	xTop, xBot := 0, m-1
	yLeft, yRight := 0, n-1
	x, y := 0, 0
	dir := Right
	result := make([]int, 0, total)
	for len(result) < total {
		for dir == Right {
			result = append(result, matrix[x][y])
			if y == yRight {
				xTop++
				x++
				dir = changeDirection(dir)
				break
			}
			y++
		}
		if len(result) == total {
			break
		}

		for dir == Down {
			result = append(result, matrix[x][y])
			if x == xBot {
				yRight--
				y--
				dir = changeDirection(dir)
				break
			}
			x++
		}
		if len(result) == total {
			break
		}

		for dir == Left {
			result = append(result, matrix[x][y])
			if y == yLeft {
				xBot--
				x--
				dir = changeDirection(dir)
				break
			}
			y--
		}
		if len(result) == total {
			break
		}

		for dir == Up {
			result = append(result, matrix[x][y])
			if x == xTop {
				yLeft++
				y++
				dir = changeDirection(dir)
				break
			}
			x--
		}
		if len(result) == total {
			break
		}

	}
	return result
}

func changeDirection(dir Direction) Direction {
	switch dir {
	case Right:
		return Down
	case Down:
		return Left
	case Left:
		return Up
	default:
		return Right
	}
}

func FindMedianSortedArrays(nums1 []int, nums2 []int) float64 {
	n1, n2 := len(nums1), len(nums2)
	if n2 < n1 {
		return FindMedianSortedArrays(nums2, nums1)
	}

	n := n1 + n2
	start, end := 0, n1-1

	for {
		p1 := start + end
		if p1 > 0 {
			p1 /= 2
		}
		p2 := ((n + 1) / 2) - (p1 + 2)
		n1Lo, n1Hi := -1<<31, 1<<31-1
		n2Lo, n2Hi := -1<<31, 1<<31-1
		if p1 >= 0 {
			n1Lo = nums1[p1]
		}
		if p2 >= 0 {
			n2Lo = nums2[p2]
		}
		if p1+1 < len(nums1) {
			n1Hi = nums1[p1+1]
		}
		if p2+1 < len(nums2) {
			n2Hi = nums2[p2+1]
		}

		if n1Lo <= n2Hi && n2Lo <= n1Hi {
			maxOfLo := float64(mathext.MaxInt(n1Lo, n2Lo))
			if n%2 == 1 {
				return maxOfLo
			}
			minOfHi := float64(mathext.MinInt(n1Hi, n2Hi))
			return (maxOfLo + minOfHi) / 2
		} else if n1Lo > n2Hi {
			end = p1 - 1
		} else {
			start = p1 + 1
		}
	}
}

func MergeSortConcurrent(data []int) []int {
	if len(data) <= 1 {
		return data
	}
	done := make(chan bool)
	mid := len(data) / 2
	var left, right []int

	go func() {
		left = MergeSortConcurrent(data[:mid])
		done <- true
	}()
	go func() {
		right = MergeSortConcurrent(data[mid:])
		done <- true
	}()
	<-done
	<-done
	return merge(left, right)
}

func MergeSort(data []int) []int {
	if len(data) <= 1 {
		return data
	}

	mid := len(data) / 2
	left := MergeSort(data[:mid])
	right := MergeSort(data[mid:])
	return merge(left, right)
}

func merge(left, right []int) []int {
	merged := make([]int, 0, len(left)+len(right))
	for len(left) > 0 || len(right) > 0 {
		if len(left) == 0 {
			return append(merged, right...)
		} else if len(right) == 0 {
			return append(merged, left...)
		} else if left[0] < right[0] {
			merged = append(merged, left[0])
			left = left[1:]
		} else {
			merged = append(merged, right[0])
			right = right[1:]
		}
	}
	return merged
}

func ShortestDistToStore(houses, stores []int) (closestStores []int) {
	sort.Ints(stores)
	n := len(stores)
	houseToStore := map[int]int{}

	var binarySearchClosest func(house int) (closestStore int)
	binarySearchClosest = func(house int) (closestStore int) {
		closest := stores[0]
		lo, hi := 0, n-1
		for lo <= hi {
			mid := (lo + hi) / 2
			store := stores[mid]
			if store == house {
				closest = store
				break
			} else if store < house {
				lo = mid + 1
			} else {
				hi = mid - 1
			}

			if store == closest && store < closest {
				closest = store
			} else if mathext.AbsInt(store-house) < mathext.AbsInt(closest-house) {
				closest = store
			}
		}
		return closest
	}

	for _, house := range houses {
		if store, ok := houseToStore[house]; ok {
			closestStores = append(closestStores, store)
		} else {
			closestStore := binarySearchClosest(house)
			houseToStore[house] = closestStore
			closestStores = append(closestStores, closestStore)
		}
	}

	return closestStores
}

func TotalFruit(trees []int) int {
	if len(trees) == 0 {
		return 0
	}

	treeIdxs := map[int]int{}
	maxFruit := -1 << 31
	lo := 0
	for hi, tree := range trees {
		if _, ok := treeIdxs[tree]; !ok && len(treeIdxs) == 2 {
			removedTree := -1
			for rt := range treeIdxs {
				if rt != trees[hi-1] {
					removedTree = rt
					break
				}
			}
			lo = treeIdxs[removedTree] + 1
			delete(treeIdxs, removedTree)
		}

		treeIdxs[tree] = hi
		maxFruit = mathext.MaxInt(maxFruit, hi-lo+1)
	}
	return maxFruit
}

func NumUniqueEmails(emails []string) (cnt int) {
	domainToLocal := map[string]map[string]struct{}{}
	for i := range emails {
		emailParts := strings.Split(emails[i], "@")
		plusIdx := strings.Index(emailParts[0], "+")
		if plusIdx == 0 {
			continue
		} else if plusIdx > 0 {
			emailParts[0] = emailParts[0][:plusIdx]
		}
		emailParts[0] = strings.ReplaceAll(emailParts[0], ".", "")
		if domainToLocal[emailParts[1]] == nil {
			domainToLocal[emailParts[1]] = map[string]struct{}{}
		}
		domainToLocal[emailParts[1]][emailParts[0]] = struct{}{}
	}
	for domain := range domainToLocal {
		cnt += len(domainToLocal[domain])
	}
	return cnt
}

func ParseAcceptLanguage(reqHeaders string, acceptedHeaders []string) []string {
	reqHeaders = strings.ReplaceAll(reqHeaders, " ", "")
	reqHeadList := strings.Split(reqHeaders, ",")

	langToAcceptHeaderMap := map[string][]string{}
	acceptHeaderSet := map[string]bool{}
	for _, ah := range acceptedHeaders {
		ahGroup := strings.Split(ah, "-")
		langToAcceptHeaderMap[ahGroup[0]] = append(langToAcceptHeaderMap[ahGroup[0]], ah)
		acceptHeaderSet[ah] = true
	}

	retSet := map[string]bool{}
	for _, rh := range reqHeadList {
		if acceptHeaderSet[rh] {
			retSet[rh] = true
		} else if len(langToAcceptHeaderMap[rh]) > 0 {
			for _, ah := range langToAcceptHeaderMap[rh] {
				retSet[ah] = true
			}
		} else if strings.Index(rh, "*") >= 0 {
			rhPattern := strings.ReplaceAll(rh, "*", ".*")
			n := len(rhPattern)
			if rhPattern[0] != '.' {
				rhPattern = "^" + rhPattern
			}
			if rhPattern[n-1] != '*' {
				rhPattern += "$"
			}

			for _, ah := range acceptedHeaders {
				if !retSet[ah] {
					isMatch, _ := regexp.MatchString(rhPattern, ah)
					if isMatch {
						retSet[ah] = true
					}
				}
			}
		}
	}

	retList := make([]string, 0, len(retSet))
	for _, ah := range acceptedHeaders {
		if retSet[ah] {
			retList = append(retList, ah)
		}
	}
	return retList
}

func NextServerNumber(serverIds []int) int {
	if len(serverIds) == 0 {
		return 1
	}

	serverSet := map[int]bool{}
	maxId := -1 << 31
	for _, sId := range serverIds {
		serverSet[sId] = true
		maxId = mathext.MaxInt(maxId, sId)
	}
	for i := 1; i <= maxId; i++ {
		if !serverSet[i] {
			return i
		}
	}
	return maxId + 1
}

type DbRow map[string]int

func (r DbRow) Less(r2 DbRow, col string) bool {
	return r[col] < r2[col]
}
func (r DbRow) Greater(r2 DbRow, col string) bool {
	return !r.Less(r2, col)
}
func GetComparator(col, order string) func(r1, r2 DbRow) int {
	return func(r1, r2 DbRow) int {
		if r1[col] == r2[col] {
			return 0
		}
		if (order == "asc" && r1.Less(r2, col)) || (order == "desc" && r1.Greater(r2, col)) {
			return -1
		}
		return 1
	}
}

func MinByColumnOrderComparator(table []map[string]int, col, order string) map[string]int {
	if len(table) == 0 {
		return nil
	}

	returnRow := table[0]
	for i := 1; i < len(table); i++ {
		row := table[i]
		compareFunc := GetComparator(col, order)
		if compareFunc(row, returnRow) == -1 {
			returnRow = row
		}
	}
	return returnRow
}

func MinByColumnsOrderedComparator(table []map[string]int, cols, orders []string) map[string]int {
	if len(table) == 0 {
		return nil
	}

	returnRow := table[0]
	for i := 1; i < len(table); i++ {
		row := table[i]
		for j := range cols {
			col, order := cols[j], orders[j]
			comparator := GetComparator(col, order)
			compareResult := comparator(row, returnRow)
			if compareResult == 0 {
				continue
			}
			if compareResult == 1 {
				break
			}
			returnRow = row
			break
		}
	}
	return returnRow
}

func MinByColumnOrder(table []map[string]int, col, order string) map[string]int {
	if len(table) == 0 {
		return nil
	}

	returnRow := table[0]
	for i := 1; i < len(table); i++ {
		row := table[i]
		if order == "asc" && DbRow(row).Less(returnRow, col) {
			returnRow = row
		}
		if order == "desc" && DbRow(row).Greater(returnRow, col) {
			returnRow = row
		}
	}
	return returnRow
}

func MinByColumns(table []map[string]int, columns []string) map[string]int {
	minRow := table[0]
	for i := 1; i < len(table); i++ {
		row := table[i]
		for _, col := range columns {
			if minRow[col] == row[col] {
				continue
			}
			if row[col] < minRow[col] {
				minRow = row
				break
			}
		}
	}
	return minRow
}

func MinByColumns2(table []map[string]int, columns []string) map[string]int {
	sort.Slice(table, func(i, j int) bool {
		for _, col := range columns {
			if table[i][col] == table[j][col] {
				continue
			} else if table[i][col] < table[j][col] {
				return true
			} else {
				return false
			}
		}
		return false
	})
	return table[0]
}

func MinByColumns3(table []map[string]int, columns []string) map[string]int {
	keysort.Sort(table, func(i int) keysort.Sortable {
		e := table[i]
		keys := make([]interface{}, len(columns))
		for j := range columns {
			keys[j] = e[columns[j]]
		}
		return keysort.Sequence(keys)
	})
	return table[0]
}

// TODO
// tStr := `["CHARGE:card_country=US&currency=USD&amount=250&ip_country=CA","ALLOW:amount>100ANDamount<250","BLOCK:currency=EUR"]`
func IsTransactionAllowed(transactionStr string) (isAllowed bool) {
	chargeRegex := regexp.MustCompile("CHARGE:([\\w+&=]+)")
	// idx - 0:full-match, 1:everything upto next "
	chargeList := chargeRegex.FindStringSubmatch(transactionStr)
	chargeParamsList := strings.Split(chargeList[1], "&")
	paramsMap := map[string]string{}
	for _, paramStr := range chargeParamsList {
		eqIdx := strings.Index(paramStr, "=")
		if eqIdx > 0 {
			paramsMap[paramStr[:eqIdx]] = paramStr[eqIdx+1:]
		}
	}

	allowRegex := regexp.MustCompile("ALLOW:(\\w+)([<>=]+)(\\d+|\\w+)(AND|OR)?(\\w+)?([<>=]+)?(\\d+|\\w+)?")
	// idx - 0:full-match, 1:param, 2:op, 3:val, (optional)4:AND|OR, (optional)5:param, (optional)6:op, (optional)7:val
	allowList := allowRegex.FindStringSubmatch(transactionStr)

	if len(allowList) > 0 {

	}

	fmtext.PrintSyn(paramsMap)
	fmtext.PrintSyn(allowList)
	return isAllowed
}

func evalParam(paramsMap map[string]string, param, op, val string) bool {
	if strext.IsNumeric(val[0]) {
		return evalParamInt(paramsMap, param, op, val)
	}
	return false
}

func evalParamInt(paramsMap map[string]string, param, op, val string) bool {
	return false
}

func FindMaxLength(nums []int) (maxLen int) {

	return maxLen
}

/*func MaximumSwap(num int) int {
	numStr := strconv.Itoa(num)
	numMap := map[int]int{}
	for i := range numStr {
		digit, _ := strconv.Atoi(string(numStr[i]))
		numMap[i] = digit
	}
	for i := range numStr {
		for d := 9; d > numMap[i]; d-- {
			if val, ok := numMap[d]; ok && val > i {
				numMap[i], numMap[]
			}
		}
	}
}*/

func FizzBuzz(n int) {
	for i := 1; i <= n; i++ {
		result := ""
		if i%3 == 0 {
			result += "Fizz"
		}
		if i%5 == 0 {
			result += "Buzz"
		}
		if result == "" {
			result = strconv.Itoa(i)
		}
		fmt.Println(result)
	}
}

func CountPrimes(n int) int {
	isPrime := make([]bool, n)
	for i := 2; i < n; i++ {
		isPrime[i] = true
	}

	for i := 2; i*i < n; i++ {
		if !isPrime[i] {
			continue
		}
		for j := i * i; j < n; j += i {
			isPrime[j] = false
		}
	}

	cnt := 0
	for i := 2; i < n; i++ {
		if isPrime[i] {
			cnt++
		}
	}
	return cnt
}

func RestoreIpAddresses(s string) (results []string) {
	var backtrack func(ipRanges []string, idx int)
	backtrack = func(ipRanges []string, idx int) {
		if len(ipRanges) == 4 {
			if idx == len(s) {
				results = append(results, strings.Join(ipRanges, "."))
			}
			return
		}

		for i := idx; i < mathext.MinInt(idx+3, len(s)); i++ {
			if s[idx] == '0' && i > idx {
				continue
			}
			num, _ := strconv.Atoi(s[idx : i+1])
			if 0 <= num && num <= 255 {
				fmt.Println(append(ipRanges, s[idx:i+1]))
				backtrack(append(ipRanges, s[idx:i+1]), i+1)
			}
		}
	}
	backtrack([]string{}, 0)
	return results
}

func MyPow(x float64, n int) float64 {
	if n < 0 {
		x = 1 / float64(n)
		n = -n
	}
	var ans float64 = 1
	var curr = x
	for i := n; i > 0; i /= 2 {
		if i%2 == 1 {
			ans = ans * curr
		}
		curr = curr * curr
	}
	return ans
}

func GenerateParenthesis(n int) []string {
	if n == 0 {
		return []string{}
	}
	if n == 1 {
		return []string{"()"}
	}

	que := []ParenInfo{{
		parenList: []byte{'('},
		openCnt:   1,
		closedCnt: 0,
	}}

	results := []string{}
	var pi ParenInfo
	for len(que) > 0 {
		pi, que = que[0], que[1:]
		if pi.openCnt == n {
			if pi.closedCnt == n {
				results = append(results, string(pi.parenList))
			} else {
				closed := pi
				closed.closedCnt++
				closed.parenList = getByteSliceCopy(pi.parenList)
				closed.parenList = append(closed.parenList, ')')
				que = append(que, closed)
			}
		} else if pi.openCnt == pi.closedCnt {
			open := pi
			open.openCnt++
			open.parenList = getByteSliceCopy(pi.parenList)
			open.parenList = append(open.parenList, '(')
			que = append(que, open)
		} else {
			open := pi
			open.openCnt++
			open.parenList = getByteSliceCopy(pi.parenList)
			open.parenList = append(open.parenList, '(')
			que = append(que, open)

			closed := pi
			closed.closedCnt++
			closed.parenList = getByteSliceCopy(pi.parenList)
			closed.parenList = append(closed.parenList, ')')
			que = append(que, closed)
		}
	}
	return results
}

func CombinationSum(candidates []int, target int) (results [][]int) {
	sort.Ints(candidates)
	var backtrack func(remaining, idx int, nums []int)
	backtrack = func(remaining, idx int, nums []int) {
		if remaining == 0 {
			results = append(results, getIntSliceCopy(nums))
			return
		} else if remaining < 0 {
			return
		}

		for ; idx < len(candidates); idx++ {
			if idx > 0 && nums[idx] == nums[idx-1] {
				continue
			}
			nums = append(nums, candidates[idx])
			backtrack(remaining-candidates[idx], idx, nums)
			nums = nums[:len(nums)-1]
		}
	}
	backtrack(target, 0, []int{})
	return results
}

func combinationSum2(nums []int, target int) (results [][]int) {
	n := len(nums)
	sort.Ints(nums)
	var traverse func(idx, remaining int, arr []int)
	traverse = func(idx, remaining int, arr []int) {
		if remaining == 0 {
			temp := make([]int, len(arr))
			copy(temp, arr)
			results = append(results, temp)
			return
		} else if idx >= n || remaining < 0 {
			return
		}

		for j := idx; j < n; {
			arr = append(arr, nums[j])
			traverse(j+1, remaining-nums[j], arr)
			arr = arr[:len(arr)-1]
			j++
			for j > 0 && j < n && nums[j] == nums[j-1] {
				j++
			}
		}
	}
	traverse(0, target, []int{})
	return results
}

func combine(n, k int) [][]int {
	results := [][]int{}
	var traverse func(num int, arr []int)
	traverse = func(num int, arr []int) {
		if len(arr) == k {
			temp := make([]int, k)
			copy(temp, arr)
			results = append(results, temp)
			return
		}

		for i := num; i <= n; i++ {
			arr = append(arr, i)
			traverse(i+1, arr)
			arr = arr[:len(arr)-1]
		}
	}
	traverse(1, []int{})
	return results
}

func CombinationSum2(candidates []int, target int) (results [][]int) {
	sort.Ints(candidates)
	var backtrack func(remaining, idx int, nums []int)
	backtrack = func(remaining, idx int, nums []int) {
		if remaining == 0 {
			results = append(results, getIntSliceCopy(nums))
			return
		} else if remaining < 0 {
			return
		}

		for ; idx < len(candidates); idx++ {
			if idx > 0 && nums[idx] == nums[idx-1] {
				continue
			}
			nums = append(nums, candidates[idx])
			backtrack(remaining-candidates[idx], idx+1, nums)
			nums = nums[:len(nums)-1]
		}
	}
	backtrack(target, 0, []int{})
	return results
}

func getIntSliceCopy(nums []int) []int {
	nums2 := make([]int, len(nums))
	copy(nums2, nums)
	return nums2
}

func getByteSliceCopy(b []byte) []byte {
	b2 := make([]byte, len(b))
	copy(b2, b)
	return b2
}

type ParenInfo struct {
	parenList          []byte
	openCnt, closedCnt int
}

func MaxSlidingWindow(nums []int, k int) []int {
	maxHeap := collection.IntWithIndexMaxHeap{}
	results := []int{}
	for i := 0; i < k; i++ {
		maxHeap.HeapPush(collection.IntWithIndex{Idx: i, Val: nums[i]})
	}
	results = append(results, maxHeap[0].Val)

	for i := k; i < len(nums); i++ {
		for maxHeap.Len() > 0 && i-maxHeap[0].Idx+1 > k {
			maxHeap.HeapPop()
		}
		maxHeap.HeapPush(collection.IntWithIndex{Idx: i, Val: nums[i]})
		results = append(results, maxHeap[0].Val)
	}
	return results
}

func IsValidSudoku(board [][]byte) bool {
	rows, cols, box := make([]map[byte]bool, len(board)), make([]map[byte]bool, len(board)), make([]map[byte]bool, len(board))
	for i := range board {
		for j := range board[i] {
			val := board[i][j]
			if val == '.' {
				continue
			}
			boxId := (i/3)*3 + j/3

			if rows[i] == nil {
				rows[i] = map[byte]bool{}
			}
			if cols[j] == nil {
				cols[j] = map[byte]bool{}
			}
			if box[boxId] == nil {
				box[boxId] = map[byte]bool{}
			}

			if rows[i][val] {
				return false
			}
			if cols[j][val] {
				return false
			}
			if box[boxId][val] {
				return false
			}

			rows[i][val] = true
			cols[j][val] = true
			box[boxId][val] = true
		}
	}
	return true
}

func IsAdmissibleOverpayment(prices []float64, notes []string, x float64) bool {
	var sum float64
	for i, price := range prices {
		sum += price - GetInStorePrice(price, notes[i])
	}
	return sum <= x
}

func GetInStorePrice(icPrice float64, note string) float64 {
	percentIdx := strings.Index(note, "%")
	if percentIdx == -1 {
		return icPrice
	}
	isHigher := strings.Index(note, "higher") != -1
	percentage, _ := strconv.ParseFloat(note[:percentIdx], 64)
	percentage /= 100
	icPrice *= 1 / percentage
	multiplier := 1 / percentage
	if isHigher {
		multiplier += 1
	} else {
		multiplier -= 1
	}
	return icPrice / multiplier
}

func GetSum(a int, b int) int {
	fmt.Printf("a: %d, %s | b: %d, %s \n", a, strconv.FormatInt(int64(a), 2), b, strconv.FormatInt(int64(b), 2))
	for b != 0 {
		a, b = a^b, (a&b)<<1
		fmt.Printf("a: %d, %s | b: %d, %s \n", a, strconv.FormatInt(int64(a), 2), b, strconv.FormatInt(int64(b), 2))
	}
	return a
}

func GetSum2(a int, b int) int {
	x, y := mathext.AbsInt(a), mathext.AbsInt(b)
	if x < y {
		return GetSum2(y, x)
	}
	sign := -1
	if a > 0 {
		sign = 1
	}
	if a*b >= 0 {
		for y > 0 {
			x, y = x^y, (x&y)<<1
		}
	} else {
		for y > 0 {
			x, y = x^y, ((^x)&y)<<1
		}
	}
	return x * sign
}

func ArrayChange(arr []int) (cnt int) {
	max := arr[0]
	for i := 1; i < len(arr); i++ {
		if arr[i] <= arr[i-1] {
			max++
			cnt += max - arr[i]
		} else {
			max = arr[i]
		}
	}
	return cnt
}

func IntervalIntersection(aList [][]int, bList [][]int) (results [][]int) {
	if len(aList) == 0 || len(bList) == 0 {
		return results
	}

	for i, j := 0, 0; i < len(aList) && j < len(bList); {
		lo := mathext.MaxInt(aList[i][0], bList[j][0])
		hi := mathext.MaxInt(aList[i][1], bList[j][1])
		if lo <= hi {
			results = append(results, []int{lo, hi})
		}

		if aList[i][1] < bList[j][1] {
			i++
		} else {
			j++
		}
	}
	return results
}

func MinIncrementForUnique(A []int) int {
	if len(A) <= 1 {
		return 0
	}
	sort.Ints(A)
	s, ans := A[0], 0
	for i := range A {
		ans += mathext.MaxInt(0, s-A[i])
		s = mathext.MaxInt(s+1, A[i]+1)
	}
	return ans
}

/*func Calculator(s string) int {
	stk := []string{}
	i := 0
	for i < len(s) {
		if s[i] != '/' && s[i] != '*' {
			stk = append(stk, string(s[i]))
			i++
		} else {
			num1, _ := strconv.Atoi(stk[len(stk)-1])
			stk = stk[:len(stk)-1]
			num2, _ := strconv.Atoi(string(s[i+1]))
			if s[i] == '*' {
				stk = append(stk, strconv.Itoa(num1*num2))
			}
			if s[i] == '/' {
				stk = append(stk, strconv.Itoa(num1/num2))
			}
			i += 2
		}
	}
	if len(stk) == 1 {
		parenList, _ := strconv.Atoi(stk[0])
		return parenList
	} else {
		i = 1
		expectedResult := 0
		for i < len(stk) {
			num1, _ := strconv.Atoi(stk[i-1])
			num2, _ := strconv.Atoi(stk[i+1])
			if stk[i] == "+" {
				expectedResult += num1 + num2
			}
			if stk[i] == "-" {
				expectedResult += num1 - num2
			}
			i += 2
		}
		return expectedResult
	}
}*/

func PairsGreaterThanZ(nums []int, z int) int {
	prevIdx := -1
	var result [][]int
	for i := range nums {
		hiIdx := len(nums) - 1
		if prevIdx != -1 {
			hiIdx = prevIdx - 1
		}
		leftIdx := -1
		if i+1 != hiIdx {
			leftIdx = BinarySearchLeftRange(nums, i+1, hiIdx, z-nums[i])
		}
		if leftIdx != -1 {
			for j := leftIdx; j <= hiIdx; j++ {
				result = append(result, []int{nums[i], nums[j]})
			}
		}
		if prevIdx != -1 {
			for j := prevIdx; j < len(nums); j++ {
				result = append(result, []int{nums[i], nums[j]})
			}
		}
		prevIdx = leftIdx
	}
	fmt.Println(result)
	return len(result)
}

func PairsGreaterThanZ2(nums []int, z int) (cnt int) {
	lo, hi := 0, len(nums)-1
	for lo < hi {
		if nums[lo]+nums[hi] >= z {
			cnt += hi - lo
			hi--
		} else {
			lo++
		}
	}
	return cnt
}

func BinarySearchLeftRange(nums []int, lo, hi, targ int) int {
	idx := -1
	for lo <= hi {
		mid := (lo + hi) / 2
		if nums[mid] == targ {
			return mid
		} else if nums[mid] < targ {
			lo = mid + 1
		} else {
			hi = mid - 1
			idx = mid
		}
	}
	return idx
}

func BoundedSquareSum(nums1, nums2 []int, lo, hi int) int {

	return -1
}

func IntersectionSizeTwo(intervals [][]int) int {
	sort.Slice(intervals, func(i, j int) bool {
		return intervals[i][1] <= intervals[j][1] && intervals[i][0] >= intervals[j][0]
	})

	ans, lo, hi := 0, -1, -1
	for _, iv := range intervals {
		if iv[0] <= lo {
			continue
		}
		if lo < iv[0] {
			ans++
			if hi != iv[1] {
				lo, hi = hi, iv[1]
			} else {
				lo, hi = iv[1]-1, iv[1]
			}
		}
		if iv[0] > hi {
			ans += 2
			lo, hi = iv[1]-1, iv[1]
		}
	}
	return ans
}

// TODO:
func FindLadders(beginWord string, endWord string, wordList []string) [][]string {

	return nil
}

func IsNumber(str string) bool {
	for i := range str {
		if str[i] == '+' || str[i] == '-' {
			if i > 0 {
				return false
			}
		} else if str[i] == 'e' || str[i] == 'E' {
			if !validateE(str, i) {
				return false
			}
		} else if str[i] == '.' {
			if !validateDecimal(str, i) {
				return false
			}
		} else {
			if !strext.IsNumeric(str[i]) {
				return false
			}
		}
	}
	return true
}

func validateE(str string, idx int) bool {
	prevIsNumerical := idx > 0 && strext.IsNumeric(str[idx-1])
	nextIsNumerical := idx < len(str)-1 && strext.IsNumeric(str[idx+1])
	if !prevIsNumerical && idx > 0 && str[idx-1] == '.' {
		prevIsNumerical = validateDecimal(str, idx-1)
	}
	if !nextIsNumerical && idx < len(str)-1 && str[idx+1] == '.' {
		nextIsNumerical = validateDecimal(str, idx+1)
	}
	return prevIsNumerical && nextIsNumerical
}

func validateDecimal(str string, idx int) bool {
	prevIsNumerical := idx > 0 && strext.IsNumeric(str[idx-1])
	nextIsNumerical := idx < len(str)-1 && strext.IsNumeric(str[idx+1])
	return prevIsNumerical || nextIsNumerical
}

func AlmostIncreasingSequence(nums []int) bool {
	prev, cnt := 0, 0
	for i := 1; i < len(nums); i++ {
		if nums[i] > prev {
			prev = i
		} else {
			if cnt == 1 {
				return false
			}
			if prev-1 >= 0 && nums[prev-1] < nums[i] {
				prev = i
			}
			cnt++
		}
	}
	return true
}

// TODO
func maxArithmeticLength(a []int, b []int) int {

	return -1
}

func LicenseKeyFormatting(S string, K int) string {
	b := make([]byte, 0, len(S))
	S = strings.ToUpper(strings.ReplaceAll(S, "-", ""))
	dashCnt := 0
	for i := len(S) - 1; i >= 0; i-- {
		if dashCnt == K {
			b = append(b, '-')
			dashCnt = 0
		}
		b = append(b, S[i])
		dashCnt++
	}
	for i, j := 0, len(b)-1; i < j; i, j = i+1, j-1 {
		b[i], b[j] = b[j], b[i]
	}
	return string(b)
}

func WordPattern(pattern string, s string) bool {
	patternMap := map[byte]int{}
	sMap := map[string]int{}
	sList := strings.Split(s, " ")

	if len(pattern) != len(sList) {
		return false
	}

	for i := 0; i < len(pattern); i++ {
		pIdx, okP := patternMap[pattern[i]]
		sIdx, okS := sMap[sList[i]]

		if okP != okS || (okP && okS && pIdx != sIdx) {
			return false
		} else if !okP && !okS {
			patternMap[pattern[i]] = i
			sMap[sList[i]] = i
		}
	}
	return true
}

func SummaryRanges(nums []int) []string {
	if len(nums) == 0 {
		return []string{}
	}
	if len(nums) == 1 {
		return []string{strconv.Itoa(nums[0])}
	}

	ranges := []string{}
	lo, hi := 0, 1
	for hi <= len(nums) {
		if hi == len(nums) || nums[hi] != nums[hi-1]+1 {
			if hi-1 == lo {
				ranges = append(ranges, strconv.Itoa(nums[lo]))
			} else {
				ranges = append(ranges, fmt.Sprintf("%d->%d", nums[lo], nums[hi-1]))
			}
			lo = hi
		}
		hi++
	}
	return ranges
}

func FullJustify(words []string, maxWidth int) (results []string) {
	currLine := [][]byte{}
	currLineWidth := 0

	var addToResults = func(line [][]byte) {
		resultLine := make([]byte, 0, maxWidth)
		for _, chunk := range currLine {
			resultLine = append(resultLine, chunk...)
		}
		results = append(results, string(resultLine))
	}

	for i := 0; i < len(words); {
		word := words[i]
		if currLineWidth == 0 {
			currLine = append(currLine, []byte(word))
			currLineWidth += len(word)
			i++
			continue
		}

		if currLineWidth+len(word)+1 <= maxWidth {
			currLine[len(currLine)-1] = append(currLine[len(currLine)-1], ' ')
			currLine = append(currLine, []byte(word))
			currLineWidth += len(word) + 1
			i++
		} else {
			for j := 0; currLineWidth < maxWidth; j++ {
				if j >= len(currLine)-1 {
					j = 0
				}
				currLine[j] = append(currLine[j], ' ')
				currLineWidth++
			}

			addToResults(currLine)
			currLine = [][]byte{}
			currLineWidth = 0
		}
	}

	if currLineWidth > 0 {
		n := len(currLine)
		currLine[n-1] = append(currLine[n-1], bytes.Repeat([]byte(" "), maxWidth-currLineWidth)...)
		addToResults(currLine)
	}

	return results
}

var solution = func(read4 func([]byte) int) func([]byte, int) int {
	buf4 := make([]byte, 4)
	size, pos := 0, 0

	// implement read below.
	return func(buf []byte, n int) int {
		cnt := 0
		for cnt < n {
			if pos == size {
				pos = 0
				size = read4(buf4)
				if size == 0 {
					return cnt
				}
			}
			buf[cnt] = buf4[pos]
			pos++
			cnt++
		}
		return cnt
	}
}

func AddBinary(a string, b string) string {
	if a == "0" {
		return b
	}
	if b == "0" {
		return a
	}

	if len(a) < len(b) {
		a = strings.Repeat("0", len(b)-len(a)) + a
	}
	if len(b) < len(a) {
		b = strings.Repeat("0", len(a)-len(b)) + b
	}

	res := make([]byte, 0, len(a)+1)
	carry := false
	for i := len(a) - 1; i >= 0; i-- {
		sum := 0
		if carry {
			sum++
		}
		if a[i] == '1' {
			sum++
		}
		if b[i] == '1' {
			sum++
		}
		switch sum {
		case 3:
			res = append(res, '1')
			carry = true
		case 2:
			res = append(res, '0')
			carry = true
		case 1:
			res = append(res, '1')
			carry = false
		default:
			res = append(res, '0')
			carry = false
		}
	}
	if carry {
		res = append(res, '1')
	}
	for i, j := 0, len(res)-1; i < j; i, j = i+1, j-1 {
		res[i], res[j] = res[j], res[i]
	}
	return string(res)
}

func NumberToWords(num int) string {
	if num == 0 {
		return "Zero"
	}

	digits := map[int]string{0: "Zero", 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}
	teens := map[int]string{10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen"}
	tens := map[int]string{20: "Twenty", 30: "Thirty", 40: "Forty", 50: "Fifty", 60: "Sixty", 70: "Seventy", 80: "Eighty", 90: "Ninety"}
	BILLION, MILLION, THOUSAND := 1000000000, 1000000, 1000

	var twoDigToStr = func(num int) string {
		if num < 20 {
			str := digits[num]
			if str == "" {
				str = teens[num]
			}
			return str
		}

		tensStr := tens[num/10*10]
		digitsStr := digits[num%10]
		if digitsStr != "Zero" && digitsStr != "" {
			tensStr += " " + digitsStr
		}
		return tensStr
	}

	var threeDigToStr = func(num int) string {
		hundredsStr := digits[num/100] + " Hundred"
		tensStr := twoDigToStr(num % 100)
		if tensStr != "" && tensStr != "Zero" {
			hundredsStr += " " + tensStr
		}
		return hundredsStr
	}

	var digToStr = func(num int) string {
		str := ""
		if num < 100 {
			str = twoDigToStr(num)
		} else {
			str = threeDigToStr(num)
		}
		return str
	}

	res := ""
	for num > 0 {
		switch {
		case num >= BILLION:
			res += fmt.Sprintf(" %s Billion", digToStr(num/BILLION))
			num %= BILLION
		case num >= MILLION:
			res += fmt.Sprintf(" %s Million", digToStr(num/MILLION))
			num %= MILLION
		case num >= THOUSAND:
			res += fmt.Sprintf(" %s Thousand", digToStr(num/THOUSAND))
			num %= THOUSAND
		default:
			res += " " + digToStr(num)
			num = 0
		}
	}
	return strings.TrimSpace(res)
}

type ParenthInfo struct {
	balance int
	str     string
}

func MinRemoveToMakeValid(s string) string {
	b := []byte(s)
	openParStk := []int{}

	for i, ch := range s {
		if ch == '(' {
			openParStk = append(openParStk, i)
		} else if ch == ')' {
			if len(openParStk) > 0 {
				openParStk = openParStk[:len(openParStk)-1]
			} else {
				b[i] = '-'
			}
		}
	}

	n := len(openParStk)
	var idx int
	for n > 0 {
		idx, openParStk = openParStk[n-1], openParStk[:n-1]
		b[idx] = '-'
		n = len(openParStk)
	}
	return strings.ReplaceAll(string(b), "-", "")
}

func IsAlienSorted(words []string, order string) bool {
	if len(words) == 1 {
		return true
	}
	orderDict := map[byte]int{}
	for i := range order {
		orderDict[order[i]] = i
	}
	for i := 1; i < len(words); i++ {
		if !isLess(words[i-1], words[i], orderDict) {
			return false
		}
	}
	return true
}

func isLess(w1, w2 string, orderDict map[byte]int) bool {
	for i := 0; i < len(w1) || i < len(w2); i++ {
		if i >= len(w2) {
			return false
		}
		if i >= len(w1) {
			return true
		}
		if w1[i] == w2[i] {
			continue
		}
		if orderDict[w1[i]] < orderDict[w2[i]] {
			return true
		}
		if orderDict[w1[i]] > orderDict[w2[i]] {
			return false
		}
	}
	return false
}

func LeastInterval(tasks []byte, n int) (time int) {
	taskCnt := make([]int, 26)
	for _, task := range tasks {
		taskCnt[task-'A']++
	}

	sort.Ints(taskCnt)
	maxFreq := taskCnt[25]
	idleTime := (maxFreq - 1) * n

	for i := 24; i >= 0 && taskCnt[i] > 0; i-- {
		idleTime -= mathext.MinInt(taskCnt[i], maxFreq-1)
	}

	return mathext.MaxInt(idleTime, 0) + len(tasks)
}

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

type TrafficDirection int

const (
	Horizontal TrafficDirection = iota
	Vertical
	LeftToDown
	RightToDown
	TopToRight
	TopToLeft
)

// TODO
func CanTraverse(matrix [][]int) bool {
	return false
}

func FindPairsSummingToK(a []int, m int, k int) int {
	cnt := 0
	numMap := map[int][]int{a[0]: {0}}

	lo, hi := 0, 1
	for hi < len(a) {
		if hi-lo+1 > m {
			numMap[a[lo]] = numMap[a[lo]][1:]
			if len(numMap[a[lo]]) == 0 {
				delete(numMap, a[lo])
			}
			lo++
		}

		if len(numMap[k-a[hi]]) > 0 {
			for _, idx := range numMap[k-a[hi]] {
				cnt += m / (hi - idx)
			}
		}
		numMap[a[hi]] = append(numMap[a[hi]], hi)
		hi++
	}
	return cnt
}

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

func LengthOfLongestSubstringWithoutDups(s string) (maxLen int) {
	charIdxMap := map[byte]int{}
	lo, hi := 0, 0
	for hi < len(s) {
		if idx, ok := charIdxMap[s[hi]]; ok {
			lo = mathext.MaxInt(lo, idx+1)
			charIdxMap[s[lo]] = lo
		}
		charIdxMap[s[hi]] = hi
		maxLen = mathext.MaxInt(hi - lo + 1)
		hi++
	}
	return maxLen
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

func NextPermutation2(A []int) []int {
	if len(A) <= 1 {
		return A
	}

	idx := -1
	for i := len(A) - 2; i >= 0; i-- {
		if A[i] < A[i+1] {
			idx = i
			break
		}
	}

	if idx == -1 {
		sort.Ints(A)
		return A
	}

	for i := idx + 1; i < len(A); i++ {
		if A[idx] <= A[i] && (i == len(A)-1 || A[idx] > A[i+1]) {
			A[idx], A[i] = A[i], A[idx]
			break
		}
	}

	for i, j := idx+1, len(A)-1; i < j; i, j = i+1, j-1 {
		A[i], A[j] = A[j], A[i]
	}

	return A
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

func SubarraySumEqualsK(nums []int, k int) (cnt int) {
	sumFreq := map[int]int{0: 1}
	sum := 0
	for _, num := range nums {
		sum += num
		if freq, ok := sumFreq[sum-k]; ok {
			cnt += freq
		}
		sumFreq[sum] += 1
	}
	return cnt
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

func Divide(dividend int, divisor int) (cnt int) {
	neg1, neg2 := false, false
	if dividend < 0 {
		neg1 = true
		dividend = -dividend
	}
	if divisor < 0 {
		neg2 = true
		divisor = -divisor
	}
	isNeg := neg1 != neg2

	for dividend >= divisor {
		shift := 0
		for (1<<(shift+1))*divisor <= dividend {
			shift++
		}
		cnt += 1 << shift
		dividend -= (1 << shift) * divisor
	}
	if isNeg {
		cnt = -cnt
	}
	return cnt
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

func MergeIntervals(intervals [][]int) [][]int {
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

func RotateMatrix(matrix [][]int) {
	n := len(matrix[0])
	for i := 0; i < (n+1)/2; i++ {
		for j := 0; j < n/2; j++ {
			botLeftRow, botLeftCol := n-1-j, i
			botRightRow, botRightCol := n-1-i, n-j-i
			topLeftRow, topLeftCol := i, j
			topRightRow, topRightCol := j, n-1-i

			temp := matrix[botLeftRow][botLeftCol]
			matrix[botLeftRow][botLeftCol] = matrix[botRightRow][botRightCol]
			matrix[botRightRow][botRightCol] = matrix[topRightRow][topRightCol]
			matrix[topRightRow][topRightCol] = matrix[topLeftRow][topLeftCol]
			matrix[topLeftRow][topLeftCol] = temp
		}
	}
}

func RotateMatrixRight(matrix [][]int) {
	n := len(matrix)
	for i := range matrix {
		for j := i; j < n; j++ {
			matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
		}
	}

	for i := range matrix {
		for j, k := 0, len(matrix[i])-1; j < k; j, k = j+1, k-1 {
			matrix[i][j], matrix[i][k] = matrix[i][k], matrix[i][j]
		}
	}
}

func RotateMatrixLeft(matrix [][]int) {
	n := len(matrix)
	for i := range matrix {
		for j := i; j < n; j++ {
			matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
		}
	}

	for i, j := 0, len(matrix)-1; i < j; i, j = i+1, j-1 {
		matrix[i], matrix[j] = matrix[j], matrix[i]
	}
}

func RotateMatrixNoDiagonals(matrix [][]int) {
	diag1 := make([]int, len(matrix))
	diag2 := make([]int, len(matrix))
	x1, y1, x2, y2 := 0, 0, 0, len(matrix)-1
	for i := range diag1 {
		diag1[i] = matrix[x1][y1]
		diag2[i] = matrix[x2][y2]
		x1++
		y1++
		x2++
		y2--
	}
	fmtext.PrintSlice(matrix)
	RotateMatrixRight(matrix)

	x1, y1, x2, y2 = 0, 0, 0, len(matrix)-1
	for i := range diag1 {
		matrix[x1][y1] = diag1[i]
		matrix[x2][y2] = diag2[i]
		x1++
		y1++
		x2++
		y2--
	}
	fmt.Println()
	fmtext.PrintSlice(matrix)
}

func RotateMatrixNoDiagonals2(matrix [][]int) {
	n := len(matrix[0])

	// Transpose: reverse across diagonal
	x1, y1, x2, y2 := 0, 0, 0, len(matrix)-1
	for i := 0; i < n; i++ {
		for j := i; j < n; j++ {
			if (i == x1 && j == y1) || (i == x2 && j == y2) {
				continue
			}
			matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
		}
		x1++
		y1++
		x2++
		y2--
	}

	// Reverse: reverse each row
	x1, y1, x2, y2 = 0, 0, 0, len(matrix)-1
	for i := 0; i < n; i++ {
		for j, k := 0, n-1; j < k; j, k = j+1, k-1 {
			if (i == x1 && j == y1) || (i == x2 && j == y2) || (i == x1 && k == y1) || (i == x2 && k == y2) {
				continue
			}
			matrix[i][j], matrix[i][k] = matrix[i][k], matrix[i][j]
		}
		x1++
		y1++
		x2++
		y2--
	}
}

/*func strStr(haystack string, needle string) int {
	if needle == "" {return 0}
	else if len(needle) > len(haystack) {return -1}
	p1, p2 := 0, 0
	for i := range haystack {


	}
	return -1
}*/

type BeautyMatrix struct {
	matrix    [][]int
	n, beauty int
}

func NewBeautyMatrix(n int) BeautyMatrix {
	matrix := make([][]int, 0, n)
	return BeautyMatrix{matrix: matrix, n: n}
}

func BeautyOfAMatrix(matrix [][]int, k int) [][]int {
	nk := len(matrix) / k
	bmList := make([]BeautyMatrix, 0, len(matrix))

	for i := 0; i < nk; i++ {
		for j := 0; j < nk; j++ {
			bm := NewBeautyMatrix(nk)
			digits := make([]int, nk*nk+1)

			r, c := i*nk, j*nk
			for l := 0; l < nk; l++ {
				bm.matrix = append(bm.matrix, matrix[r][c:c+nk])
				for _, num := range bm.matrix[len(bm.matrix)-1] {
					digits[num-1]++
				}
				r++
			}
			for i := range digits {
				if digits[i] == 0 {
					bm.beauty = i + 1
					break
				}
			}
			bmList = append(bmList, bm)
		}
	}

	sort.SliceStable(bmList, func(i, j int) bool {
		return bmList[i].beauty < bmList[j].beauty
	})

	retMatrix := make([][]int, len(matrix))

	for i := range bmList {
		idx := (i / k) * nk
		for j := range bmList[i].matrix {
			retMatrix[idx] = append(retMatrix[idx], bmList[i].matrix[j]...)
			idx++
		}
	}
	return retMatrix
}

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

func MinCost(s string, cost []int) int {
	curSum, curMax, res := 0, 0, 0
	for i := 0; i < len(s); i++ {
		if i > 0 && s[i] != s[i-1] {
			res += curSum - curMax
			curSum, curMax = 0, 0
		}
		curSum += cost[i]
		curMax = mathext.MaxInt(curMax, cost[i])
	}
	return res + curSum - curMax
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
			cntrs[A[i]-1] = mathext.MaxInt(cntrs[A[i]-1]+1, globalMax+1)
			maxCntr = mathext.MaxInt(maxCntr, cntrs[A[i]-1])
		}
	}

	for i := range cntrs {
		if cntrs[i] < globalMax {
			cntrs[i] = globalMax
		}
	}
	return cntrs
}

func SortedSquaredArray(array []int) []int {
	idxPos := 0
	for idxPos < len(array) && array[idxPos] < 0 {
		idxPos++
	}

	res := make([]int, 0, len(array))
	idxNeg := idxPos - 1
	for idxNeg >= 0 || idxPos < len(array) {
		if idxNeg < 0 {
			res = append(res, array[idxPos]*array[idxPos])
			idxPos++
		} else if idxPos >= len(array) {
			res = append(res, array[idxNeg]*array[idxNeg])
			idxNeg--
		} else {
			if mathext.AbsInt(array[idxNeg]) < mathext.AbsInt(array[idxPos]) {
				res = append(res, array[idxNeg]*array[idxNeg])
				idxNeg--
			} else {
				res = append(res, array[idxPos]*array[idxPos])
				idxPos++
			}
		}
	}
	return res
}

func MaxTripletProduct(A []int) int {
	sort.Ints(A)
	n := len(A)
	mp1 := A[n-1] * A[n-2] * A[n-3]
	mp2 := A[0] * A[1] * A[n-1]
	return mathext.MaxInt(mp1, mp2)
}

func DiskIntersection(disks []int) (intersections int) {
	return
}

func TriangleExists(points []int) (exists bool) {
	sort.Ints(points)
	for i := 0; i < len(points)-2; i++ {
		if points[i]+points[i+1] > points[i+2] &&
			points[i]+points[i+2] > points[i+1] &&
			points[i+1]+points[i+2] > points[i] {
			return true
		}
	}
	return false
}

func GenerateDocument(characters string, document string) bool {
	freqC, freqD := map[byte]int{}, map[byte]int{}
	for i := 0; i < len(characters) || i < len(document); i++ {
		if i < len(characters) && characters[i] != ' ' {
			freqC[characters[i]] += 1
		}
		if i < len(document) && document[i] != ' ' {
			freqD[document[i]] += 1
		}
	}

	if len(freqC) < len(freqD) {
		return false
	}
	for char, cnt := range freqD {
		if cnt >= freqC[char] {
			return false
		}
	}

	return true
}

func ValidStartingCity(distances []int, fuel []int, mpg int) int {
	minIdx, minGas := 0, 0
	gas := 0
	for i := range distances {
		if i == 0 {
			continue
		}
		gas += fuel[i-1]*mpg - distances[i-1]
		if gas < minGas {
			minIdx, minGas = i, gas
		}
	}
	return minIdx
}

func ReverseWordsInString(str string) string {
	sb := strings.Builder{}
	sb.Grow(len(str))
	for lo, hi := len(str)-1, len(str)-1; lo >= -1; lo-- {
		if lo == -1 || str[lo] == ' ' {
			if str[lo+1] != ' ' {
				sb.WriteString(str[lo+1 : hi+1])
			}
			if lo != -1 {
				sb.WriteByte(' ')
			}
			hi = lo - 1
		}
	}
	return sb.String()
}

func FindMinMissingNumber(A []int) int {
	i := 0
	for i < len(A) {
		if A[i] >= 1 && A[i] <= len(A) && A[i] != i+1 {
			A[i], A[A[i]-1] = A[A[i]-1], A[i]
		} else {
			i++
		}
	}

	for i, num := range A {
		if i+1 != num {
			return i + 1
		}
	}
	return len(A) + 1
}

func GlobMatching(fileName, pattern string) bool {
	if pattern == "*" || len(fileName) == 1 && pattern == "?" {
		return true
	}

	wildCards := map[byte]bool{'*': true, '?': true}
	fileIdx := 0
	for patternIdx := 0; patternIdx < len(pattern); {
		if !wildCards[pattern[patternIdx]] {
			if fileName[fileIdx] != pattern[patternIdx] {
				return false
			}
			fileIdx++
			patternIdx++
		} else {
			if pattern[patternIdx] == '?' {
				if fileIdx == len(fileName) {
					return false
				}
				fileIdx++
				patternIdx++
			} else {
				for patternIdx < len(pattern) && wildCards[pattern[patternIdx]] {
					patternIdx++
				}
				if patternIdx == len(pattern) {
					return true
				}

				for fileIdx < len(fileName) && fileName[fileIdx] != pattern[patternIdx] {
					fileIdx++
				}
				if fileIdx == len(fileName) {
					patternIdx++
					for patternIdx < len(pattern) && pattern[patternIdx] == '*' {
						patternIdx++
					}
					if patternIdx == len(pattern) {
						return true
					}
					return false
				} else {
					patternIdx++
					fileIdx++
				}
			}
		}
	}
	if fileIdx < len(fileName) {
		return false
	}
	return true
}

func MinDeletions(S string, C []int) (minCost int) {
	if len(S) <= 1 {
		return 0
	}
	stk := []int{0}
	for i := 1; i < len(S); i++ {
		if S[i] == S[stk[len(stk)-1]] {
			if C[i] < C[stk[len(stk)-1]] {
				minCost += C[i]
			} else {
				minCost += C[stk[len(stk)-1]]
				stk = stk[:len(stk)-1]
				stk = append(stk, i)
			}
		} else {
			stk = append(stk, i)
		}
	}
	return minCost
}

func TestGroupScores(T, R []string) (score int) {
	testGroupIdx := 0
	for testGroupIdx < len(T) && strext.IsAlpha(T[0][testGroupIdx]) {
		testGroupIdx++
	}

	statusMap := map[string]bool{}
	for i, test := range T {
		testGroup := test[:testGroupIdx]
		numIdxStart, numIdxEnd := testGroupIdx, testGroupIdx
		for numIdxEnd < len(test) && strext.IsNumeric(test[numIdxEnd]) {
			numIdxEnd++
		}
		testGroup += test[numIdxStart:numIdxEnd]
		if status, ok := statusMap[testGroup]; ok && !status {
			continue
		}
		status := R[i] == "ok"
		statusMap[testGroup] = status
	}
	fmt.Println(statusMap)

	passCnt := 0
	for _, status := range statusMap {
		if status {
			passCnt++
		}
	}
	s1, s2 := passCnt*100/len(statusMap), passCnt*(100/len(statusMap))
	fmt.Println(s1, s2, float32(passCnt)/float32(len(statusMap))*100)
	return s2
}

func FindBinarySearchShiftedIdx(words []string) int {
	lo, hi := 0, len(words)-1
	for lo < hi {
		mid := (lo + hi) / 2
		if words[mid] >= words[lo] {
			lo = mid
		} else {
			hi = mid
		}

		if lo+1 == hi {
			return hi
		}
	}
	return -1
}

// TODO: Come back to
func MultiplyMatrices(mat1 [][]int, mat2 [][]int) [][]int {
	result := make([][]int, len(mat1))
	return result
}

func MinDeletionCostNoRepeatedLetter(s string, cost []int) (minCost int) {
	if len(s) <= 1 {
		return 0
	}
	stk := []int{0}
	for i := 1; i < len(s); i++ {
		n := len(stk)
		if s[i] != s[stk[n-1]] {
			stk = append(stk, i)
		} else {
			if cost[i] <= cost[stk[n-1]] {
				minCost += cost[i]
			} else {
				minCost += cost[stk[n-1]]
				stk = stk[:n-1]
				stk = append(stk, i)
			}
		}
	}
	return minCost
}

func IsValidParenthesis(s string) bool {
	stk := []byte{}
	brackets := map[byte]byte{')': '(', ']': '[', '}': '{'}
	for i := range s {
		if brackets[s[i]] != 0 {
			n := len(stk)
			if stk[n-1] != brackets[s[i]] {
				return false
			}
			stk = stk[:n-1]
		} else {
			stk = append(stk, s[i])
		}
	}
	return len(stk) == 0
}

func NumIslands(grid [][]byte) (cnt int) {
	visited, que := map[int]bool{}, []int{}
	rows, cols := len(grid), len(grid[0])
	directions := [][]int{{0, 1}, {0, -1}, {1, 0}, {-1, 0}}
	var point int

	for i := 0; i < rows; i++ {
		for j := 0; j < cols; j++ {
			if grid[i][j] == '1' && !visited[i*cols+j] {
				cnt++
				que = append(que, i*cols+j)
				for len(que) > 0 {
					point, que = que[0], que[1:]
					r, c := point/cols, point%cols
					for _, dir := range directions {
						newR, newC := r+dir[0], c+dir[1]
						if newR >= 0 && newC >= 0 && newR < rows && newC < cols &&
							grid[newR][newC] == '1' && !visited[newR*cols+newC] {
							que = append(que, newR*cols+newC)
							visited[newR*cols+newC] = true
						}
					}
				}
			}
		}
	}
	return cnt
}

type CharFreq struct {
	char byte
	freq int
}
type CharFreqMaxHeap []CharFreq

func (cfh CharFreqMaxHeap) Len() int              { return len(cfh) }
func (cfh CharFreqMaxHeap) Less(i, j int) bool    { return cfh[i].freq > cfh[j].freq }
func (cfh CharFreqMaxHeap) Swap(i, j int)         { cfh[i], cfh[j] = cfh[j], cfh[i] }
func (cfh *CharFreqMaxHeap) Push(val interface{}) { *cfh = append(*cfh, val.(CharFreq)) }
func (cfh *CharFreqMaxHeap) Pop() interface{} {
	n := cfh.Len()
	item := (*cfh)[n-1]
	*cfh = (*cfh)[:n-1]
	return item
}
func (cfh *CharFreqMaxHeap) Heapify() {
	heap.Init(cfh)
}
func (cfh *CharFreqMaxHeap) HeapPush(val CharFreq) {
	heap.Push(cfh, val)
}
func (cfh *CharFreqMaxHeap) HeapPop() CharFreq {
	return (heap.Pop(cfh)).(CharFreq)
}

func ReOrganizeString(str string) (reOrgStr string) {
	reOrgBytes := []byte{}
	charFreqMap := map[byte]int{}
	for i := range str {
		charFreqMap[str[i]] += 1
	}
	maxHeap := CharFreqMaxHeap{}
	for char := range charFreqMap {
		maxHeap.HeapPush(CharFreq{
			char: char,
			freq: charFreqMap[char],
		})
	}

	for len(maxHeap) > 1 {
		c1, c2 := maxHeap.HeapPop(), maxHeap.HeapPop()
		bLen := len(reOrgBytes)
		if bLen == 0 || c1.char != reOrgBytes[bLen-1] {
			reOrgBytes = append(reOrgBytes, c1.char)
			c1.freq--
		} else if bLen == 0 || c2.char != reOrgBytes[bLen-1] {
			reOrgBytes = append(reOrgBytes, c2.char)
			c2.freq--
		} else {
			return ""
		}
		if c1.freq > 0 {
			maxHeap.HeapPush(c1)
		}
		if c2.freq > 0 {
			maxHeap.HeapPush(c2)
		}
	}

	if len(maxHeap) == 1 {
		bLen := len(reOrgBytes)
		if (bLen > 0 && maxHeap[0].char == reOrgBytes[bLen-1]) || maxHeap[0].freq > 1 {
			return ""
		}
		reOrgBytes = append(reOrgBytes, maxHeap[0].char)
	}
	return string(reOrgBytes)
}

func MaxSubArray(nums []int) int {
	if len(nums) == 0 {
		return 0
	}
	if len(nums) == 1 {
		return nums[0]
	}
	var idx int
	currSum, maxSum := 0, -1<<31-1
	for idx < len(nums) {
		currSum += nums[idx]
		maxSum = mathext.MaxInt(maxSum, currSum)
		idx++
		if currSum < 0 {
			currSum = 0
		}
	}
	return maxSum
}

func MaxBalloons(text string) (cnt int) {
	balloonMap := map[byte]int{'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}
	for i := range text {
		if _, ok := balloonMap[text[i]]; ok {
			balloonMap[text[i]] += 1
		}
	}

	minSingles, minDoubles := 1<<31-1, 1<<31-1
	for char := range balloonMap {
		if char == 'b' || char == 'a' || char == 'n' {
			minSingles = mathext.MinInt(minSingles, balloonMap[char])
		} else {
			minDoubles = mathext.MinInt(minDoubles, balloonMap[char])
		}
	}

	if minSingles == 0 || minDoubles < 2 {
		return 0
	} else if minDoubles <= 2*minSingles {
		return minDoubles / 2
	} else {
		return minSingles
	}
}

func SumZero(n int) []int {
	if n == 1 {
		return []int{0}
	}

	sum := 0
	result := make([]int, n)
	for i := 0; i < n; i++ {
		result[i] = i + 1
		sum += i + 1
	}
	sum -= result[n-1]
	result[n-1] = -sum
	return result
}

func FirstMissingPositive(nums []int) int {
	oneExists := false
	for i := range nums {
		if !oneExists && nums[i] == 1 {
			oneExists = true
		}
		if nums[i] <= 0 || nums[i] > len(nums)+1 {
			nums[i] = 1
		}
	}

	if !oneExists {
		return 1
	}

	for i := range nums {
		if mathext.AbsInt(nums[i])-1 < len(nums) && nums[mathext.AbsInt(nums[i])-1] > 0 {
			nums[mathext.AbsInt(nums[i])-1] = -nums[mathext.AbsInt(nums[i])-1]
		}
	}

	for i := range nums {
		if nums[i] > 0 {
			return i + 1
		}
	}
	return len(nums) + 1
}

func SearchMatrix(matrix [][]int, target int) bool {
	rows, cols := len(matrix), len(matrix[0])
	x, y := 0, cols-1
	for {
		if x < 0 || y < 0 || x >= rows || y >= cols {
			break
		}
		if target == matrix[x][y] {
			return true
		}

		if target < matrix[x][y] {
			y--
		} else if target > matrix[x][y] {
			x++
		}
	}
	return false
}

func CountAndSay(n int) string {
	if n == 0 {
		return "10"
	}
	nStr := strconv.FormatInt(int64(n), 10)
	res := ""
	lo, hi := 0, 1
	for hi < len(nStr) {
		if nStr[hi] != nStr[hi-1] || hi == len(nStr)-1 {
			if hi == len(nStr)-1 {
				hi++
			}
			res += fmt.Sprintf("%d%s", hi-lo, nStr[hi-1:hi])
			lo = hi
		}
		hi++
	}
	return res
}

func generateMatrix(A int) [][]int {
	arr := make([][]int, A)
	for i := range arr {
		arr[i] = make([]int, A)
	}
	topBound, botBound := 0, A-1
	leftBound, rightBound := 0, A-1
	x, y := 0, 0
	var dir Direction = Right

	for i := 1; i <= A*A; i++ {
		arr[x][y] = i
		if dir == Right {
			if y == rightBound {
				x++
				topBound++
				dir = Down
				continue
			}
			y++
		} else if dir == Down {
			if x == botBound {
				y--
				rightBound--
				dir = Left
				continue
			}
			x++
		} else if dir == Left {
			if y == leftBound {
				x--
				botBound--
				dir = Up
				continue
			}
			y--
		} else if dir == Up {
			if x == topBound {
				y++
				leftBound++
				dir = Right
				continue
			}
			x--
		}
	}
	return arr
}
