//This is a merge sort implementation

package main

import (
	"fmt"
	_ "math/rand"
	_ "time"
)


func merge(nums [] int , start , end int) {

	middle :=  ((start + end ) / 2 )
	var tempList = make([]int,end - start + 1)
	tempListPos := 0
	lpointer := start
	rpointer := middle + 1
	for lpointer <= middle && rpointer <= end {
		if(nums[lpointer] < nums[rpointer]){
		tempList[tempListPos] = nums[lpointer]
		lpointer++;tempListPos++;
		} else{
			tempList[tempListPos] = nums[rpointer]
			rpointer++;tempListPos++;
		}
	}
	for (lpointer <= middle  ){
			tempList[tempListPos] = nums[lpointer]
			lpointer++;tempListPos++;
	}
	for (rpointer <= end ){
			tempList[tempListPos] = nums[rpointer]
			rpointer++;tempListPos++;
	}
	i := 0
	for( i<tempListPos ){
		nums[start+i] = tempList[i]
		i++;
	}
}

func mergeSort(nums []int , start , end int ) { // Start and end inclusive
	middle :=  (start + end ) / 2
	if(start == end){return}
	if(end - start == 1){merge(nums,start,end) ; return}
	mergeSort(nums , start , middle)
	mergeSort(nums , middle + 1 , end  )
	merge(nums , start , end )
}

func sortArray(nums []int) []int {
	mergeSort(nums , 0 , len(nums) - 1)
	return nums
}

func main(){

	arr := []int{5,0,0}
	fmt.Println(sortArray(arr))

}