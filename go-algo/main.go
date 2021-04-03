package main

import (
	"fmt"
)

func main() {
	var x []int
	x = append(x, 1)
	fmt.Println(x)
}


func printLine(i ...interface{}) {
	fmt.Println(i...)
}

func printSyntax(i ...interface{}) {
	fmt.Printf("%#v\n", i...)
}

func describe(i interface{}) {
	fmt.Printf("(%v, %T)\n", i, i)
}
