def isBalanced(parentheses):

    utilStack = []

    for char in parentheses:

        if char in ["(", "{", "["]:
            utilStack.append(char)
        
        # if the character in input is an open bracket, then we push it into the stack
        
        else:
            if not utilStack:
                return False
            # if stack is already empty then no pop can occur, so false
            
            current_char = utilStack.pop()
            if current_char == '(':
                if char != ")":
                    return False
            if current_char == '{':
                if char != "}":
                    return False
            if current_char == '[':
                if char != "]":
                    return False
            # if the current character is not the closing bracket for the one popped from the stack, then again it is unbalanced
            
    if utilStack:
        return False
    # if at the end of all input, the stack is not empty, then the input was unbalanced

    return True

if __name__ == "__main__":

    parentheses = input("'enter the string of parentheses")

    if isBalanced(parentheses):
        print("string is Balanced")
    else:
        print("string is Not Balanced")
 
