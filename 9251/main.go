package main

import (
	"bufio"
	"fmt"
	"os"
)

var (
	r = bufio.NewReader(os.Stdin)
	w = bufio.NewWriter(os.Stdout)
	s1 string
	s2 string
	cache [][]string
	res int
)

func main() {
	defer w.Flush()
	fmt.Fscanf(r, "%s ", &s1)
	fmt.Fscanf(r, "%s ", &s2)
	//cache init
	cache = make([][]string, len(s1))
	for i := 0; i < len(s1); i++ {
		cache[i] = make([]string, len(s2))
		for j := 0; j < len(s2); j++ {
			cache[i][j] = "."
		}
	}
	res := recursion(s1,s2)
	fmt.Fprintln(w, len(res))
}

func recursion(string1 string, string2 string) string {
	l1 := len(string1)
	l2 := len(string2)

	if l1 == 0 || l2 == 0 {
		return ""
	}
	if cache[l1-1][l2-1] != "." {
		return cache[l1-1][l2-1]
	}

	if string1[l1-1] == string2[l2-1] {
		res := recursion(string1[:l1-1],string2[:l2-1]) + string(string1[l1-1])
		cache[l1-1][l2-1] = res
	}else {
		var temp1, temp2 string
		if l1-1 >= 0 && l2 >= 0{
			temp1 = recursion(string1[:l1-1], string2[:l2])

		}
		if l1 >= 0 && l2 -1 >= 0{
			temp2 = recursion(string1[:l1],string2[:l2-1])

		}
		if len(temp2) > len(temp1) {
			cache[l1-1][l2-1] = temp2
		}else{
			cache[l1-1][l2-1] = temp1
		}
	}
	return cache[l1-1][l2-1]

}
