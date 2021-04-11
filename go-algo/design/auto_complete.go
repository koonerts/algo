package design

// TODO
type AcsNode struct {
	val string
	children []*AcsNode
	isEnd bool
	times int
}

func NewAcsNode(b byte) *AcsNode {
	return &AcsNode{val:string(b), children:make([]*AcsNode, 27)}
}

type AutocompleteSystem struct {
	root, prev *AcsNode
	currentSentence []byte
}


func Constructor(sentences []string, times []int) AutocompleteSystem {
	root := &AcsNode{children: make([]*AcsNode, 27)}
	for i, sentence := range sentences {
		prev := root
		for j := range sentence {
			prev = prev.GetOrAdd(sentence[j])
		}
		prev.isEnd = true
		prev.times = times[i]
	}
	return AutocompleteSystem{root, nil, []byte{}}
}


func (acs *AutocompleteSystem) Input(c byte) []string {
	return nil
}

func (acsn *AutocompleteSystem) findSentence(buf *[]byte) {

}

func (acsn *AcsNode) GetOrAdd(b byte) *AcsNode {
	var idx byte = 26
	if b != ' ' {
		idx = b - 'a'
	}
	if acsn.children[idx] == nil {
		acsn.children[idx] = NewAcsNode(b)
	}
	return acsn.children[idx]
}
