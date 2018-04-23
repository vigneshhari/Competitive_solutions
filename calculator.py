#using python 3
#This Code is Obsolete now
import math

class Calc_num:
    def __init__(self):
        self.oper = []
    def convert(self,inputs):
        _1 = str(inputs).split();z=0;listindex = 0;i=0
        temper = ''.join(_1)
        print(temper)
        self.oper = [None] * (int(temper.__len__()) )
        while(temper.__len__() > i):
            if(if_func(temper[i])):
                self.oper[listindex] = temper[i:(i+3)]
                z = i
                listindex += 1
                i=i+3
            if(if_operand(temper[i])):
                if(temper[i] == '('):
                    i+=1
                    self.oper[listindex] = '('
                    listindex += 1
                    z=i
                    continue
                if(temper[i] == ')'):
                    i+=1
                    if(temper[z:i-1] != ''):
                          self.oper[listindex] = temper[z:i-1]
                          listindex += 1
                    self.oper[listindex] = ')'
                    listindex += 1
                    z = i+1
                    continue
                if(temper[z:i] != ''):
                   self.oper[listindex] = temper[z:i]
                   listindex = listindex + 1
                self.oper[listindex] = temper[i];z = i+1
                listindex =  listindex + 1
            self.oper[listindex] = temper[z:i+1]
            i = i + 1
        print(self.oper)

def if_operand(lest):
        operands  = ['+','-','*','/','^','(',')']
        for opers in operands:
            if(lest == opers):return True
        return False

def if_func(num):
        num = str(num)
        funcs = ['tan','cos','sin','sqt','log']
        for fun in funcs:
            if(num[0] == fun[0] ): return True
        return False

def calculates(a,b,sign):
    a = int(a);b = int(b)
    if(sign == '*'): return (a * b)
    elif(sign == '-'): return (a - b)
    elif(sign == '+'): return (a + b)
    elif(sign == '/'): return (a / b)
    elif(sign == '^'): return int(math.pow(a,b))

def funcs(a,fun):
    a = int(a)
    if(fun == 'sin'): return math.sin(a)
    if(fun == 'cos'): return math.cos(a)
    if(fun == 'tan'): return math.tan(a)
    if(fun == 'log'): return math.log10(a)
    if(fun == 'sqt'): return math.sqrt(a)



def Actual_Calculator(test,vi):
    test.convert(vi);
    i = 0;popper =0
    while True:
        if(i > test.oper.__len__() - 1): break
        if(test.oper[i] == '('):
            pass
            '''
            end = 0 ; parent = 0
            parent += 1
            elif(test.oper[end] == ')'):parent -= 1
            if(parent == 0 ): break
            end +=1;
            '''
        if(if_func(test.oper[i])):
              end = i+1;
              start = i ;parent = 0
              while(True):
                  if(test.oper[end] == '('):parent += 1
                  elif(test.oper[end] == ')'):parent -= 1
                  if(parent == 0 ): break
                  end +=1;
              sub = Calc_num()
              ans = Actual_Calculator(sub,''.join(test.oper[(i+2):end]))
              final = funcs(ans,test.oper[i])
              del test.oper[i+1:end+1]
              test.oper[i] = final
        vals = 0
        if(if_operand(test.oper[i])):
              vals = calculates(test.oper[i-1],test.oper[i+1],str(test.oper[i]))
              test.oper.pop(popper);
              popper = popper +1
              test.oper.pop(popper)
              popper = 0
              test.oper[0] = vals
              i = 0
        i += 1
    return float(vals)

test = Calc_num();
vi = raw_input("Enter the Calculation String" + '\n')
ans = Actual_Calculator(test,vi)
print(ans)