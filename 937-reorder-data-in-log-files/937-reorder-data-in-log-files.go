func reorderLogFiles(logs []string) []string {
    
    if len(logs) < 2 {
        return logs
    }
    
    var sortedLetterLogs []string
    var sortedDigitLogs []string
    
    for _, log := range logs {
        i:= strings.Index(log, " ")
        if log[i+1] >= 'a' && log[i+1] <= 'z' {
            sortedLetterLogs = append(sortedLetterLogs, log)
        } else {
            sortedDigitLogs = append(sortedDigitLogs, log)
        }
    }
    
    sort.Slice(sortedLetterLogs, func (i, j int) bool {
        iIndex := strings.Index(sortedLetterLogs[i], " ")
        jIndex := strings.Index(sortedLetterLogs[j], " ")
        
        iLog := sortedLetterLogs[i][iIndex+1:]
        jLog := sortedLetterLogs[j][jIndex+1:]
        if iLog == jLog {
            return sortedLetterLogs[i] < sortedLetterLogs[j]
        }
        return iLog < jLog
    })
    
    sortedLetterLogs = append(sortedLetterLogs, sortedDigitLogs...)
    
    return sortedLetterLogs
    
}

