package main

import "fmt"

func main() {
	//申明一个数组，里面有2个字符串
	var a [2]string
	a[0] = "Hello"
	a[1] = "World"
	fmt.Println(a[0], a[1])
	fmt.Println(a)
}
