package test

import (
	"strings"
	"testing"
)

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