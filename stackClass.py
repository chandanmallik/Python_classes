class stack():
    def __init__(self):
        self.__myList= []
    def push(self,val):
        self.__myList.append(val)
        print(f"{val} is been added to stack {self.__myList} ")
    def pop(self):
        print(f"{self.__myList[-1]}  has been poped out")
        del self.__myList[-1]
        print(self.__myList)

obj_stack = stack()  #creating a obj of class
obj_stack.push(4)
obj_stack.push(3)
obj_stack.push(1)
obj_stack.push(8)
obj_stack.pop()
