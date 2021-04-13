package arr

import (
	"fmt"
	"math/rand"
	"reflect"
	"testing"
)

func BenchmarkMergeSort(b *testing.B) {
	x := make([]int, 1000000)
	for i := 0; i < len(x); i++ {
		x[i] = i
	}
	rand.Shuffle(len(x), func(i, j int) {x[i], x[j] = x[j], x[i]})
	b.ResetTimer()
	b.ReportAllocs()
	for i := 0; i < b.N; i++ {
		_ = MergeSort(x)
	}
}

func BenchmarkMergeSortConcurrent(b *testing.B) {
	x := make([]int, 1000000)
	for i := 0; i < len(x); i++ {
		x[i] = i
	}
	rand.Shuffle(len(x), func(i, j int) {x[i], x[j] = x[j], x[i]})
	b.ResetTimer()
	b.ReportAllocs()
	for i := 0; i < b.N; i++ {
		_ = MergeSortConcurrent(x)
	}
}

func TestShortestDistToStore(t *testing.T) {
	tests := []struct {
		houses, stores, expectedResult []int
	}{
		{[]int{5,10,17}, []int{1, 5, 20, 11, 16}, []int{5, 11, 16}},
		{[]int{2,4,2}, []int{5,1,2,3}, []int{2,3,2}},
		{[]int{4,8,1,1}, []int{5,3,1,2,6}, []int{3,6,1,1}},
	}

	for _, test := range tests {
		testName := fmt.Sprintf("Houses:%v\nStores:%v\n", test.houses, test.stores)
		t.Run(testName, func(t *testing.T) {
			ans := ShortestDistToStore(test.houses, test.stores)
			if !reflect.DeepEqual(ans, test.expectedResult) {
				t.Errorf("\nExpected:%v\nGot:%v", test.expectedResult, ans)
			}
		})
	}
}


func TestDbRowCompare(t *testing.T) {
	r1 := map[string]int{"a": 1, "b": 2, "c": 3}
	r2 := map[string]int{"a": 10}
	var tests = []struct {
		table []map[string]int
		col, order string
		result map[string]int
	}{
		{[]map[string]int{r1, r2}, "a", "asc", r1},
		{[]map[string]int{r1, r2}, "a", "desc", r2},
		{[]map[string]int{r1, r2}, "b", "asc", r2},
		{[]map[string]int{r1, r2}, "b", "desc", r1},
	}

	for _, tt := range tests {
		testName := fmt.Sprintf("%#v | %s | %s \n", tt.table, tt.col, tt.order)
		t.Run(testName, func(t *testing.T) {
			ans := MinByColumnOrderComparator(tt.table, tt.col, tt.order)
			if !reflect.DeepEqual(ans, tt.result) {
				t.Errorf("got %#v, want %#v", ans, tt.result)
			}
		})
	}
}


func TestParseAcceptLanguage(t *testing.T) {
	var tests = []struct {
		reqHeaders          string
		acceptedHeadersList []string
		expectedResult      []string
	}{
		{"en", []string{"en-US", "fr-CA", "fr-FR"}, []string{"en-US"}},
		{"fr", []string{"en-US", "fr-CA", "fr-FR"}, []string{"fr-CA", "fr-FR"}},
		{"fr-FR, fr, en", []string{"en-US", "fr-CA", "fr-FR", "en-CA"}, []string{"en-US", "fr-CA", "fr-FR", "en-CA"}},
		{"", []string{"en-US", "fr-CA", "fr-FR"}, []string{}},
		{"en-", []string{"en-US", "fr-CA", "fr-FR"}, []string{}},
		{"*CA*", []string{"en-CA", "en-US", "fr-CA", "fr-FR"}, []string{"en-CA", "fr-CA"}},
		{"CA*", []string{"en-CA", "en-US", "fr-CA", "fr-FR"}, []string{}},
	}

	for _, test := range tests {
		testName := fmt.Sprintf("(%s, %v)", test.reqHeaders, test.acceptedHeadersList)
		t.Run(testName, func(t *testing.T){
			ans := ParseAcceptLanguage(test.reqHeaders, test.acceptedHeadersList)
			if !reflect.DeepEqual(test.expectedResult, ans) {
				t.Errorf("Expected: %v\nGot: %v\n", test.expectedResult, ans)
			}
		})
	}
}