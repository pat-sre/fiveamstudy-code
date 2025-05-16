package tempconv

// Exercise 2.1:
// Add types, constants, and functions to tempconv for processing temperatures in the Kelvin scale,
// where zero Kelvin is −273.15°C and a difference of 1K has the same magnitude as 1°C.

// CToF converts Celsius temp to a Fahrenheit temp
func CToF(c Celsius) Fahrenheit { return Fahrenheit(c*9/5 + 32) }

// FToC converts a Fahrenheit temp to a Celsius temp
func FToC(f Fahrenheit) Celsius { return Celsius((f - 32) * 5 / 9) }

// KToF converts Kelvin temp to Fahrenheit
func KToF(k Kelvin) Fahrenheit { return CToF(KToC(k)) }

// FToC converts Kelvin temp to Celsius
func KToC(k Kelvin) Celsius { return Celsius(k + 273) }

//FToK converts Fahrenheit to Kelvin temp

//CToK converts Celsius to Kelvin temp
