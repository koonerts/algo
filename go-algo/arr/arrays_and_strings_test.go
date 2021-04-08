package arr


import (
	"fmt"
	"reflect"
	"testing"
)

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