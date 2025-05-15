package main

import "fmt"

var p = f()

func f() *int {
	v := 1
	return &v
}

func main() {
	fmt.Println(p, *p)
}
