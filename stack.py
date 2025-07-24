# #Q1. Valid Parantheses
class Solution:
    def isValid(self,s):
        stack=[]
        mapping={')':'(', ']':'[', '}':'{'}
        for char in s:
            if char in mapping.values():
                stack.append(char)

            elif char in mapping:
                if not stack or stack[-1]!=mapping[char]:
                    return False
                stack.pop()
        return not stack
sol=Solution()
s = "[]"
print(sol.isValid(s))
s1="([{}])"
print(sol.isValid(s1))
s2 = "[(])"
print(sol.isValid(s2))

#Q2. Min stack
class MinStack:
    def __init__(self):
        self.main_stack=[]
        self.min_stack=[]
    
    def push(self,val):
        self.main_stack.append(val)
        if not self.min_stack or val<=self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        if self.main_stack:
            val=self.main_stack.pop()
            if val==self.min_stack[-1]:
                self.min_stack.pop()
    
    def top(self):
        if self.main_stack:
            return self.main_stack[-1]
        
    def getMin(self):
        if self.min_stack:
            return self.min_stack[-1]

ops=["MinStack", "push", 1, "push", 2, "push", 0, "getMin", "pop", "top", "getMin"]
args = [[], [1], [2], [0], [], [], [], []]

output = []
stack=None
arg_index = 0

for i in range(len(ops)):
    op = ops[i]
    if op == "MinStack":
        stack = MinStack()
        output.append(None)
    elif op == "push":
        val = args[arg_index][0]
        stack.push(val)
        output.append(None)
        arg_index += 1
    elif op == "pop":
        stack.pop()
        output.append(None)
    elif op == "top":
        output.append(stack.top())
    elif op == "getMin":
        output.append(stack.getMin())

print(output)

#Q3. Reverse Polish Notation
class Solution():
    def evalRPN(self,tokens):
        stack=[]
        for token in tokens:
            if token in '+-/*':
                b=stack.pop()
                a=stack.pop()
                if token == '+':
                    stack.append(a+b)
                elif token=='-':
                    stack.append(a-b)
                elif token=='*':
                    stack.append(a*b)
                elif token=='/':
                    stack.append(int(a/b))
            else:
                stack.append(int(token))
        return stack[0]
    
sol=Solution()
tokens = ["1","2","+","3","*","4","-"]
print(sol.evalRPN(tokens))

#Q4. Generate Parenthesis
class Solution:
    def generateParenthesis(self, n):
        result=[]
        def backtrack(current,open_count,close_count):
            if len(current)==2*n:
                result.append(current)
                return
            if open_count<n:
                backtrack(current+"(",open_count+1,close_count)
            if close_count<open_count:
                backtrack(current+")",open_count,close_count+1)

        backtrack("",0,0)
        return result
    
if __name__ == "__main__":
    try:
        n = int(input("Enter the number of pairs of parentheses (n): "))
        sol = Solution()
        combinations = sol.generateParenthesis(n)
        print("All valid combinations:")
        for combo in combinations:
            print(combo)
    except ValueError:
        print("Please enter a valid integer.")

#Q5. Daily temperatures
class Solution:
    def dailyTemperatures(self,temperatures):
        n=len(temperatures)
        result=[0]*n
        stack=[]
        for i in range(n):
            while stack and temperatures[i]>temperatures[stack[-1]]:
                prev_day=stack.pop()
                result[prev_day]=i-prev_day
            stack.append(i)
        return result
    
temperatures = [22,21,20]
sol=Solution()
print(sol.dailyTemperatures(temperatures))

#Q6. Car fleet
class Solution:
    def carFleet(self,target,position,speed):
        cars=sorted(zip(position,speed), reverse=True)
        stack=[]
        for pos,spd in cars:
            time=(target-pos)/spd
            if not stack or time>stack[-1]:
                stack.append(time)
        
        return len(stack)
sol=Solution()
target = 10
position = [1,4]
speed = [3,2]
print(sol.carFleet(target,position,speed))l