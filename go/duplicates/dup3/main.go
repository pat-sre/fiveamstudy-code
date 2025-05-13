package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {
	counts := make(map[string]int)
	for _, filename := range os.Args[1:] {
		data, err := os.ReadFile(filename)
		if err != nil {
			fmt.Fprintf(os.Stderr, "dup3: %v\n", err)
		}
		for _, line := range strings.Split(string(data), "\n") {
			counts[line]++
		}
	}
	fmt.Println(counts)
	for line, n := range counts {
		fmt.Printf("%d\t%s\n", n, line)
	}
}
