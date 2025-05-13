package main

import (
	"fmt"
	"os"
)

// Exercise 1.2:
// Modify the echo program to print the index and value of each of its arguments,
// one per line.

func main() {
	s, sep := "", ""
	for idx, arg := range os.Args { // _ is to not assign the index
		fmt.Println(idx, arg, sep)
	}
	fmt.Println(s)
}
