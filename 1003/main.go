package main

import (
	"bufio"
	"fmt"
	"os"
)

var (
	r = bufio.NewReader(os.Stdin)
	w = bufio.NewWriter(os.Stdout)
	tc int
	num int
	zeronums [41]int
	onenums [41]int
)

func main() {
	defer w.Flush()
	fmt.Fscanf(r,"%d ", &tc)

	//init
	zeronums[0] = 1
	onenums[1] = 1

	for i := 2; i < 41; i++ {
		zeronums[i] = zeronums[i-1] + zeronums[i-2]
		onenums[i] = onenums[i-1] + onenums[i-2]
	}

	for i := 0; i < tc; i++ {
		fmt.Fscanf(r,"%d ", &num)
		fmt.Fprintln(w, zeronums[num], onenums[num])
	}
}
