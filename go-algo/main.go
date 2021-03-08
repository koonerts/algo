package main

import (
	"fmt"
	"go-algo/collection"
	"go-algo/tree"
)

func main() {
	uf := collection.NewUnionFind(5)
	for _, edge := range [][]int32{{2,1}, {5,3}, {5,1}, {3,4}, {3,1}, {5,4}, {4,1}, {5,2}, {4,2}} {
		uf.Union(edge[0], edge[1])
	}
	roots := uf.GetDistinctRoots()
	print(roots)
	print(uf.GetSize(roots[0]))
	print(uf)

	print(tree.RoadsAndLibraries(5, 92, 23, [][]int32{{2,1}, {5,3}, {5,1}, {3,4}, {3,1}, {5,4}, {4,1}, {5,2}, {4,2}}))
}


func print(i interface {}) {
	fmt.Println(i)
}
