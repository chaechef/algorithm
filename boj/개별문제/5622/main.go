package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	r := bufio.NewReader(os.Stdin)
	w := bufio.NewWriter(os.Stdout)
	defer w.Flush()

	alpabets := []int {3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,8,9,9,9,10,10,10,10}
	str := ""
	res := 0
	fmt.Fscanln(r, &str)

	for i := 0; i < len(str); i++  {
		ch := str[i] - 'A'
		res += alpabets[ch]
	}

	fmt.Fprintln(w, res)



}
