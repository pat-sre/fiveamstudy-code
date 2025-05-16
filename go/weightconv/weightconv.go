package weightconv

import "fmt"

type Pounds float64
type Kilograms float64

func (p Pounds) String() string    { return fmt.Sprintf("%g Pounds", p) }
func (k Kilograms) String() string { return fmt.Sprintf("%g Kilograms", k) }
