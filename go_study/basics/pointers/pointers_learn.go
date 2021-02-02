package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	text, _ := reader.ReadString('\n')
	text = text[:len(text) -1]
	number, _ := strconv.Atoi(text)
	if(number % 2 == 0) {
		fmt.Println("YES")
	} else {fmt.Println("NO")}
}
