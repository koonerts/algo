package main

import (
	"encoding/json"
	"fmt"
)

func main() {
	fmt.Println(CanPartitionEqualSubsets([]int{1, 1, 3, 4, 7}))
}


func PrettyPrint(v interface{}) (err error) {
	b, err := json.MarshalIndent(v, "", "  ")
	if err == nil {
		fmt.Println(string(b))
	}
	return
}
