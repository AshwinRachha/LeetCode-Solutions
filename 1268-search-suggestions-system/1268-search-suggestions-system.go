func suggestedProducts(products []string, searchWord string) [][]string {
    
    sort.Slice(products, func(i, j int) bool {
        return products[i] < products[j]
    })
    
    result := [][]string{}
    
    left := 0
    right := len(products) - 1
    
    for i:=0; i < len(searchWord); i++ {
        strs := []string{}
        c := searchWord[i]
        
        for left <= right && (len(products[left]) <= i || products[left][i] < c) {
            left++
        }
        for left <= right && (len(products[right]) <= i || products[right][i] > c) {
            right --
        }
        
        for j := 0; j < 3 && left + j <= right; j++ {
            strs = append(strs, products[left + j])
        }
        
        result = append(result, strs)
    }
    
    return result
    
}