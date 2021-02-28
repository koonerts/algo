package main

import (
	"fmt"
	_ "go-algo/collection"
	"go-algo/tree"
	_ "gopkg.in/karalabe/cookiejar.v2/collections/deque"
)


func main() {
	root := tree.CreateBinaryTree("{\"nodes\":[{\"id\":\"1\",\"left\":\"2\",\"right\":\"3\",\"value\":1},{\"id\":\"2\",\"left\":\"4\",\"right\":\"5\",\"value\":2},{\"id\":\"3\",\"left\":null,\"right\":\"6\",\"value\":3},{\"id\":\"4\",\"left\":null,\"right\":null,\"value\":4},{\"id\":\"5\",\"left\":\"7\",\"right\":\"8\",\"value\":5},{\"id\":\"6\",\"left\":null,\"right\":null,\"value\":6},{\"id\":\"7\",\"left\":null,\"right\":null,\"value\":7},{\"id\":\"8\",\"left\":null,\"right\":null,\"value\":8}],\"root\":\"1\"}")
	fmt.Println(tree.HeightBalancedBinaryTree(root))
}