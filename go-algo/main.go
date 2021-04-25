package main

import (
	"fmt"
	"go-algo/ext/jsonext"
	"sort"
)

func main() {
	fmt.Println(findItinerary(jsonext.StrToStringMatrix("[[\"EZE\",\"AXA\"],[\"TIA\",\"ANU\"],[\"ANU\",\"JFK\"],[\"JFK\",\"ANU\"],[\"ANU\",\"EZE\"],[\"TIA\",\"ANU\"],[\"AXA\",\"TIA\"],[\"TIA\",\"JFK\"],[\"ANU\",\"TIA\"],[\"JFK\",\"TIA\"]]\n")))
}


func findItinerary(tickets [][]string) []string {
	adjMap := map[string][]string{}
	remainingFlights := map[string]map[string]int{}
	for _, t := range tickets {
		if remainingFlights[t[0]] == nil {
			remainingFlights[t[0]] = map[string]int{}
		}
		remainingFlights[t[0]][t[1]] += 1
		adjMap[t[0]] = append(adjMap[t[0]], t[1])
	}

	edges := 0
	for sourceCity := range adjMap {
		sort.Strings(adjMap[sourceCity])
		edges += len(adjMap[sourceCity])
	}

	result := []string{}
	var dfs func(src string)
	dfs = func(src string) {
		result = append(result, src)
		if len(result) == edges+1 {
			return
		}

		for _, dest := range adjMap[src] {
			if remainingFlights[src][dest] > 0 {
				remainingFlights[src][dest] -= 1
				dfs(dest)
				if len(result) == edges + 1 {
					return
				}
				result = result[:len(result)-1]
				remainingFlights[src][dest] += 1
			}
		}
	}

	dfs("JFK")
	return result
}

