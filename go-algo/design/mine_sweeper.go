package design

import (
	"bufio"
	"encoding/json"
	"fmt"
	"go-algo/ext/fmtext"
	"math/rand"
	"os"
	"strconv"
	"time"
)

const (
	Unrevealed   = "#"
	RevealedEmpty = "."
	RevealedMine = "X"
)

var directions = [][]int{
	{-1, 0}, {1, 0}, {0, -1}, {0, 1},
	{-1, -1}, {-1, 1}, {1, 1}, {1, -1},
}

type MineSweeperBoard struct {
	Grid          [][]string
	n, m          int
	mineCount     int
	unrevealedCnt int
	Mines         map[int]map[int]bool
	Scanner       *bufio.Scanner
}

func NewMineSweeperBoard(n, m, mineCount int) *MineSweeperBoard {
	grid := make([][]string, n)
	for i := range grid {
		grid[i] = make([]string, m)
		for j := range grid[i] {
			grid[i][j] = Unrevealed
		}
	}
	board := &MineSweeperBoard{Grid: grid, mineCount: mineCount, n: n, m: m, unrevealedCnt:n*m}

	mines := map[int]map[int]bool{}
	possibleMineLocs := make([][]int, n)
	for i := range possibleMineLocs {
		possibleMineLocs[i] = make([]int, m)
		for j := range possibleMineLocs {
			possibleMineLocs[i][j] = j
		}
		r := rand.New(rand.NewSource(time.Now().Unix() + int64(rand.Int())))
		r.Shuffle(m, func(k, l int) {
			possibleMineLocs[i][k], possibleMineLocs[i][l] = possibleMineLocs[i][l], possibleMineLocs[i][k]
		})
	}

	for mineCount > 0 {
		n = len(possibleMineLocs)
		r := rand.New(rand.NewSource(time.Now().Unix() + int64(rand.Int())))
		randX := r.Intn(n)

		m = len(possibleMineLocs[randX])
		r = rand.New(rand.NewSource(time.Now().Unix() + int64(rand.Int())))
		randY := r.Intn(m)

		xVal, yVal := randX, possibleMineLocs[randX][randY]
		if mines[xVal] == nil {
			mines[xVal] = make(map[int]bool)
		}
		mineCount--
		mines[xVal][yVal] = true
		possibleMineLocs[randX][randY], possibleMineLocs[randX][m-1] = possibleMineLocs[randX][m-1], possibleMineLocs[randX][randY]
		possibleMineLocs[randX] = possibleMineLocs[randX][:m-1]
		if len(possibleMineLocs[randX]) == 0 {
			for i := randX + 1; i < len(possibleMineLocs); i++ {
				possibleMineLocs[i-1] = possibleMineLocs[i]
			}
			possibleMineLocs = possibleMineLocs[:n-1]
		}
	}
	board.Mines = mines
	return board
}

func SetupAndPlayMinesweeper() {
	fmt.Print("Welcome to MineSweeper! Please input the dimensions for the board as -> [x, y]: ")
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	dimensionsStr := scanner.Text()
	bytes := []byte(dimensionsStr)
	var dims []int
	err := json.Unmarshal(bytes, &dims)
	for err != nil {
		fmt.Print("An error occurred reading the input. Please try again -> [x, y]: ")
		scanner.Scan()
		dimensionsStr = scanner.Text()
		var dims []int
		err = json.Unmarshal(bytes, &dims)
	}

	fmt.Print("Thanks! Now please input the desired mine count (eg: 10): ")
	scanner.Scan()
	mineCountStr := scanner.Text()
	mineCount, err := strconv.Atoi(mineCountStr)
	for err != nil {
		fmt.Print("An error occurred reading the input. Please try again: ")
		scanner.Scan()
		mineCountStr = scanner.Text()
		mineCount, err = strconv.Atoi(mineCountStr)
	}

	board := NewMineSweeperBoard(dims[0], dims[1], mineCount)
	board.Scanner = scanner
	board.Print(-1, -1)
	fmt.Print("Excellent - The game is ready to start!\nPlease input your first play as -> [x, y]: ")
	board.ReadPlay()
}

func (b *MineSweeperBoard) ReadPlay() {
	b.Scanner.Scan()
	pointStr := b.Scanner.Text()
	bytes := []byte(pointStr)
	var point []int

	err := json.Unmarshal(bytes, &point)
	for err != nil || len(point) != 2 {
		fmt.Print("An error occurred reading the input. Please try again -> [x, y]: ")
		b.Scanner.Scan()
		pointStr = b.Scanner.Text()
		var point []int
		err = json.Unmarshal(bytes, &point)
	}

	if b.Play(point[0], point[1]) {
		if b.unrevealedCnt == b.mineCount {
			fmt.Println("CONGRATULATIONS - You've won!")
			return
		}
		fmt.Print("Please input your next play -> [x, y]: ")
		b.ReadPlay()
	}
}

func (b *MineSweeperBoard) Play(x, y int) bool {
	if b.Mines[x][y] {
		for mx := range b.Mines {
			for my := range b.Mines[mx] {
				b.Grid[mx][my] = RevealedMine
			}
		}
		b.Print(x, y)
		fmt.Println("You chose a mine! GAME OVER")
		return false
	}

	que := []int{x*b.m + y}
	vis := map[int]bool{x*b.m + y:true}
	var point int
	for len(que) > 0 {

		point, que = que[0], que[1:]
		px, py := point/b.m, point%b.m
		adjPoints, adjMinesCount := b.getAdjMineCount(px, py)
		if adjMinesCount > 0 {
			b.Grid[px][py] = strconv.Itoa(adjMinesCount)
			b.unrevealedCnt--
		} else {
			b.Grid[px][py] = RevealedEmpty
			b.unrevealedCnt--
			for _, adjPoint := range adjPoints {
				if vis[adjPoint] {
					continue
				}
				vis[adjPoint] = true
				que = append(que, adjPoint)
			}
		}
	}
	b.Print(x, y)
	return true
}

func (b *MineSweeperBoard) getAdjMineCount(x, y int) (adjPoints []int, adjMinesCount int) {
	for _, dir := range directions {
		nx, ny := x+dir[0], y+dir[1]
		nPoint := nx*b.m + ny
		if nx < 0 || ny < 0 || nx == b.n || ny == b.m {
			continue
		}
		if b.Mines[nx][ny] {
			adjMinesCount++
		} else if b.Grid[nx][ny] == Unrevealed {
			adjPoints = append(adjPoints, nPoint)
		}
	}
	return adjPoints, adjMinesCount
}

func (b *MineSweeperBoard) Print(x, y int) {
	fmt.Printf("\nDimensions: %dx%d\nMine Count: %d\nUnrevealed Count:%d\n", b.n, b.m, b.mineCount, b.unrevealedCnt)
	fmtext.PrintSlice(b.Grid)
	if x >= 0 {
		fmt.Printf("You played [%d,%d]\n", x, y)
	}
	fmt.Println()
}
