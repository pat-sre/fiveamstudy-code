package main

import (
	"fmt"
	"io"
	"net/http"
	"os"
	"time"
)

//Exercise 1.10:
// Find a web site that produces a large amount of data.
// Investigate caching by running fetchall twice in succession to see whether the reported time changes much.
// Do you get the same content each time? Modify fetchall to print its output to a file so it can be examined.

//Exercise 1.11:
// Try fetchall with longer argument lists, such as samples from the top million web sites
// available at alexa.com. How does the program behave if a web site just doesn’t respond?
// (Section 8.9 describes mechanisms for coping in such cases.)

// The main function creates a channel of strings using make.
// For each command-line argument, the go statement in the first range loop starts a new goroutine
// that calls fetch asynchronously to fetch the URL using http.Get.
// The io.Copy function reads the body of the response and discards it by
// writing to the ioutil.Discard output stream. Copy returns the byte count,
// along with any error that occurred. As each result arrives, fetch sends a summary line on the channel ch.
// The second range loop in main receives and prints those lines.

func fetch(url string, ch chan<- string) {
	start := time.Now()
	resp, err := http.Get(url)
	if err != nil {
		ch <- fmt.Sprint(err)
		return
	}
	b, err := io.Copy(io.Discard, resp.Body)
	if err != nil {
		ch <- fmt.Sprintf("Error while reading %s: %v\n", url, err)
		return
	}
	resp.Body.Close()
	secs := time.Since(start).Seconds()
	ch <- fmt.Sprintf("%.2fs %7d %s", secs, b, url)
}

func main() {
	ch := make(chan string)
	for _, url := range os.Args[1:] {
		go fetch(url, ch)
	}
	for range os.Args[1:] {
		fmt.Println(<-ch)
	}
}
