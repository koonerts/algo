package main

import (
	"fmt"
	"go-algo/dp"
)

func main() {
	printLine(arr.LicenseKeyFormatting("5F3Z-2e-9-w", 4))
	printLine(arr.LicenseKeyFormatting("2-5g-3-J", 2))
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