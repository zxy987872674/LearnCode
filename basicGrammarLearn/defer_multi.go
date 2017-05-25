package main

import (
	"fmt"
	"time"
)

func main() {
	fmt.Println("counting")

	for i := 0; i < 10; i++ {
		//defer相当与将操作放入一个栈，当函数返回后，才执行，且执行时，后入先出
		defer fmt.Println(i)
		time.Sleep(time.Second * 1)
	}

	fmt.Println("done")
	time.Sleep(time.Second * 1)
}
