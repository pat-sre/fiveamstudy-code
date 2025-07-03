package main

import (
	"fmt"
	"os"
)

func main() {
	// as we dont set the value, the "zero value" for string will be set, thats ""
	var s, sep string
	for i := 1; i < len(os.Args); i++ {
		s += sep + os.Args[i]
		sep = ""
	}
	fmt.Println(s)
}
