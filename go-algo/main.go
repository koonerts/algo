package main

import (
	"fmt"
	"go-algo/arr"
	"go-algo/jsonext"
	"go-algo/slice"
)

func main() {
	matrix := jsonext.StrToIntMatrix("[[1,2,3,1,2,3,1,2,3],[4,5,6,4,5,6,4,5,6],[7,8,10,7,9,10,8,9,10],[1,2,3,1,2,3,1,2,3],[4,5,7,4,6,7,5,6,7],[8,9,10,8,9,10,8,9,10],[1,2,4,1,3,4,2,3,4],[5,6,7,5,6,7,5,6,7],[8,9,10,8,9,10,8,9,10]]")
	retMatrix := arr.BeautyOfAMatrix(matrix, 3)
	slice.PrintSlice(retMatrix)
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
