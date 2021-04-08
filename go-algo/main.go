package main

import (
	"fmt"
	"go-algo/arr"
)

func main() {
	fmt.Println(arr.MinByColumns([]map[string]int{{"a": 1, "b": 2, "c": 3}, {"a": 10}}, []string{"a"}))
	fmt.Println(arr.MinByColumns([]map[string]int{{"a": 1, "b": 2, "c": 3}, {"a": 10}}, []string{"b"}))
	fmt.Println(arr.MinByColumns([]map[string]int{
		{"x": 1, "y": 2, "z": 3},
		{"x": 1, "y": 2, "z": 2},
		{"x": 1, "y": 2, "z": 4}},
		[]string{"x", "y", "z"}))
	fmt.Println(arr.MinByColumns2([]map[string]int{
		{"x": 1, "y": 2, "z": 3},
		{"x": 1, "y": 2, "z": 2},
		{"x": 1, "y": 2, "z": 4}},
		[]string{"x", "y", "z"}))
}
