package main

import "fmt"

var p = f()

type Celsius float64

func f() *int {
	v := 1
	return &v
}

func (c Celsius) String() string {
	return fmt.Sprintf("%g°C", c)
}

func main() {
	test := "Welcome to 5 AM Study"
	var medals [3]string
	medals[0] = "gold"
	medals[1] = "silver"
	medals[2] = "bronze"
	fmt.Println(&test)
	var c Celsius
	fmt.Println(c.String()) // "100°C"
	fmt.Printf("%v\n", c)   // "100°C"; no need to call String explicitly
	fmt.Printf("%s\n", c)   // "100°C"
	fmt.Println(c)          // "100°C"
	fmt.Printf("%g\n", c)   // "100"; does not call String
	fmt.Println(float64(c)) // "100"; does not call String
}
