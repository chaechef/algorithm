package main

import (
	"bufio"
	"os"
)

func main() {
	//fmt.Print("Hello World!") //4ms
	//fmt.Println("Hello World!") //4ms
	//fmt.Printf("%s","Hello World!") //4ms
	w := bufio.NewWriter(os.Stdout)
	w.WriteString("Hello World!")
	w.Flush() //4ms

}
