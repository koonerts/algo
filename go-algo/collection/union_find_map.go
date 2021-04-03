package collection

type UnionFindMap struct {
	roots, sizes        map[int]int
	connectedComponents int
}

func NewUnionFindMap() *UnionFindMap {
	return &UnionFindMap{map[int]int{}, map[int]int{}, 0}
}

func (uf *UnionFindMap) Insert(p int) bool {
	if uf.Find(p) == -1 {
		uf.roots[p] = p
		uf.sizes[p] = 1
		uf.connectedComponents++
		return true
	}
	return false
}

func (uf *UnionFindMap) Union(p1, p2 int) {
	p1Root, p2Root := uf.Find(p1), uf.Find(p2)
	if p1Root == -1 {uf.Insert(p1); p1Root=p1}
	if p2Root == -1 {uf.Insert(p2); p2Root=p2}
	if p1Root == p2Root {return}

	uf.connectedComponents--
	if uf.sizes[p1Root] >= uf.sizes[p2Root] {
		uf.sizes[p1Root] += uf.sizes[p2Root]
		uf.roots[p2Root] = p1Root
	} else {
		uf.sizes[p2Root] += uf.sizes[p1Root]
		uf.roots[p1Root] = p2Root
	}
}

func (uf *UnionFindMap) Find(p int) int {
	if _, ok := uf.roots[p]; !ok {return -1}

	for p != uf.roots[p] {
		uf.roots[p] = uf.roots[uf.roots[p]]
		p = uf.roots[p]
	}
	return p
}

func (uf *UnionFindMap) GetConnectionComponents() int {
	return uf.connectedComponents
}