package main

import (
	"fmt"
)

func main() {
	printLine(arr.MinRemoveToMakeValid("))(("))
}

func printLine(i ...interface{}) {
	fmt.Println(i...)
}

func printAsGoSyntax(i ...interface{}) {
	fmt.Printf("%#v\n", i...)
}

func describe(i interface{}) {
	fmt.Printf("(%v, %T)\n", i, i)
}
