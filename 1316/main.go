package main

import (
	"bufio"
	"fmt"
	"os"
)

func isGroupWord(str string) bool {
	alphabets := [26]bool{}
	check := true
	var prev byte

	for i := 0; i < len(str); i++ {
		ch := str[i] - 'a'
		if alphabets[ch] == true && prev != ch {
			check = false
			break
		}
		alphabets[ch] = true
		prev = ch
	}
	return  check
}
func main()  {
	r := bufio.NewReader(os.Stdin)
	w := bufio.NewWriter(os.Stdout)
	defer w.Flush()

	var t, res int

	fmt.Fscanln(r, &t)
	for i := 0; i < t; i++ {
		var str string
		fmt.Fscanln(r, &str)
		if isGroupWord(str) == true {
			res++
		}
	}
	fmt.Fprintln(w, res)
}
