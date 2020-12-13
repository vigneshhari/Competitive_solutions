'''
# Solution 1
for i in range(input()):
    inp = raw_input()
    trie = {}
    uniq_char_list = []
    temp = trie
    for i in range(0,len(inp)):
        if(inp[i] not in uniq_char_list):
            temp[ inp[i] ] = {}
            temp = temp[inp[i]]
            uniq_char_list.append(inp[i])
        else:
            temp['fo'] = 1
            temp_trie = trie
            faulty = False
            for k in range(i + 1 , len(inp)):
                if(temp_trie.get( inp[k] , -1 ) == -1 and temp_trie.get( 'fo' , -1 ) == 1 ):temp_trie = trie
                if(temp_trie.get( inp[k] , -1 ) == -1):
                    if(temp_trie.get( 'fo' , -1 ) == -1):
                        faulty = True
                        break
                    else:
                        temp_trie = trie
                temp_trie = temp_trie[ inp[k] ]
            if( faulty == False):
                print trie
'''

# Solution 2

for _ in xrange(input()):
    inp = raw_input()
    length = len(inp)
    for i in xrange(1,length):
        if(i == length -1 ):
            if(inp[-1] == inp[0]):print length - 1 ; break
            print length;break
        if( inp[i]  == inp[0] ):
            for k in xrange(i,length):
                if(inp[k-i] != inp[k] ):
                    break
            if(k == length -1):
                print i
                break
