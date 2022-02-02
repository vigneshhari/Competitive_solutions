package main

func romanToInt(s string) int {
	integerVal := 0
	previous := '-'
	for _, char := range s {
		switch char {
		case 'I':
			{
				integerVal += 1
			}
		case 'V':
			{
				if previous == 'I' {
					integerVal -= 2
				}
				integerVal += 5
			}
		case 'X':
			{
				if previous == 'I' {
					integerVal -= 2
				}
				integerVal += 10
			}
		case 'L':
			{
				if previous == 'X' {
					integerVal -= 20
				}
				integerVal += 50
			}
		case 'C':
			{
				if previous == 'X' {
					integerVal -= 20
				}
				integerVal += 100
			}
		case 'D':
			{
				if previous == 'C' {
					integerVal -= 200
				}
				integerVal += 500
			}
		case 'M':
			{
				if previous == 'C' {
					integerVal -= 200
				}
				integerVal += 1000
			}
		}
		previous = char
	}
	return integerVal
}

func main() {
	print(romanToInt("MCMXCIV"))
}
