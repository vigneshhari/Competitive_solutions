package main

func guess(num int) int { // Faking judge
	value := 1 // Update Value here
	if num == value {
		return 0
	} else if num > value {
		return -1
	}
	return 1
}

func guessNumber(n int) int {
	lValue := 0
	rValue := n
	for lValue <= rValue {
		currentValue := (lValue + rValue) / 2
		guessOutput := guess(currentValue)
		if guessOutput == 1 {
			lValue = currentValue + 1
		} else if guessOutput == -1 {
			rValue = currentValue - 1
		} else {
			return currentValue
		}
	}
	return -1
}

func main() {
	print(guessNumber(1))
}
