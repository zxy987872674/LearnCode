package main

import (
	"fmt"
	"time"
)

func main() {
	defer fmt.Println("world")

	fmt.Println("hello")
	time.Sleep(time.Second * 2)
}
