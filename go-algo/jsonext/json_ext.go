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

func PrettyPrint(v interface{}) (err error) {
	b, err := json.MarshalIndent(v, "", "  ")
	if err == nil {
		fmt.Println(string(b))
	}
	return
}