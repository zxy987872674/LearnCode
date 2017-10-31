package main

import (
	"fmt"
	"runtime"
)

func main() {
	fmt.Print("Go runs on \n")
	os := runtime.GOOS //获取当前的操作系统
	switch os {
	case "darwin":
		fmt.Println("OS X.")
	case "linux":
		fmt.Println("Linux.")
	default:
		fmt.Printf("%s.", os)
	}
}
