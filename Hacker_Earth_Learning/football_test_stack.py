times = input()
while times:
    num,top = raw_input().split(" ")
    num = int(num)
    stack = [top]
    while num:
        current = raw_input()
        if(current[0] == "P"):
            stack.append(current[2:])
            before = top
            top = current[2:]
        else:
            stack.append(stack[-2])
        num-=1
    print "Player" , stack.pop()
    times-=1

'''
    Electronics Workshop - The Students of my college were slowly shifting to just learning the theory side. we conducted a hands on electronics workshop with online prototyping tools ( So that no cost will be there and its safe ) so that the students can actually try out what they wanted. I Took the Entire Session. 

ISQIP'17 - The IEEE Student Quality Improvement Program is an 8 day event that brought industry experts to teach the basics of different types of development and advanced hands on workshops on various fields . This was followed by an  internship Drive that helped many students find a place for their projects


Hall of Code

10 students were selected from various branches and were trained on a unique subject (Including Programming languages and New Technologies) and after two weeks of training we set up stalls in a room for each subject they chose . College students were brought to these rooms and they visited the booths they wanted and gained information on that unique subject . 
The Students were taught the basics of the Following -
Ruby,Python,Java,C++,C,Php,Html,Css,JavaScript,Django,Opencv,Android Programming and Machine learning.
Such large topics were covered within a day because the students were able to share their learning experience with their colleagues and learn together. The overall participation rose upto 60. It helped students get a basic understanding of various fields of development and understand what is best for them currently. since a lot of options were given to the students they could find the ones which they found interesting and could work on that. After "Hall of Code" Interested students formed a Developer Community and is working on Various Projects now 


'''