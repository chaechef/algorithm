package main

import (
	"bufio"
	"fmt"
	"os"
)

var (
	r = bufio.NewReader(os.Stdin)
	w = bufio.NewWriter(os.Stdout)
	inst string
	instNum int
)

type stack struct {
	nodes []int
	count int
}

func newStack() stack {
	return stack{}
}

func (s *stack)push(n int)  {
	s.nodes = append(s.nodes, n)
	s.count++
}

func (s *stack)pop() int {
	if s.count == 0 {
		return -1
	}
	temp := s.nodes[s.count-1]
	s.nodes = s.nodes[:s.count-1]
	s.count--
	return temp
}

func (s *stack)top() int {
	if s.count == 0 {
		return -1
	}
	temp := s.nodes[s.count-1]
	return temp
}

func main() {
	defer w.Flush()
	tstack := newStack()
	fmt.Fscanf(r, "%d ", &instNum)
	for i := 0; i < instNum; i++ {
		fmt.Fscanf(r, "%s ", &inst)
		var temp int
		switch inst {
		case "push":
			fmt.Fscanf(r, "%d ", &temp)
			tstack.push(temp)
		case "pop":
			temp = tstack.pop()
			fmt.Fprintln(w, temp)
		case "size":
			fmt.Fprintln(w, tstack.count)
		case "empty":
			if tstack.count == 0 {
				fmt.Fprintln(w, 1)
			}else {
				fmt.Fprintln(w, 0)
			}
		case "top":
			temp = tstack.top()
			fmt.Fprintln(w, temp)
		}
	}
}
