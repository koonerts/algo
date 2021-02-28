package main

import (
	"fmt"
	"go-algo/design"
	"go-algo/tree"
)

func main() {
	root := tree.CreateTreeNode([]int{1, 2, 3, -1 << 31, -1 << 31, 4, 5, -1 << 31, -1 << 31, -1 << 31, -1 << 31, 6, 7})
	codec := design.Constructor()
	jsonStr := codec.Serialize(root)
	root2 := codec.Deserialize(jsonStr)
	fmt.Println(root2)
}
