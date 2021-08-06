package temp

import "fmt"


type Stack struct {
	nodes []int
	count int
}

func newStack() *Stack {
	return &Stack{}
}

func (s *Stack) push(element int){
	s.nodes = append(s.nodes, element)
	s.count++
}

func (s *Stack) pop() int{
	if s.count == 0 {
		return -1
	}
	res := s.nodes[s.count-1]
	s.nodes = s.nodes[:s.count-1]
	s.count--
	return res
}

func (s *Stack) top() int {
	if s.count == 0 {
		return -1
	}
	return s.nodes[s.count-1]
}

func (s *Stack) empty() int {
	if s.count == 0 {
		return 1
	}
	return 0
}
func main() {
	num := 0
	fmt.Scanf("%d", &num)
	stack := newStack()
	for i := 0; i < num; i++ {
		var inst string
		fmt.Scanf("%s", &inst)
		switch inst {
		case "push":
			var element int
			fmt.Scanf("%d",&element)
			stack.push(element)
		case "pop":
			res := stack.pop()
			fmt.Println(res)
		case "size":
			fmt.Println(stack.count)
		case "empty":
			res := stack.empty()
			fmt.Println(res)
		case "top":
			res := stack.top()
			fmt.Println(res)
		}
	}

}