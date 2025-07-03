package main

import (
	"bufio"
	"fmt"
	"os"
)

// Exercise 1.4:
// Modify dup2 to print the names of all files
// in which each duplicated line occurs.

func main() {
	counts := make(map[string]int)
	occurences := make(map[string][]string) // occurences[word]: [file1, file2]
	files := os.Args[1:]
	if len(files) == 0 {
		countLines(os.Stdin, counts, occurences)
	} else {
		for _, arg := range files {
			f, err := os.Open(arg)
			if err != nil {
				fmt.Fprintf(os.Stderr, "dup2: %v\n", err)
				continue
			}
			counts, occurences = countLines(f, counts, occurences)
			defer f.Close()
		}
	}
	// fmt.Println(counts)
	// fmt.Println(occurences)
	for idx, count := range counts {
		if count > 1 {
			fmt.Printf("%d\t%s\t%s\n", count, idx, occurences[idx])
		}
	}

}

func countLines(f *os.File, counts map[string]int, occurences map[string][]string) (map[string]int, map[string][]string) {
	input := bufio.NewScanner(f)
	var line string
	for input.Scan() {
		line = input.Text()
		counts[line]++
		occurences[line] = append(occurences[line], f.Name())
	}

	return counts, occurences
}
