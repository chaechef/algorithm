package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	r := bufio.NewReader(os.Stdin)
	num := 0
	fmt.Fscanf(r, "%d", &num)
	arr := make([]bool , 1001)
	if num < 100 {
		fmt.Println(num)

	}else {
		sum := 99
		for i := 100; i <= num; i++ {
			curr := i
			var a, b, c int
			c = curr % 10
			curr /= 10
			b = curr % 10
			a = curr / 10

			if a-b == b- c {
				arr[i] = true
				sum++
			}
		}
		fmt.Println(sum)

	}
}