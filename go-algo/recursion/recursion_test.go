package recursion


import (
	"fmt"
	"sort"
	"testing"
)

func TestStringPermutations(t *testing.T) {
	var tests = []struct {
		in string
		out []string
	}{
		{"", []string{""}},
		{"a", []string{"a"}},
		{"ab", []string{"ab", "ba"}},
		{"abc", []string{"cba", "bca", "bac", "cab", "acb", "abc"}},
	}

	for _, tt := range tests {
		testName := fmt.Sprintf("%s", tt.in)
		t.Run(testName, func(t *testing.T) {
			ans := StringPermutations(tt.in)
			sort.Strings(ans)
			sort.Strings(tt.out)
			errored := false
			if len(ans) != len(tt.out) {
				errored = true
			} else {
				for i := range ans {
					if ans[i] != tt.out[i] {
						errored = true
						break
					}
				}
			}
			if errored {
				t.Errorf("got %#v, want %#v", ans, tt.out)
			}
		})
	}
}
