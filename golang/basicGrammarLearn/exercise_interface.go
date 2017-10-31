package main

import "fmt"

type People interface {
	say()
}

type Men struct {
	name string
}

func (men *Men) say() {
	fmt.Println("mem say hi:", men.name)
}

func main() {
	m := &Men{"mike"}
	m.say()

	m2 := new(Men)
	m2.name = "new men"

	var p People
	p = m2
	p.say()
}
