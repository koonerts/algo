package collection

type UnionFind struct {
	roots, sizes []int
}

func NewUnionFind(size int) *UnionFind {
	r, s := make([]int, size+1), make([]int, size+1)
	for i := range r {
		r[i] = i
		s[i] = 1
	}
	r[0] = -1
	s[0] = -1
	return &UnionFind{r, s}
}

func (uf *UnionFind) Union(p, q int) {
	proot := uf.Find(p)
	qroot := uf.Find(q)
	if proot == qroot {
		return
	}

	if uf.sizes[proot] >= uf.sizes[qroot] {
		uf.roots[qroot] = proot
		uf.sizes[proot] += uf.sizes[qroot]
	} else {
		uf.roots[proot] = qroot
		uf.sizes[qroot] += uf.sizes[proot]
	}
}

func (uf *UnionFind) Find(p int) int {
	if p >= len(uf.roots) {
		return -1
	}

	for uf.roots[p] != p {
		uf.roots[p] = uf.roots[uf.roots[p]]
		p = uf.roots[p]
	}
	return p
}

func (uf *UnionFind) GetDistinctRoots() []int {
	rootSet := map[int]bool{}
	var i = 1
	for ; i < len(uf.roots); i++ {
		rootSet[uf.Find(i)] = true
	}
	res := make([]int, 0, len(rootSet))
	for root := range rootSet {
		res = append(res, root)
	}
	return res
}

func (uf *UnionFind) GetSize(p int) int {
	return uf.sizes[uf.Find(p)]
}
