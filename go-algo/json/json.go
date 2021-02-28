package json

import (
	"encoding/json"
	"fmt"
)

type MatrixHelper struct {
	IntMatrix [][]int
	StringMatrix [][]string
}
func strToIntMatrix(str string) [][]int {
	bytes := []byte(`{"intMatrix":`)
	bytes = append(append(bytes, str...), `}`...)
	var v MatrixHelper
	_ = json.Unmarshal(bytes, &v)
	return v.IntMatrix
}
func strToStringMatrix(str string) [][]string {
	bytes := []byte(`{"stringMatrix":`)
	bytes = append(append(bytes, str...), `}`...)
	var v MatrixHelper
	_ = json.Unmarshal(bytes, &v)
	return v.StringMatrix
}

func PrettyPrint(v interface{}) (err error) {
	b, err := json.MarshalIndent(v, "", "  ")
	if err == nil {
		fmt.Println(string(b))
	}
	return
}