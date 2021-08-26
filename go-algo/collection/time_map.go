package collection

type TimeItem struct {
	key, val  string
	timestamp int
}

type TimeMap struct {
	cache map[string][]TimeItem
}

func NewTimeMap() TimeMap {
	return TimeMap{
		cache: map[string][]TimeItem{},
	}
}

func (tm *TimeMap) Set(key string, value string, timestamp int) {
	item := TimeItem{key, value, timestamp}
	if _, ok := tm.cache[key]; !ok {
		tm.cache[key] = []TimeItem{item}
	} else {
		tm.cache[key] = append(tm.cache[key], item)
	}
}

func (tm *TimeMap) Get(key string, timestamp int) string {
	if len(tm.cache[key]) == 0 {
		return ""
	}

	rVal := ""
	lo, hi := 0, len(tm.cache[key])-1
	for lo <= hi {
		mid := (lo + hi) / 2
		item := tm.cache[key][mid]
		if item.timestamp == timestamp {
			return item.val
		} else if item.timestamp < timestamp {
			rVal = item.val
			lo = mid + 1
		} else {
			hi = mid - 1
		}
	}

	return rVal
}
