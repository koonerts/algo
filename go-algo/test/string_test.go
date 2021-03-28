package test

import (
	"github.com/google/uuid"
	"go-algo/mathext"
	"sort"
	"strings"
	"testing"
)

func BenchmarkLinearSearchString(b *testing.B) {
	uuids := make([]string, 1_000_000)
	for i := range uuids {
		uuids[i] = uuid.New().String()
	}
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		uuidStr := uuids[mathext.RandInt(0, 999_999)]
		for k := range uuids {
			if uuidStr == uuids[k] {
				break
			}
		}
	}
}

func BenchmarkBinarySearchString(b *testing.B) {
	uuids := make([]string, 1_000_000)
	for i := range uuids {
		uuids[i] = uuid.New().String()
	}
	b.ResetTimer()

	sort.Strings(uuids)
	for i := 0; i < b.N; i++ {
		uuidStr := uuids[mathext.RandInt(0, 999_999)]
		lo, hi := 0, len(uuids)-1
		for lo <= hi {
			mid := (lo + hi) / 2
			if uuids[mid] == uuidStr {
				break
			} else if uuids[mid] < uuidStr {
				lo = mid + 1
			} else {
				hi = mid - 1
			}
		}
	}
}

func BenchmarkStringBuilder(b *testing.B) {
	s := "abcde"
	s2 := "sdjsdbf"
	var bl strings.Builder
	for i := 0; i < b.N; i++ {
		bl.WriteString(s)
		bl.WriteString(s2)
	}
	_ = bl.String()
}

func BenchmarkStringByteSlice(b *testing.B) {
	s := "abcde"
	s2 := "sdjsdbf"
	var bslice []byte
	for i := 0; i < b.N; i++ {
		bslice = append(bslice, s...)
		bslice = append(bslice, s2...)
	}
	_ = string(bslice)
}

func BenchmarkStringConcat(b *testing.B) {
	s := "abcde"
	s2 := "sdjsdbf"
	var str string
	for i := 0; i < b.N; i++ {
		str += s
		str += s2
	}
}

func BenchmarkByteToStringUsingConversion(b *testing.B) {
	s := "abcde"
	for i := 0; i < b.N; i++ {
		_ = string(s[3])
	}
}

func BenchmarkByteToStringUsingSlice(b *testing.B) {
	s := "abcde"
	for i := 0; i < b.N; i++ {
		_ = s[3:4]
	}
}
