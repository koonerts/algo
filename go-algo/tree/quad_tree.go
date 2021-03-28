package tree

type QuadNode struct {
	Val         bool
	IsLeaf      bool
	TopLeft     *QuadNode
	TopRight    *QuadNode
	BottomLeft  *QuadNode
	BottomRight *QuadNode
}

func NewQuadTree(grid [][]int) *QuadNode {
	rows, cols := len(grid), len(grid[0])

	var constructRecursive func(xlo, xhi, ylo, yhi int) *QuadNode
	constructRecursive = func(xlo, xhi, ylo, yhi int) *QuadNode {
		if !(xlo >= 0 && ylo >= 0 && xhi < rows && yhi < cols) {return nil}

		isLeaf := true
		initVal := grid[xlo][ylo]
		for i := xlo; i <= xhi; i++ {
			for j := ylo; j <= yhi; j++ {
				if grid[i][j] != initVal {
					isLeaf = false
					break
				}
			}
		}

		var node *QuadNode
		if isLeaf {
			node = &QuadNode{Val:initVal==1, IsLeaf:true}
		} else {
			node = &QuadNode{Val:initVal==1, IsLeaf:false}
			xmid, ymid := (xhi+xlo)/2, (yhi+ylo)/2
			node.TopLeft = constructRecursive(xlo, xmid, ylo, ymid)
			node.BottomLeft = constructRecursive(xmid+1, xhi, ylo, ymid)
			node.TopRight = constructRecursive(xlo, xmid, ymid+1, yhi)
			node.BottomRight = constructRecursive(xmid+1, xhi, ymid+1, yhi)
		}
		return node
	}
	return constructRecursive(0, len(grid)-1, 0, len(grid[0])-1)
}
