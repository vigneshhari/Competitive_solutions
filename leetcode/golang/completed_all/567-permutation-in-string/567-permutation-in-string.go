package main

//func checkInclusion(s1 string, s2 string) bool {
//	mapper := make(map[int32]int)
//	for _, j := range s1 {
//		mapper[j]++
//	}
//	tempMapper := make(map[int32]int)
//	completed := 0
//	pos := 0
//	for i, j := range s2 {
//		val, ok := mapper[j]
//		currentVal, _ := tempMapper[j]
//		tempMapper[j]++
//		currentVal++
//		if currentVal == val {
//			completed++
//			if completed == len(mapper) {
//				fmt.Println(string(j), completed, len(mapper))
//				return true
//			}
//		} else if !ok {
//			pos = i + 1
//			completed = 0
//			tempMapper = make(map[int32]int)
//		} else if currentVal > val {
//			v, o := tempMapper[int32(s2[i])]
//		}
//	}
//	return false
//}

func main() {
	//fmt.Println("Can there be a substring with a permutation of s1? : ", checkInclusion("adc", "dcda"))
}
