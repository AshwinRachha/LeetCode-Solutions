import "fmt"
func carPooling(trips [][]int, capacity int) bool {
    
    arr := make([]int, 1001)
    for i := range(trips) {
        passangers, start, end := trips[i][0], trips[i][1], trips[i][2]
        arr[start] += passangers
        arr[end] -= passangers
    }
    used_cap := 0
    for i := 0; i < 1001; i++ {
        used_cap += arr[i]
        if used_cap > capacity {
            return false
        }
    }
    return true
}