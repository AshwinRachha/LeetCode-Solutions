func isSubsequence(s string, t string) bool {
    
    i, j := 0, 0
    
    for i != len(s) && j < len(t) {
        if s[i] == t[j] {
            i = i+1
            j = j+1
        } else {
            j = j + 1
        }
    }
    
    return i == len(s)
    
}