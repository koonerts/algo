package collection


type UnionFind struct {
	roots, sizes []int32
}

func NewUnionFind(size int32) *UnionFind {
	r, s := make([]int32, size+1), make([]int32, size+1)
	for i := range r {
		r[i] = int32(i)
		s[i] = 1
	}
	r[0] = -1
	s[0] = -1
	return &UnionFind{r,s}
}

func (uf *UnionFind) Union(p, q int32) {
	proot := uf.Find(p)
	qroot := uf.Find(q)
	if proot == qroot {return}

	if uf.sizes[proot] >= uf.sizes[qroot] {
		uf.roots[qroot] = proot
		uf.sizes[proot] += uf.sizes[qroot]
	} else {
		uf.roots[proot] = qroot
		uf.sizes[qroot] += uf.sizes[proot]
	}
}

func (uf *UnionFind) Find(p int32) int32 {
	if p >= int32(len(uf.roots)) {
		return -1
	}

	for uf.roots[p] != p {
		uf.roots[p] = uf.roots[uf.roots[p]]
		p = uf.roots[p]
	}
	return p
}

func (uf *UnionFind) GetDistinctRoots() []int32 {
	rootSet := map[int32]bool{}
	var i int32 = 1
	for ; i < int32(len(uf.roots)); i++ {
		rootSet[uf.Find(i)] = true
	}
	res := make([]int32, 0, len(rootSet))
	for root := range rootSet {
		res = append(res, root)
	}
	return res
}

func (uf *UnionFind) GetSize(p int32) int32 {
	return uf.sizes[uf.Find(p)]
}