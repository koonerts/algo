package recursion


type SudokuGame struct {
	board [][]byte
	rows [][]bool
	cols [][]bool
	boxes [][]bool
}

func NewSudokuGame(board [][]byte) *SudokuGame {
	rows, cols, boxes := make([][]bool, 9), make([][]bool, 9), make([][]bool, 9)
	for i := range rows {
		rows[i], cols[i], boxes[i] = make([]bool, 9), make([]bool, 9), make([]bool, 9)
	}
	game := &SudokuGame{board, rows, cols, boxes}
	for i := range board {
		for j := range board[i] {
			if board[i][j] != '.' {
				game.place(i, j, board[i][j])
			}
		}
	}
	return game
}

func (sg SudokuGame) canPlace(row, col int, val byte) bool {
	boxId := row/3 * 3 + col/3
	valIdx := int(val-'0') - 1
	return sg.board[row][col] == '.' && !sg.rows[row][valIdx] && !sg.cols[col][valIdx] && !sg.boxes[boxId][valIdx]
}

func (sg *SudokuGame) place(row, col int, val byte) {
	boxId := row/3 * 3 + col/3
	valIdx := int(val-'0') - 1
	sg.board[row][col] = val
	sg.rows[row][valIdx], sg.cols[col][valIdx], sg.boxes[boxId][valIdx] = true, true, true
}

func (sg *SudokuGame) remove(row, col int) {
	boxId := row/3 * 3 + col/3
	valIdx := int(sg.board[row][col]-'0') - 1
	sg.rows[row][valIdx], sg.cols[col][valIdx], sg.boxes[boxId][valIdx] = false, false, false
	sg.board[row][col] = '.'
}

func solveSudoku(board [][]byte)  {
	game := NewSudokuGame(board)
	var dfs func(row, col int) bool
	dfs = func(row, col int) bool {
		if row >= 8 && col >= 9 {
			return true
		} else if col >= 9 {
			return dfs(row+1, 0)
		} else if game.board[row][col] != '.' {
			return dfs(row, col+1)
		}

		for i := 1; i <= 9; i++ {
			if game.canPlace(row, col, byte(i+'0')) {
				game.place(row, col, byte(i+'0'))
				isSolved := dfs(row, col+1)
				if isSolved {
					return true
				}
				game.remove(row, col)
			}
		}
		return false
	}
	dfs(0, 0)
}