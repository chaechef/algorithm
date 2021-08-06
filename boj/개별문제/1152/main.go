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

	var (
		ch byte
		isprev bool
		res int
		str string
	)
	str, _ = r.ReadString('\n')

	for i := 0; i < len(str); i++ {
		ch = str[i]
		if (ch >= 'a' && ch <= 'z') || (ch >= 'A' && ch <= 'Z') {
			if isprev == false {
				res++
				isprev = true
			}
		} else if ch == ' ' {
			isprev = false
		}
	}
	fmt.Fprintln(w, res)
}
