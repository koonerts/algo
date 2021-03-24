package main

import (
	"fmt"
	"go-algo/dp"
)

func main() {
	printLine(dp.DecodeWays("226"))
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