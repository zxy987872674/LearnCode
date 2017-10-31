package main

import "fmt"

func main() {
	m := make(map[string]int)
	//Insert an element in map m
	m["Answer"] = 42
	fmt.Println("The value:", m["Answer"])
	//Update an element in map m
	m["Answer"] = 48
	fmt.Println("The value:", m["Answer"])
	//Delete an element in map m
	delete(m, "Answer")
	fmt.Println("The value:", m["Answer"])
	//If key is in m, ok is true. If not, ok is false and elem is the zero value for the map's element type
	v, ok := m["Answer"]
	fmt.Println("The value:", v, "Present?", ok)
}
