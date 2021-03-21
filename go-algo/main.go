package main

import (
	"fmt"
	"go-algo/arr"
)

func main() {
	print(arr.IsValidParenthesis("()"))
	print(arr.IsValidParenthesis("([)]"))
	print(arr.IsValidParenthesis("()[]{}"))
	print(arr.IsValidParenthesis("(]"))
	print(arr.IsValidParenthesis("{[]}"))
}

func print(i ...interface{}) {
	fmt.Println(i...)
}

func printAsGoSyntax(i ...interface{}) {
	fmt.Printf("%#v\n", i...)
}