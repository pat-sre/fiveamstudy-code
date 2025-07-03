package popcount

var pc [256]byte

// Exercise 2.3:
// Rewrite PopCount to use a loop instead of a single expression.
// Compare the performance of the two versions.
// (Section 11.4 shows how to compare the performance of different implementations systematically.)

// Exercise 2.4:
// Write a version of PopCount that counts bits by shifting its argument through 64 bit positions,
// testing the rightmost bit each time. Compare its performance to the table-lookup version.

// Exercise 2.5:
// The expression x&(x-1) clears the rightmost non-zero bit of x.
// Write a version of PopCount that counts bits by using this fact,
// and assess its performance

func init() {
	for i := range pc {
		pc[i] = pc[i/2] + byte(i&1)
	}
}

func PopCount(x uint64) int {
	return int(pc[byte(x>>(0*8))] +
		pc[byte(x>>(1*8))] +
		pc[byte(x>>(2*8))] +
		pc[byte(x>>(3*8))] +
		pc[byte(x>>(4*8))] +
		pc[byte(x>>(5*8))] +
		pc[byte(x>>(6*8))] +
		pc[byte(x>>(7*8))])
}
