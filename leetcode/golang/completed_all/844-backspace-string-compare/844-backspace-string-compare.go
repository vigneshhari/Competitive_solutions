package main

import "fmt"

func stringProcessor(s string) string {
	output := ""
	for _, j := range s {
		if j == '#' {
			if output != "" {
				output = output[:len(output)-1]
			}
			continue
		}
		output += string(j)
	}
	return output
}

func backspaceCompare(s string, t string) bool {
	s_processed := stringProcessor(s)
	t_processed := stringProcessor(t)
	return s_processed == t_processed
}

func main() {

	fmt.Print("Comparison resulted in ", backspaceCompare("ab##", "ba##a"))
}
