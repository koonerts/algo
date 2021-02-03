package main

import (
	"encoding/json"
	"fmt"
)

func main() {
	fmt.Println(MinCoinChainUnlimited([]int{ 1, 2, 3 }, 5))
}


func PrettyPrint(v interface{}) (err error) {
	b, err := json.MarshalIndent(v, "", "  ")
	if err == nil {
		fmt.Println(string(b))
	}
	return
}
