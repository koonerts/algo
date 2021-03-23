package jsonext

import (
	"encoding/json"
	"fmt"
	_ "github.com/tidwall/gjson"
)


type IntMatrix [][]int
type StringMatrix [][]string

func StrToIntMatrix(str string) [][]int {
	bytes := []byte(str)
	var v IntMatrix
	_ = json.Unmarshal(bytes, &v)
	return v
}

func StrToStringMatrix(str string) [][]string {
	bytes := []byte(str)
	var v StringMatrix
	_ = json.Unmarshal(bytes, &v)
	return v
}

func StrToByteMatrix(str string) [][]byte {
	strMatrix := StrToStringMatrix(str)
	byteMatrix := make([][]byte, len(strMatrix))
	for i := range byteMatrix {
		byteMatrix[i] = make([]byte, len(strMatrix[i]))
		for j := range byteMatrix[i] {
			byteMatrix[i][j] = strMatrix[i][j][0]
		}
	}
	return byteMatrix
}

func PrettyPrint(v interface{}) (err error) {
	b, err := json.MarshalIndent(v, "", "  ")
	if err == nil {
		fmt.Println(string(b))
	}
	return
}