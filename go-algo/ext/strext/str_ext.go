package strext


func RemoveNonAlphaNumeric(bytes []byte) []byte {
	n := 0
	for i := range bytes {
		if IsAlphaNumeric(bytes[i]) || bytes[i] == ' ' {
			bytes[n] = bytes[i]
			n++
		} else if (bytes[i] == ',' || bytes[i] == '.') && i+1 < len(bytes) && bytes[i+1] != ' ' {
			bytes[n] = ' '
			n++
		}
	}
	return bytes[:n]
}

func IsAlpha(b byte) bool {
	return (b >= 'a' && b <= 'z') || (b >= 'A' && b <= 'Z')
}

func IsNumeric(b byte) bool {
	return b >= '0' && b <= '9'
}

func IsAlphaNumeric(b byte) bool {
	return IsAlpha(b) || IsNumeric(b)
}

