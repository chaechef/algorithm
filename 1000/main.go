package main

import (
	"fmt"
	"os"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func main() {
	file, _ := os.Open("/1000/input.txt")
	fmt.Println(file)
	b1 := make([]byte, 5)
	n1, _ := file.Read(b1)
	fmt.Println(n1)
}