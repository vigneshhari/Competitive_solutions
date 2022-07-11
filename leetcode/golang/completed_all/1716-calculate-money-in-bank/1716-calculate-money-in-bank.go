package main

func totalMoney(n int) int {
	weeks := n / 7 // Golang rounds down for us
	sum := weeks * 28
	rem := n - (weeks * 7)                             // Gets the number of days from the last complete week
	sum += ((weeks - 1) * (7 + (7 * (weeks - 1)))) / 2 // 7 + 14 + 21 + ...
	sum += (rem * (rem + 1) / 2) + (weeks * rem)       // Calculate remaining amount with the extra
	return sum
}

func main() {
	print(totalMoney(20))
}
