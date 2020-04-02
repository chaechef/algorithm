package main

import (
	"bufio"
	"fmt"
	"os"
)

func splitNumber(num int) int {
	res := 0
	for num > 0 {
		res += num % 10
		num /= 10
	}
	return res
}
func main() {
	r := bufio.NewReader(os.Stdin)
	w := bufio.NewWriter(os.Stdout)
	defer w.Flush()

	var num int
	var check = false
	fmt.Fscanln(r, &num)

	for i := 1; i <= num; i++ {
		res := i + splitNumber(i)
		if res == num {
			fmt.Fprintln(w, i)
			check = true
			break
		}
	}
	if check == false {
		fmt.Fprintln(w, 0)
	}
}
