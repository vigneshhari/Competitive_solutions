package main

func sumOfUnique(nums []int) int {
	var check = map[int]bool{}
	sum := 0
	for _, v := range nums {
		val, ok := check[v]
		if !ok {
			sum += v
			check[v] = false
		} else if !val {
			check[v] = true
			sum -= v
		}
	}
	return sum
}

func main() {

	print(sumOfUnique([]int{1, 2, 2, 3, 3, 4}))
}
