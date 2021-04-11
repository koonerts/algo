package fmtext

import (
	"encoding/json"
	"fmt"
	"go-algo/ext/mathext"
	"strconv"
	"strings"
)


func PrintSyn(i ...interface{}) {
	fmt.Printf("%#v\n", i...)
}

func Describe(i interface{}) {
	fmt.Printf("(%v, %T)\n", i, i)
}

func PrintSlice(iSlice interface{}) {
	strSlice := [][]string{}
	maxLen := 0
	switch slice := iSlice.(type) {
	case [][]bool:
		for _, value := range slice {
			strSl := []string{}
			for _, val := range value {
				str := strconv.FormatBool(val)
				maxLen = mathext.MaxInt(len(str), maxLen)
				strSl = append(strSl, str)
			}
			strSlice = append(strSlice, strSl)
		}
	case [][]string:
		for _, value := range slice {
			strSl := []string{}
			for _, val := range value {
				str := val
				maxLen = mathext.MaxInt(len(str), maxLen)
				strSl = append(strSl, str)
			}
			strSlice = append(strSlice, strSl)
		}
	case [][]int:
		for _, value := range slice {
			strSl := []string{}
			for _, val := range value {
				str := strconv.FormatInt(int64(val), 10)
				maxLen = mathext.MaxInt(len(str), maxLen)
				strSl = append(strSl, str)
			}
			strSlice = append(strSlice, strSl)
		}
	case [][]float64:
		for _, value := range slice {
			strSl := []string{}
			for _, val := range value {
				str := strconv.FormatFloat(val, 'E', -1, 64)
				maxLen = mathext.MaxInt(len(str), maxLen)
				strSl = append(strSl, str)
			}
			strSlice = append(strSlice, strSl)
		}
	case [][]byte:
		for _, value := range slice {
			strSl := []string{}
			for _, val := range value {
				str := string(val)
				maxLen = mathext.MaxInt(len(str), maxLen)
				strSl = append(strSl, str)
			}
			strSlice = append(strSlice, strSl)
		}
	case []bool:
		fmt.Println(slice)
	case []string:
		fmt.Println(slice)
	case []int:
		fmt.Println(slice)
	case []float64:
		fmt.Println(slice)
	case []byte:
		fmt.Println(slice)
	}

	if len(strSlice) > 0 {
		for i := range strSlice {
			for j := range strSlice[i] {
				if len(strSlice[i][j]) < maxLen {
					strSlice[i][j] = strings.Repeat(" ", maxLen - len(strSlice[i][j])) + strSlice[i][j]
				}
			}
		}

		for _, row := range strSlice {
			fmt.Printf("\t%v\n", row)
		}
	}
}

func PrettyPrint(v interface{}) (err error) {
	b, err := json.Marshal(v)
	//b, err := json.MarshalIndent(v, "", "  ")
	if err == nil {
		fmt.Println(string(b))
	}
	return
}

