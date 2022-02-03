for i in range(0,input()):
    data = raw_input().split("IEM")
    while("".join(data) != "".join("".join(data).split("IEM"))):
        data = "".join(data).split("IEM")
    if("".join(data).strip() == ""):
        print "Yes"
    else:
        print "No"
