package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	r := bufio.NewReader(os.Stdin)
	var l int
	var num string
	fmt.Fscanln(r, &l)
	fmt.Fscanln(r, &num)
	sum := 0
	for i := 0; i < l; i++ {
		a, _ := strconv.Atoi(string(num[i]))
		sum += a
	}
	fmt.Println(sum)
}