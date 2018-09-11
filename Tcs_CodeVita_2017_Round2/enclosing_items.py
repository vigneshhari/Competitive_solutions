symb = ["(", ")", "{", "}" ,"[" ,"]" ,"<" ,">", "/","\\"]
open_tag = ["(", "{" ,"[" ,"<" , "/"]
close_tag = [ ")", "}" ,"]" ,">" ,"\\"]

dic_sym = { ")" : "(" , "}" : "{" , "]" : "[" , ">" : "<" , "\\" : "/" }    

times = input()
while times:
    data = raw_input()
    string = ""
    inside = 0
    for i in range(0,len(data)):
        try:
            if(data[i] == "@" and data[i+1] == "*"):inside+=1
            if(data[i] == "*" and data[i+1] == "@"):inside-=1
        except: 
            pass
        if inside == 0 and data[i] in symb : string = string + data[i]
    out = "True"
    tags = [""]
    for i in string:
        if i in open_tag:
            tags.append(i)
        elif i in close_tag:
            rev = dic_sym.get(i)
            if(rev == tags[-1] and len(tags) > 0):del tags[-1]
            else: out = "False"
    if len(tags) > 1: out = "False"
    print out
    times-=1