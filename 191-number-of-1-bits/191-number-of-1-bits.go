func hammingWeight(num uint32) int {
    
    bits := 0
    for num > 0 {
        num = num & (num-1)
        bits++
    }
    return bits
}