package main

import (
	"encoding/json"
	"fmt"
)

func main() {
	fmt.Println(RodCuttingProfit([]int{ 1, 2, 3, 4, 5 }, []int{2,6,7,10,13}, 5))
}


func PrettyPrint(v interface{}) (err error) {
	b, err := json.MarshalIndent(v, "", "  ")
	if err == nil {
		fmt.Println(string(b))
	}
	return
}
