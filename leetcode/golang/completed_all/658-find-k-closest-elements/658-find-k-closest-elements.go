package main

import (
	"fmt"
)

func abs(a int) int {
	if a < 0 {return a * -1}
	return a
}

func findClosest(arr []int , x int) int{
	closestIndex := 0
	closestValue := abs(arr[0] - x)
	for index , val := range(arr){
		currentValue := abs(val - x)
		if(currentValue < closestValue){
			closestValue = currentValue
			closestIndex = index
		}
	}
	return  closestIndex
}

func findClosestElements(arr []int, k int, x int) []int {

	currentIndex := findClosest(arr,x)
	leftPointer := currentIndex
	rightPointer := currentIndex

	counter := 1
	for counter < k {
		counter += 1
		if(leftPointer <= 0 ){
			rightPointer += 1
			continue
		}
		if(rightPointer >= len(arr) -1){
			leftPointer -=1
			continue
		}
		if(abs(arr[leftPointer -1] - x) <= abs(arr[rightPointer + 1] - x)) {
			leftPointer -= 1
		}else{
			rightPointer+=1
		}
	}
	return arr[leftPointer:rightPointer+1]
}

func main(){
	fmt.Println(findClosestElements( []int{1,2,3,4,5} , 2, 3 ))
}