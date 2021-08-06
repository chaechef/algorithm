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

	var tc int
	var m int
	var str string

	fmt.Fscanln(r, &tc)

	for i := 0; i < tc; i++ {
		var res string
		fmt.Fscanf(r, "%d %s\n", &m, &str)
		for j := 0; j < len(str); j++ {
			for k := 0; k < m; k++ {
				res += string(str[j])
			}
		}
		fmt.Println(res)

	}

}
