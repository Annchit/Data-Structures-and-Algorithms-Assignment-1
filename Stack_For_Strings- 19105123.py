mainStack=[]
top=None

def isEmpty(tempStack):
    if(tempStack==[]):
        return True
    else:
        return False
    
# isEmpty - checks if the stack is empty or not

def getSize(tempStack):
    return len(tempStack)

# getSize - returns the size of the stack
    
def push(tempStack, entity):
    global top
    tempStack.append(entity)
    top=len(tempStack)-1
    
# push - pushes another character into the stack
    
def pop(tempStack):
    global top
    if(isEmpty(tempStack)):
        return('underflow')
    else:
        i=tempStack.pop()
        if (len(tempStack)==0):
            top=None
        else:
            top=top-1
    return i

# pop - takes out the topmost element from the stack and if the stack is already empty then informs about the underflow

def peek(tempStack):
    if(isEmpty(tempStack)):
        return('underflow')
    else:
        top=len(tempStack)-1
        return tempStack[top]
    
# peek - returns the topmost element of the stack

def display(tempStack):
    if(isEmpty(tempStack)):
        print('Heyy! Stack is empty!')
    else:
        top=len(tempStack)-1
        print(tempStack[top],'<-- top')
        
        for i in range(top-1,-1,-1):
            print(tempStack[i])
            
# display - prints all the elements of the stack
            
while True:
    print('Implementation of Stack')
    print('1. Push')
    print('2. Pop')
    print('3. Peek')
    print('4. Display')
    print('5. Size')
    print('6. Exit')
    
    choice=int(input('Enter a choice (1-6)'))
    
    if(choice==1):
        entity=(input('Enter the entity that you want to push:'))
        push(mainStack,entity)
        print('\n')
        print('%s added successfully...' %entity)
    
    elif(choice==2):
        entity =pop(mainStack)
        if (entity=='underflow'):
            print('stack already empty...')
        else:
            print('\n')
            print('%s is popped' %entity)            
            
    elif(choice==3):
        entity =peek(mainStack)
        if (entity=='underflow'):
            print('stack already empty...')
        else:
            print('\n')
            print('%s is at the top' %entity)
     
    elif(choice==4):
        print('\n')
        display(mainStack)
        
    elif(choice==5):
        entity = getSize(mainStack)
        print('\n')
        print('%s is the size of the stack ' %entity)
   
    elif(choice==6):
        break
        
    else:
        print('\n')
        print('Invalid option')
        
    print('\n\n')
