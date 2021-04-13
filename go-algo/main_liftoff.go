package main
/*
import (
	"bufio"
	"fmt"
	"golang.org/x/crypto/ssh/terminal"
	"log"
	"os"
	"syscall"
)

const (
	Up    = 65
	Down  = 66
	Right = 67
	Left  = 68
	CtrlC = 3
)

func main() {
	log.SetFlags(0)
	console, err := NewConsole()
	if err != nil {
		fmt.Println(err)
		return
	}
	defer console.Restore()
inputloop:
	for {
		b, err := console.GetInput()
		if err != nil {
			log.Fatalf("Error calling GetInput(): %s", err)
		}
		switch b {
		case Up:
			log.Println("up")
		case Down:
			log.Println("down")
		case Right:
			log.Println("right")
		case Left:
			log.Println("left")
		case CtrlC:
			log.Println("exiting")
			break inputloop
		default:
			log.Println(b)
		}
	}
}

// Console handles putting the terminal in a raw state and getting unbuffered input.
type Console struct {
	state *terminal.State
	buf   *bufio.Reader
}

func NewConsole() (*Console, error) {
	c := &Console{
		buf: bufio.NewReader(os.Stdin),
	}
	var err error
	c.state, err = terminal.MakeRaw(int(syscall.Stdin))
	if err != nil {
		return nil, err
	}
	return c, nil
}

func (c *Console) Restore() error {
	return terminal.Restore(int(syscall.Stdin), c.state)
}

func (c *Console) GetInput() (byte, error) {
	b, err := c.buf.ReadByte()
	if err != nil {
		return 0, err
	}
	if b != 27 {
		return b, nil
	}
	b, err = c.buf.ReadByte()
	if err != nil {
		return 0, err
	}
	if b != 91 {
		return b, nil
	}
	b, err = c.buf.ReadByte()
	if err != nil {
		return 0, err
	}
	return b, nil
}
*/