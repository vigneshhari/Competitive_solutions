package main

import "fmt"

func twoSum(numbers []int, target int) []int {
	startPointer, endPointer := 0, len(numbers)-1
	for startPointer < endPointer {
		sum := numbers[startPointer] + numbers[endPointer]
		if sum == target {
			return []int{startPointer + 1, endPointer + 1}
		} else if sum > target {
			endPointer--
		} else {
			startPointer++
		}
	}
	return []int{-1, -1}
}

func main() {
	fmt.Println("The result of two sum is :", twoSum([]int{2, 7, 11, 15}, 9))
}
