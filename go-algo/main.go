package main

import (
	"fmt"
)

func main() {
	var b, b2 byte = '9', '9'+1
	fmt.Println(string(b), string(b2), b2)
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