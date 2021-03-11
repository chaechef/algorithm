package _2675

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)
func recursion (mul int, str string) string {
	res := ""
	for i := 0; i < len(str); i++ {
		res += strings.Repeat(string(str[i]), mul)
	}
	return res
}

func main() {
	r := bufio.NewReader(os.Stdin)
	var tc int
	fmt.Fscanln(r, &tc)
	for i := 0; i < tc; i++ {
		var mul int
		var str string
		fmt.Fscanln(r, &mul, &str)
		res := recursion(mul, str)
		fmt.Println(res)
	}
}

