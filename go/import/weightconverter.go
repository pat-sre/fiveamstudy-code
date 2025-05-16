package main

import (
	"fiveamstudy-code/go/weightconv"
	"fmt"
	"os"
	"strconv"
)

func main() {
	w := os.Args[1]
	if len(os.Args) > 2 {
		fmt.Println("Too many args", os.Args)
		os.Exit(1)
	}
	t, err := strconv.ParseFloat(w, 64)
	if err != nil {
		os.Exit(1)
	}
	k := weightconv.Kilograms(t)
	p := weightconv.Pounds(t)
	fmt.Printf("%s = %s\n", k, weightconv.KToP(k))
	fmt.Printf("%s = %s\n", p, weightconv.PToK(p))
}
