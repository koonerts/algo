package design


type TimedLogger struct {
	cache map[string]int
}


/** Initialize your data structure here. */
func NewTimedLogger() TimedLogger {
	return TimedLogger{map[string]int{}}
}


/** Returns true if the message should be printed in the given timestamp, otherwise returns false.
  If this method returns false, the message will not be printed.
  The timestamp is in seconds granularity. */
func (log *TimedLogger) ShouldPrintMessage(timestamp int, message string) bool {
	if prevTimestamp, ok := log.cache[message]; !ok || timestamp >= prevTimestamp+10 {
		log.cache[message] = timestamp
		return true
	}
	return false
}