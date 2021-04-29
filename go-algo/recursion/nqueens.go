package recursion


type nQueens struct {
	board [][]byte
	n int
	rows, cols []bool
	diag1, diag2 map[int]bool
	solutions [][]string
}

func newNQueens(n int) *nQueens {
	board := make([][]byte, n)
	for i := range board {
		board[i] = make([]byte, n)
		for j := range board[i] {
			board[i][j] = '.'
		}
	}
	rows, cols := make([]bool, n), make([]bool, n)
	diag1, diag2 := map[int]bool{}, map[int]bool{}

	return &nQueens{board, n, rows, cols, diag1, diag2, [][]string{}}
}

func (nq *nQueens) placeQueen(r, c int) {
	nq.board[r][c] = 'Q'
	nq.rows[r] = true
	nq.cols[c] = true
	nq.diag1[r-c] = true
	nq.diag2[r+c] = true
}

func (nq *nQueens) removeQueen(r, c int) {
	nq.board[r][c] = '.'
	nq.rows[r] = false
	nq.cols[c] = false
	nq.diag1[r-c] = false
	nq.diag2[r+c] = false
}

func (nq *nQueens) canPlace(r, c int) bool {
	return nq.board[r][c] == '.' && !nq.rows[r] && !nq.cols[c] && !nq.diag1[r-c] && !nq.diag2[r+c]
}

func (nq *nQueens) getSolution() []string {
	sol := make([]string, nq.n)
	for i := range nq.board {
		sol[i] = string(nq.board[i])
	}
	return sol
}

func solveNQueens(n int) (solutions [][]string) {
	game := newNQueens(n)
	var dfs func(row int)
	dfs = func(row int) {
		if row >= n {
			game.solutions = append(game.solutions, game.getSolution())
			return
		}

		for col := 0; col < n; col++ {
			if game.canPlace(row, col) {
				game.placeQueen(row, col)
				dfs(row+1)
				game.removeQueen(row, col)
			}
		}
	}
	dfs(0)
	return game.solutions
}
