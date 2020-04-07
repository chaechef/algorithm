package main

import (
	"bufio"
	"fmt"
	"os"
)

func factorial(num int) int {

	if num == 0 {
		return 1
	}
	return num * factorial(num-1)
}
func main() {
	r := bufio.NewReader(os.Stdin)
	w := bufio.NewWriter(os.Stdout)
	defer w.Flush()

	var num, res int
	fmt.Fscanln(r, &num)
	res = factorial(num)
	fmt.Fprintln(w, res)

}
