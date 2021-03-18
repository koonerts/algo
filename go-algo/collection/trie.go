package collection

import (
	_ "github.com/dghubble/trie"
)

type Trie struct {
	root *TrieNode
}

type TrieNode struct {
	isEnd bool
	children [26]*TrieNode
}


func Constructor() Trie {
	return Trie{root: &TrieNode{}}
}


func (t *Trie) Insert(word string)  {
	if t.root.children[word[0]-'a'] == nil {
		t.root.children[word[0]-'a'] = &TrieNode{}
	}
	parent := t.root.children[word[0]-'a']
	for i := 1; i < len(word); i++ {
		if parent.children[word[i]-'a'] == nil {
			parent.children[word[i]-'a'] = &TrieNode{}
		}
		parent = parent.children[word[i]-'a']
	}
	parent.isEnd = true
}


func (t *Trie) Search(word string) bool {
	node := t.root.children[word[0]-'a']
	if node == nil {
		return false
	}

	for i := 1; i < len(word); i++ {
		if node.children[word[i]-'a'] == nil {
			return false
		}
		node = node.children[word[i]-'a']
	}
	if node.isEnd {
		return true
	}
	return false
}

func (t *Trie) StartsWith(prefix string) bool {
	node := t.root.children[prefix[0]-'a']
	if node == nil {
		return false
	}

	for i := 1; i < len(prefix); i++ {
		if node.children[prefix[i]-'a'] == nil {
			return false
		}
		node = node.children[prefix[i]-'a']
	}
	return true
}