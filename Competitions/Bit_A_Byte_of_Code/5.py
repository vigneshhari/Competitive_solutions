def minion_game(st):
    vowels = ["A" , "E" , "I" , "O" , "U"]

    stuart = 0
    kevin = 0



    for i in range(0, len(st)+1):
        temp_list = []
        for k in range(0,len(st) - i+1 ):
            if(st[k:k+i] in temp_list):continue
            temp_list.append(st[k:k+i])
            if(st[k] in vowels):
                kevin+= st.count(st[k:k+i])
            else:
                print st.count(st[k:k+i]) , st[k:k+i]
                stuart+= st.count(st[k:k+i])

    stuart = stuart - (len(st) + 1 )

    if(stuart > kevin):
        print "Stuart {}".format(stuart)
    elif(kevin > stuart):
        print "Kevin {}".format(kevin)
    else:
        print "Draw"

minion_game("BANANA")
