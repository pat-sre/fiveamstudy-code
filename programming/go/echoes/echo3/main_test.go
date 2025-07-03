package main

import (
	"strings"
	"testing"
)

var args = []string{
	"hello",
	"five",
	"AM",
	"study",
	"crew!",
}

// 13ns
func BenchmarkEfficientEcho(b *testing.B) {
	b.ResetTimer()
	var _ = strings.Join(args, " ")
}

// 16ns
func BenchmarkLessEfficientEcho(b *testing.B) {
	b.ResetTimer()
	var s, sep string
	for _, arg := range args {
		s += sep + arg
		sep = " "
	}
}
