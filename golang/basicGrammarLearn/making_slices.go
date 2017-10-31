package main

import "fmt"

/*
a := make([]int, 5)  // len(a)=5
b := make([]int, 0, 5) // len(b)=0, cap(b)=5
b = b[:cap(b)] // len(b)=5, cap(b)=5
b = b[1:]      // len(b)=4, cap(b)=4

根据官方文档的解释：
	func cap(v Type) int
The cap built-in function returns the capacity of v, according to its type:
	Array: the number of elements in v (same as len(v)).
	Pointer to array: the number of elements in *v (same as len(v)).
	Slice: the maximum length the slice can reach when resliced;
	if v is nil, cap(v) is zero.
	Channel: the channel buffer capacity, in units of elements;
	if v is nil, cap(v) is zero.
*/

func main() {
	//初始化的时候，默认为0，cap为5，则a=[0 0 0 0 0]
	a := make([]int, 5)
	printSlice("a", a)
	//指定了b的长度为0，即b为空，cap为5，所以b=[]
	b := make([]int, 0, 5)
	printSlice("b", b)
	//定义c时，c的空间大小与b相同，由于初始值为0，所以取前两个值，长度为2，c=[0 0]
	c := b[:2]
	printSlice("c", c)
	//定义d时，d的空间大小为d的最大长度，由于初始值为0，所以取前三个值，长度为3，d=[0 0 0]
	d := c[2:5]
	printSlice("d", d)
}

func printSlice(s string, x []int) {
	fmt.Printf("%s len=%d cap=%d %v\n",
		s, len(x), cap(x), x)
}

/*
a len=5 cap=5 [0 0 0 0 0]
b len=0 cap=5 []
c len=2 cap=5 [0 0]
d len=3 cap=3 [0 0 0]
*/
