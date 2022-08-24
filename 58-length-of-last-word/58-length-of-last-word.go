func lengthOfLastWord(s string) int {
	len := len(s)
	result := 0
	for i := len - 1; i >= 0; i-- {
		if s[i] != ' ' {
			result += 1
		} else if result > 0 {
			return result
		}
	}
	return result
}