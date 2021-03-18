package main

import (
	"fmt"
)

func main() {

	fmt.Println('z'-'a', 'A')
}

func print(i ...interface{}) {
	fmt.Println(i...)
}
