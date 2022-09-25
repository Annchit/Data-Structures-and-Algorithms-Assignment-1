def isBalanced(parentheses):

    utilStack = []

    for char in parentheses:

        if char in ["(", "{", "["]:
            utilStack.append(char)
        
        else:
            if not utilStack:
                return False
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

    if utilStack:
        return False

    return True

if __name__ == "__main__":

    parentheses = input("'enter the string of parentheses")

    if isBalanced(parentheses):
        print("string is Balanced")
    else:
        print("string is Not Balanced")
 