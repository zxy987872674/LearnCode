package main

import (
	"fmt"
)

type ErrNegativeSqrt float64

func (e ErrNegativeSqrt) Error() string {
	return fmt.Sprintf("can't Sqrt negative number: %v", float64(e))
}

func Sqrt(f float64) (float64, error) {
	if f < 0 {
		return 0, ErrNegativeSqrt(f)
	}
	z := f
	for i := 0; i < 10; i++ {
		z = (z + f/z) / 2
	}
	return z, nil
}

func main() {
	if value, err := Sqrt(2); err != nil {
		fmt.Println(err)
	} else {
		fmt.Println(value)
	}
	if value, err := Sqrt(-2); err != nil {
		fmt.Println(err)
	} else {
		fmt.Println(value)
	}

}
