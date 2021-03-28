package collection


type WordDictionary struct {
	root *WordTrieNode
}

type WordTrieNode struct {
	children []*WordTrieNode
	isEnd bool
}

func (wtn *WordTrieNode) getOrAdd(b byte) *WordTrieNode {
	if wtn.children[b-'a'] == nil {
		wtn.children[b-'a'] = &WordTrieNode{}
	}
	return wtn.children[b-'a']
}

/** Initialize your data structure here. */
func NewWordDictionary() WordDictionary {
	return WordDictionary{&WordTrieNode{}}
}


func (wd *WordDictionary) AddWord(word string)  {
	prev := wd.root
	for i := 0; i < len(word); i++ {
		prev.getOrAdd(word[i])
	}
	prev.isEnd = true
}

// TODO:
func (wd *WordDictionary) Search(word string) bool {
	return false
}


/**
 * Your WordDictionary object will be instantiated and called as such:
 * obj := Constructor();
 * obj.AddWord(word);
 * param_2 := obj.Search(word);
 */