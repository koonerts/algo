package collections

import "container/heap"

type MedianFinder struct {
	min *IntMinHeap
	max *IntMaxHeap
}

func NewMedianFinder() MedianFinder {
	return MedianFinder{&IntMinHeap{}, &IntMaxHeap{}}
}

func (mf *MedianFinder) AddNum(num int)  {
	if len(*mf.max) == 0 || num <= (*mf.max)[0] {
		heap.Push(mf.max, num)
	} else {
		heap.Push(mf.min, num)
	}

	if len(*mf.min) > len(*mf.max) || len(*mf.max)-1 > len(*mf.min) {
		mf.resize()
	}
}

func (mf *MedianFinder) FindMedian() float64 {
	l1, l2 := len(*mf.min), len(*mf.max)
	if (l1+l2)%2 == 1 {
		return float64((*mf.max)[0])
	} else {
		return (float64((*mf.max)[0])+float64((*mf.min)[0]))/2
	}
}

func (mf *MedianFinder) resize() {
	if len(*mf.max) > len(*mf.min) {
		heap.Push(mf.min, heap.Pop(mf.max).(int))
	} else {
		heap.Push(mf.max, heap.Pop(mf.min).(int))
	}
}