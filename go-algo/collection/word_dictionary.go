package collection


type WordDictionary struct {
	root *WordTrieNode
}

type WordTrieNode struct {
	val string
	children []*WordTrieNode
	isEnd bool
}

func NewWordTrieNode(val string) *WordTrieNode {
	children := make([]*WordTrieNode, 26)
	return &WordTrieNode{val:val, children:children}
}



/** Initialize your data structure here. */
func NewWordDictionary() WordDictionary {
	wtn := NewWordTrieNode("")
	return WordDictionary{wtn}
}

func (wtn *WordTrieNode) getOrAdd(b byte) *WordTrieNode {
	if wtn.children[b-'a'] == nil {
		wtn.children[b-'a'] = NewWordTrieNode(string(b))
	}
	return wtn.children[b-'a']
}

func (wd *WordDictionary) AddWord(word string)  {
	prev := wd.root
	for i := range word {
		prev = prev.getOrAdd(word[i])
	}
	prev.isEnd = true
}

func (wd *WordDictionary) Search(word string) bool {
	prev := wd.root
	return searchHelper(prev, word, 0)
}

func searchHelper(prev *WordTrieNode, word string, idx int) bool {
	if idx == len(word) && prev.isEnd {
		return true
	}


	if word[idx] != '.' && prev.children[word[idx]-'a'] == nil {
		return false
	} else if word[idx] != '.' {
		prev = prev.children[word[idx]-'a']
		return searchHelper(prev, word, idx+1)
	} else {
		for j := range prev.children {
			if prev.children[j] == nil {continue}
			if idx == len(word)-1 && prev.children[j].isEnd {
				return true
			}
			isFound := searchHelper(prev.children[j], word, idx+1)
			if isFound {
				return true
			}
		}
	}
	return false
}


/**
 * Your WordDictionary object will be instantiated and called as such:
 * obj := Constructor();
 * obj.AddWord(word);
 * param_2 := obj.Search(word);
 */