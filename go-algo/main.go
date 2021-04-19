package main

import (
	"fmt"
	"go-algo/arr"
)

func main() {
	fmt.Println(arr.NumberToWords(5))
	fmt.Println(arr.NumberToWords(18))
	fmt.Println(arr.NumberToWords(21))
	fmt.Println(arr.NumberToWords(123))
	fmt.Println(arr.NumberToWords(12345))
	fmt.Println(arr.NumberToWords(1234567))
	fmt.Println(arr.NumberToWords(1234567891))
}

