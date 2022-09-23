func concatenatedBinary(n int) int {
    length, res, mod := 0, 0, 1000000007
    
    for i:=1; i<=n; i++ {
        if i & (i-1) == 0 {
            length++
        }
        res = (res << length | i) % mod
    }
    return res
}