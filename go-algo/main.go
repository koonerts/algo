package main

import (
	"fmt"
	"go-algo/arr"
)

func main() {
	print(arr.TestGroupScores([]string{"test1", "test2", "test3", "test4", "test5", "test10"}, []string{"ok", "ok", "fail", "ok", "ok", "fail"}))
}

func print(i ...interface{}) {
	fmt.Println(i...)
}
