package dp

import "testing"

func BenchmarkLongestCommonSubsequenceMake(b *testing.B) {
	b.ReportAllocs()
	for i := 0; i < b.N; i++ {
		LongestCommonSubsequenceLength("kaphoigmxsphyhvoblhraefjxucpestsobiytgjmzwvtefgkhznoyqgnmzxicmnruklecsyzzyqjdwjlkwaltpiuqftkaqfitwtmhujrbdudtfnqzudnythb", "kaphoigmxsphyhvoblhraefjxucpestsobiytgjmhujrbdudtfnqzudnythb")
	}
}


func BenchmarkLongestCommonSubsequenceCopy(b *testing.B) {
	b.ReportAllocs()
	for i := 0; i < b.N; i++ {
		LongestCommonSubsequenceLength2("kaphoigmxsphyhvoblhraefjxucpestsobiytgjmzwvtefgkhznoyqgnmzxicmnruklecsyzzyqjdwjlkwaltpiuqftkaqfitwtmhujrbdudtfnqzudnythb", "kaphoigmxsphyhvoblhraefjxucpestsobiytgjmhujrbdudtfnqzudnythb")
	}
}