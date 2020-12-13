class Trie:
    def __init__(self):
        self.root = {}
        self.midmarker = "^"
        self.endmarker = "$"

    def AddWord(self,word):
        temp = self.root
        for i in word:
            if(self.endmarker in temp.keys()):return 1
            try:
                _ = temp[i]
            except:
                temp[i] = {} 
            temp[self.midmarker] = temp.get(self.midmarker,0)
            temp = temp[i] 
        if(self.midmarker in temp.keys() ):return 1
        if(self.endmarker in temp.keys() ):return 1

        temp[self.endmarker] = temp.get(self.endmarker,0) 
        return 0


    def FindLike(self,word):
        temp = self.root
        for i in word:
            try:
                temp = temp[i]
            except:
                return 0
        if("$" not in temp.keys()):return 0
        return temp["$"]

trie = Trie()
done = 1
failed = ""
for _ in range(input()):
    val = raw_input()
    if( done):
        if(trie.AddWord(val)):
            done = 0
            failed = val
if(done):
    print "GOOD SET"
else:
    print "BAD SET"
    print failed