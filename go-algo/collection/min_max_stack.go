package collection


type MinMaxStack struct {
	stk, minStk, maxStk []int
}

func NewMinMaxStack() *MinMaxStack {
	return &MinMaxStack{[]int{}, []int{}, []int{}}
}

func (s *MinMaxStack) Peek() int {
	n := len(s.stk)
	return s.stk[n-1]
}

func (s *MinMaxStack) Pop() int {
	n := len(s.stk)
	val := s.stk[n-1]
	s.stk = s.stk[:n-1]

	n = len(s.minStk)
	if val == s.minStk[n-1] {
		s.minStk = s.minStk[:n-1]
	}

	n = len(s.maxStk)
	if val == s.maxStk[n-1] {
		s.maxStk = s.maxStk[:n-1]
	}
	return val
}

func (s *MinMaxStack) Push(num int) {
	s.stk = append(s.stk, num)
	if len(s.minStk) == 0 || num <= s.GetMin() {
		s.minStk = append(s.minStk, num)
	}
	if len(s.maxStk) == 0 || num >= s.GetMax() {
		s.maxStk = append(s.maxStk, num)
	}
}

func (s *MinMaxStack) GetMin() int {
	n := len(s.minStk)
	return s.minStk[n-1]
}

func (s *MinMaxStack) GetMax() int {
	n := len(s.maxStk)
	return s.maxStk[n-1]
}


