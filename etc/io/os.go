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
	read, err := os.Open("input.txt")
	check(err)
	defer read.Close()
	write, err := os.Create("output.txt")
	check(err)
	defer write.Close()

	buff := make([]byte ,1024)
	for {
		cnt, err := read.Read(buff)
		check(err)
		fmt.Println(cnt ,string(buff))
		if cnt == 0 {
			break
		}
		_, err = write.Write(buff[:cnt])
		check(err)
	}
}