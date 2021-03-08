package strext


func RemoveNonAlphaNumeric(bytes []byte) []byte {
	n := 0
	for i := range bytes {
		if (bytes[i] >= 'a' && bytes[i] <= 'z') ||
			(bytes[i] >= 'A' && bytes[i] <= 'Z') ||
			(bytes[i] >= '0' && bytes[i] <= '9') ||
			bytes[i] == ' ' {
			bytes[n] = bytes[i]
			n++
		} else if (bytes[i] == ',' || bytes[i] == '.') && i+1 < len(bytes) && bytes[i+1] != ' ' {
			bytes[n] = ' '
			n++
		}
	}
	return bytes[:n]
}