package recursion

type UnsafeInfo struct {
	rows, cols, diag1, diag2 map[int]bool
}
func NewUnsafeInfo() *UnsafeInfo {
	return &UnsafeInfo{
		rows:  map[int]bool{},
		cols:  map[int]bool{},
		diag1: map[int]bool{},
		diag2: map[int]bool{},
	}
}

func isSafe(usi *UnsafeInfo, x, y int) bool {
	if usi.rows[x] || usi.cols[y] || usi.diag1[x-y] || usi.diag2[x+y] {
		return false
	}
	return true
}

func placeQueen(board [][]string, usi *UnsafeInfo, x, y int) bool {
	if board != nil {
		board[x][y] = "q"
	}
	usi.rows[x] = true
	usi.cols[y] = true
	usi.diag1[x-y] = true
	usi.diag2[x+y] = true
	return true
}

func removeQueen(board [][]string, usi *UnsafeInfo, x, y int) bool {
	if board != nil {
		board[x][y] = "-"
	}
	usi.rows[x] = false
	usi.cols[y] = false
	usi.diag1[x-y] = false
	usi.diag2[x+y] = false
	return false
}

func PlaceQueens(board [][]string) (placedBoards [][][]string) {
	usi := NewUnsafeInfo()
	var place func(x int) bool
	place = func(x int) bool {
		if x >= len(board) {
			boardCopy := make([][]string, len(board))
			for i := range board {
				boardCopy[i] = make([]string, len(board[i]))
				copy(boardCopy[i], board[i])
			}
			placedBoards = append(placedBoards, boardCopy)
			return false
		} else {
			isPlaced := false
			for y := range board[x] {
				if isSafe(usi, x, y) {
					isPlaced = placeQueen(board, usi, x, y)
					if !place(x+1) {
						isPlaced = removeQueen(board, usi, x, y)
					}
				}
			}
			return isPlaced
		}
	}
	place(0)
	return placedBoards
}


func TotalNQueens(n int) (cnt int) {
	usi := NewUnsafeInfo()
	var place func(x int) bool
	place = func(x int) bool {
		if x >= n {
			cnt++
			return false
		} else {
			isPlaced := false
			for y := 0; y < n; y++ {
				if isSafe(usi, x, y) {
					isPlaced = placeQueen(nil, usi, x, y)
					if !place(x+1) {
						isPlaced = removeQueen(nil, usi, x, y)
					}
				}
			}
			return isPlaced
		}
	}
	place(0)
	return cnt
}
