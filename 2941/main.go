package main

import (
	"bufio"
	"fmt"
	"os"
)

func sub(str string) string {
	tokens := []string {"c=","c-","d-","lj","nj","s=","z="}

	if len(str) > 2 && str[:3] == "dz=" {
		return str[3:]
	}

	for i := 0; i<len(tokens); i++  {
		if len(str) > 1 && str[0:2] == tokens[i] {
			return str[2:]
		}
	}

	return str[1:]
}

func main() {
	r := bufio.NewReader(os.Stdin)
	w := bufio.NewWriter(os.Stdout)
	defer w.Flush()

	var str string
	var res int
	fmt.Fscanln(r, &str)

	for str != "" {
		str = sub(str)
		res++
	}
	fmt.Fprintln(w, res)
}

