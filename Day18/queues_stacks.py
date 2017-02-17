import sys

class Solution:
    # Write your code here
    def __init__(self):
        self.stack = []
        self.queue = []
    
    def pushCharacter(self, char):
        self.stack.insert(0, char)
        
    def popCharacter(self):
        ans = self.stack[0]
        self.stack.pop(0)
        return ans
    
    def enqueueCharacter(self, char):
        self.queue.append(char)
        
    def dequeueCharacter(self):
        ans = self.queue[0]
        self.queue.pop(0)
        return ans


