package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

func main() {
	r := bufio.NewReader(os.Stdin)
	w := bufio.NewWriter(os.Stdout)
	defer w.Flush()

	var n int
	fmt.Fscanln(r, &n)
	arr := make([]int, n)
	for i := 0; i < n; i++	{
		fmt.Fscanln(r,&arr[i])
	}
	sort.Ints(arr)
	for _, v := range arr{
		fmt.Fprintln(w, v)
	}
}
