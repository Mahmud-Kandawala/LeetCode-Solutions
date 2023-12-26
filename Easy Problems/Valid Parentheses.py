class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] # Stack is used as a stack data structure to keep track of the opening brackets ('(', '[', '{'). Stacks are LIFO (Last In, First Out) structures, meaning the last element added is the first one to be removed.
        closeToOpen = {")" : "(", "]" : "[", "}" : "{" } # Maps each type of closing bracket to its corresponding opening bracket. 

        for char in s: # Iterates over each character 'char' in the string 's'. Each character is examined to determine whether it's an opening or closing bracket.
            if char in closeToOpen: # Checks if the current character is a closing bracket (i.e., one of the keys in the closeToOpen).
                if stack and stack[-1] == closeToOpen[char]: # Checks if the stack is not empty and checks whether the bracket at the top of the stack is the matching opening bracket 
                    stack.pop() # Removes the last opening bracket from the stack
                else:
                    return False
            else:
                stack.append(char) # If the current character is not a closing bracket, it's treated as an opening bracket and is added to the stack. This is for later matching with a corresponding closing bracket.
        return True if not stack else False # After processing all characters in the string, this line is executed. True if the stack is empty, indicating that all opening brackets have been properly matched with closing brackets. False, if the stack is not empty, it means there are unmatched opening brackets left
            

        
