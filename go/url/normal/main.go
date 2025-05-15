package main

import (
	"fmt"
	"io"
	"net/http"
	"os"
	"strings"
)

// Exercise 1.7:
// The function call io.Copy(dst, src) reads from src and writes to dst.
// Use it instead of ioutil.ReadAll to copy the response body to os.Stdout
// without requiring a buffer large enough to hold the entire stream.
// Be sure to check the error result of io.Copy.

// Exercise 1.8:
// Modify fetch to add the prefix http:// to each argument URL if it is missing.
// You might want to use strings.HasPrefix.

// Exercise 1.9: Modify fetch to also print the HTTP status code, found in resp.Status

func main() {
	for _, url := range os.Args[1:] {
		if !strings.HasPrefix(url, "https://") {
			url = "https://" + url
		}
		resp, err := http.Get(url)
		if err != nil {
			fmt.Fprintf(os.Stderr, "fetch: %v\n", err)
			os.Exit(1)
		}
		_, err = io.Copy(os.Stdout, resp.Body)
		if err != nil {
			fmt.Fprintf(os.Stderr, "fetch: reading %s: %v\n", url, err)
		}
		fmt.Printf("statusCode=%s\n", resp.Status)
	}
}
