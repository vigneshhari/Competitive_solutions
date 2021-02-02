package main

import (
	"fmt"
)

var alphabetList = []string{"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"}

func createHashMap(wordList []string) map[string]bool  {
	wordPresent := make(map[string]bool)
	for _ , word := range wordList {
		wordPresent[word] = true
	}
	return wordPresent
}

func createAutomata(beginWord string, wordList []string) map[string]map[string]bool {
	wordMap := make(map[string]map[string]bool)
	wordPresent := createHashMap(wordList)
	wordList = append(wordList, beginWord)
	for _ , word := range wordList {
		for index:= 0 ; index < len(beginWord) ; index++ {
			for _ , letter := range alphabetList {
				newWord := word
				newWord = newWord[:index] + letter + newWord[index+1:]
				if _, ok := wordPresent[newWord]; ok && newWord != word {
					if wordMap[word] == nil {wordMap[word] = make(map[string]bool)}
					wordMap[word][newWord] = true
				}
			}
		}
	}
	return wordMap
}

func BFS( current string ,target string, graph map[string]map[string]bool   )[][]string {
	var wordTravel,queue [][]string
	visited := make(map[string]int)
	queue = append(queue , []string{current})
	for len(queue) > 0 {
		currentPath := queue[0]
		lastNode := currentPath[len(currentPath)-1]
		queue = queue[1:]
		visitedLength , visitedBefore := visited[lastNode]
		if(visitedBefore){if(visitedLength < len(currentPath)){continue}}
		visited[lastNode] = len(currentPath)
		if(lastNode == target){
			wordTravel=append(wordTravel,currentPath);
			continue }
		if(graph[lastNode] == nil ){continue}
		for word := range graph[lastNode] {
			var temp []string ;
			temp = append(currentPath,word)
			_copy := append(temp[:0:0], temp...)
			queue = append(queue , _copy )
		}
	}
	return wordTravel
}


func findLadders(beginWord string, endWord string, wordList []string) [][]string {
	graph := createAutomata(beginWord , wordList)
	possibleRoutes := BFS(beginWord , endWord  , graph )
	return possibleRoutes
}

func main(){
	wordlist := []string{"kid","tag","pup","ail","tun","woo","erg","luz","brr","gay","sip","kay","per","val","mes","ohs","now","boa","cet","pal","bar","die","war","hay","eco","pub","lob","rue","fry","lit","rex","jan","cot","bid","ali","pay","col","gum","ger","row","won","dan","rum","fad","tut","sag","yip","sui","ark","has","zip","fez","own","ump","dis","ads","max","jaw","out","btu","ana","gap","cry","led","abe","box","ore","pig","fie","toy","fat","cal","lie","noh","sew","ono","tam","flu","mgm","ply","awe","pry","tit","tie","yet","too","tax","jim","san","pan","map","ski","ova","wed","non","wac","nut","why","bye","lye","oct","old","fin","feb","chi","sap","owl","log","tod","dot","bow","fob","for","joe","ivy","fan","age","fax","hip","jib","mel","hus","sob","ifs","tab","ara","dab","jag","jar","arm","lot","tom","sax","tex","yum","pei","wen","wry","ire","irk","far","mew","wit","doe","gas","rte","ian","pot","ask","wag","hag","amy","nag","ron","soy","gin","don","tug","fay","vic","boo","nam","ave","buy","sop","but","orb","fen","paw","his","sub","bob","yea","oft","inn","rod","yam","pew","web","hod","hun","gyp","wei","wis","rob","gad","pie","mon","dog","bib","rub","ere","dig","era","cat","fox","bee","mod","day","apr","vie","nev","jam","pam","new","aye","ani","and","ibm","yap","can","pyx","tar","kin","fog","hum","pip","cup","dye","lyx","jog","nun","par","wan","fey","bus","oak","bad","ats","set","qom","vat","eat","pus","rev","axe","ion","six","ila","lao","mom","mas","pro","few","opt","poe","art","ash","oar","cap","lop","may","shy","rid","bat","sum","rim","fee","bmw","sky","maj","hue","thy","ava","rap","den","fla","auk","cox","ibo","hey","saw","vim","sec","ltd","you","its","tat","dew","eva","tog","ram","let","see","zit","maw","nix","ate","gig","rep","owe","ind","hog","eve","sam","zoo","any","dow","cod","bed","vet","ham","sis","hex","via","fir","nod","mao","aug","mum","hoe","bah","hal","keg","hew","zed","tow","gog","ass","dem","who","bet","gos","son","ear","spy","kit","boy","due","sen","oaf","mix","hep","fur","ada","bin","nil","mia","ewe","hit","fix","sad","rib","eye","hop","haw","wax","mid","tad","ken","wad","rye","pap","bog","gut","ito","woe","our","ado","sin","mad","ray","hon","roy","dip","hen","iva","lug","asp","hui","yak","bay","poi","yep","bun","try","lad","elm","nat","wyo","gym","dug","toe","dee","wig","sly","rip","geo","cog","pas","zen","odd","nan","lay","pod","fit","hem","joy","bum","rio","yon","dec","leg","put","sue","dim","pet","yaw","nub","bit","bur","sid","sun","oil","red","doc","moe","caw","eel","dix","cub","end","gem","off","yew","hug","pop","tub","sgt","lid","pun","ton","sol","din","yup","jab","pea","bug","gag","mil","jig","hub","low","did","tin","get","gte","sox","lei","mig","fig","lon","use","ban","flo","nov","jut","bag","mir","sty","lap","two","ins","con","ant","net","tux","ode","stu","mug","cad","nap","gun","fop","tot","sow","sal","sic","ted","wot","del","imp","cob","way","ann","tan","mci","job","wet","ism","err","him","all","pad","hah","hie","aim","ike","jed","ego","mac","baa","min","com","ill","was","cab","ago","ina","big","ilk","gal","tap","duh","ola","ran","lab","top","gob","hot","ora","tia","kip","han","met","hut","she","sac","fed","goo","tee","ell","not","act","gil","rut","ala","ape","rig","cid","god","duo","lin","aid","gel","awl","lag","elf","liz","ref","aha","fib","oho","tho","her","nor","ace","adz","fun","ned","coo","win","tao","coy","van","man","pit","guy","foe","hid","mai","sup","jay","hob","mow","jot","are","pol","arc","lax","aft","alb","len","air","pug","pox","vow","got","meg","zoe","amp","ale","bud","gee","pin","dun","pat","ten","mob"}
	fmt.Println(findLadders("cet" , "ism" , wordlist))
	//wordlist := []string{"ted","tex","red","tax","tad","den","rex","pee"}
	//fmt.Println(findLadders("red" , "tax" , wordlist))

	//wordlist := []string{"hot","dot","dog","pet","mwt","wer","ver" ,"cet" ,"cem","lot","log","cog"}
	//fmt.Println(findLadders("hit" , "cog" , wordlist))
	//[[inn ins its ito ibo ibm ism]]
}
