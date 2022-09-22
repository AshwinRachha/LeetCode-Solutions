import "fmt"
func reverseWords(s string) string {
   bs := []byte(s)
	left := 0
	for i, b := range bs {
		if b == ' ' {
			reverse(&bs, left, i-1)
			left = i + 1
		}
	}
	reverse(&bs, left, len(bs)-1)
	return string(bs)
}

func reverse(src *[]byte, start int, end int) {
    for start < end {
        (*src)[start], (*src)[end] = (*src)[end], (*src)[start]
        start++
        end--
    }
}