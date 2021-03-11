package main

import (
	"fmt"
	"io/ioutil"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func main() {
	bytes, err := ioutil.ReadFile("input.txt")
	check(err)
	fmt.Println(bytes)
	err = ioutil.WriteFile("output.txt", bytes, 0)
	check(err)

}