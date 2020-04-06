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
	str string
)

func sum(arr []int) (res int) {
	for i := 0; i < len(arr); i++ {
		res += arr[i]
	}
	return
}

func main() {
	defer w.Flush()
	fmt.Fscanf(r,"%d ", &tc)
	for i := 0; i < tc; i++ {
		fmt.Fscanf(r,"%s ", &str)
		dp := make([]int, len(str))
		if str[0] == 'O'{
			dp[0] = 1
		}else{
			dp[0] = 0
		}
		for j := 1; j < len(str); j++ {
			if str[j] == 'O'  {
				dp[j] = dp[j-1] +1
			}
		}
		fmt.Fprintln(w,sum(dp))
	}

}
