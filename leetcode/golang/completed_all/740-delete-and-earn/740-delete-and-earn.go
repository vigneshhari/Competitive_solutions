package main

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func deleteAndEarn(nums []int) int {
	var scores [10002]int
	previous, currrent := 0, 0

	for _, val := range nums {
		scores[val] += val
	}
	for _, num := range scores {
		previous, currrent = currrent, max(currrent, previous+num)
	}
	return currrent
}

func main() {
	print(deleteAndEarn([]int{3, 7, 10, 5, 2, 4, 8, 9, 9, 4, 9, 2, 6, 4, 6, 5, 4, 7, 6, 10}))
}
