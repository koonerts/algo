package tree


type BSTIterator struct {
	stk []*TreeNode
	root, curr *TreeNode
}


func Constructor(root *TreeNode) BSTIterator {
	return BSTIterator{[]*TreeNode{}, root, root}
}


func (bstIt *BSTIterator) Next() int {
	for bstIt.curr != nil {
		bstIt.stk = append(bstIt.stk, bstIt.curr)
		bstIt.curr = bstIt.curr.Left
	}
	n := len(bstIt.stk)
	bstIt.curr, bstIt.stk = bstIt.stk[n-1], bstIt.stk[:n-1]
	val := bstIt.curr.Val
	bstIt.curr = bstIt.curr.Right
	return val
}


func (bstIt *BSTIterator) HasNext() bool {
	return len(bstIt.stk) > 0 || bstIt.curr != nil
}