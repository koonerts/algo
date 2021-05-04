package collection

import (
	"container/list"
)

type LRUCacheItem struct {
	key, value int
}
type LRUCache struct {
	cache      map[int]*list.Element
	head, tail *list.Element
	kvList     *list.List
	size       int
	capacity   int
}

func NewLRUCache(capacity int) LRUCache {
	ll := list.New()
	head := ll.PushFront(nil)
	tail := ll.PushBack(nil)
	return LRUCache{
		cache:    map[int]*list.Element{},
		head:     head,
		tail:     tail,
		kvList:   ll,
		size:     0,
		capacity: capacity,
	}
}

func (lru *LRUCache) Get(key int) int {
	elem := lru.cache[key]
	if elem == nil {return -1}

	lru.kvList.MoveAfter(elem, lru.head)
	return elem.Value.(*LRUCacheItem).value
}


func (lru *LRUCache) Put(key int, value int) {
	elem := lru.cache[key]
	if elem == nil {
		elem = lru.kvList.InsertAfter(&LRUCacheItem{key, value}, lru.head)
		lru.cache[key] = elem
		lru.size++

		if lru.size > lru.capacity {
			removedElem := lru.tail.Prev()
			delete(lru.cache, removedElem.Value.(*LRUCacheItem).key)
			lru.kvList.Remove(removedElem)
			lru.size--
		}
	} else {
		elem.Value.(*LRUCacheItem).value = value
		lru.kvList.MoveAfter(elem, lru.head)
	}
}
