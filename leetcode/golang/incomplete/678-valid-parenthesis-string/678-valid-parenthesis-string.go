package main;

func checkValidString(s string) bool {
	status := 0
	lifelines := 0
	simLifeLine := 0
	var lastChar int32
	for _ , char := range(s){
		if(char == 40 ){
			simLifeLine = 0
			status+=1
		} else if(char == 41){
			simLifeLine = 0
			if(status > 0){status-=1
			} else if (lifelines > 0){
				lifelines -=1
			} else {
				return false
			}
		} else {
			if(simLifeLine == 0){simLifeLine+=1}
			lifelines+=1
		if(lastChar == char){
			simLifeLine +=1
		}}
	lastChar = char
	}
	if(simLifeLine >= status){return true}
	return status==0
}

func main(){
	print(checkValidString("((*)(*))((**"))
}