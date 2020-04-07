package main

import (
	"bufio"
	"fmt"
	"os"
)

func reverse(num int) (res int) {
	for num > 0 {
		res += num % 10
		num /= 10
		if num > 0 {
			res *= 10
		}
	}
	return
}
func main() {
	r := bufio.NewReader(os.Stdin)
	w := bufio.NewWriter(os.Stdout)
	defer w.Flush()

	var (
		num1 int
		num2 int
	)

	fmt.Fscanln(r, &num1, &num2)
	num1 = reverse(num1)
	num2 = reverse(num2)

	if num1 > num2 {
		fmt.Fprintln(w, num1)
	}else {
		fmt.Fprintln(w, num2)
	}

}
