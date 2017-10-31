package main

import "fmt"

//结构体，相当于变量的集合
type Vertex struct {
	X int
	Y int
}

func main() {
	fmt.Println(Vertex{1, 2})
}
