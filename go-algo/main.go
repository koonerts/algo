package main

import (
	"fmt"
	"go-algo/dp"
)

func main() {
	print(dp.CakeThiefUnlimitedOpt([][]int{{7,160}, {3,90}, {2,15}}, 20))
}

func print(i ...interface{}) {
	fmt.Println(i...)
}

func printAsGoSyntax(i ...interface{}) {
	fmt.Printf("%#v\n", i...)
}