package design

import (
	"container/heap"
	"container/list"
)

type PrioBSTNode struct {
	item *PriorityLRUExpirationCacheItem
	left, right *PrioBSTNode
}

type ExpiryBSTNode struct {
	item *PriorityLRUExpirationCacheItem
	left, right *ExpiryBSTNode
}

type PriorityLRUExpirationCacheItem struct {
	key, val, priority, expireTime int
}

type PriorityLRUExpirationCache struct {

}

func NewPriorityLRUCache(cap int) *PriorityLRUExpirationCache {
	return &PriorityLRUExpirationCache{

	}
}

func (plru *PriorityLRUExpirationCache) Get(key int) int {

}

func (plru *PriorityLRUExpirationCache) Set(key, val, priority, currentTime, expireTime int) int {

}

func (plru *PriorityLRUExpirationCache) Evict(currentTime int) {

}


