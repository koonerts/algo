package collections


type MinStack struct {
	main, min []int
}

func NewMinStack() MinStack {
	return MinStack{[]int{}, []int{}}
}

func (ms *MinStack) Push(x int)  {
	ms.main = append(ms.main, x)
	if len(ms.min) == 0 || x <= ms.min[len(ms.min)-1] {
		ms.min = append(ms.min, x)
	}
}

func (ms *MinStack) Pop()  {
	n, n2 := len(ms.main)-1, len(ms.min)-1
	if ms.min[n2] == ms.main[n] {
		ms.min = ms.min[:n2]
	}
	ms.main = ms.main[:n]
}

func (ms *MinStack) Top() int {
	return ms.main[len(ms.main)-1]
}

func (ms *MinStack) GetMin() int {
	return ms.min[len(ms.min)-1]
}