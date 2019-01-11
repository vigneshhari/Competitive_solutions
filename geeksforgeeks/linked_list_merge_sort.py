

class ll:

    next = None

    def __init__(self,val):
        self.val = val

    def setnext(self,next):
        self.next = next


def stringll(node):
    if(node == None):return ""
    return str(node.val) + " " + stringll(node.next)


head = ll(-1)
looper = head
for i in range(input()):
    temp = ll(input())
    looper.setnext(temp)
    looper = looper.next

print stringll(head)
