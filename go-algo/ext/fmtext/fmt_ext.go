package fmtext

import "fmt"


func PrintSyn(i ...interface{}) {
	fmt.Printf("%#v\n", i...)
}

func Describe(i interface{}) {
	fmt.Printf("(%v, %T)\n", i, i)
}
