class A:
    def __init__(self,a):
        self.a=a 
    def __lt__(self,other):
        if self.a<other.a:
            print("Object 1 is less than object two!")
        else:
            print("Object 1 is greater than object 2")
    def __eq__(self,other):
        if (self.a==other.a):
            print("The two values are equal!")
        else:
            print("The two objects are not equal")
obj1=A(2)
obj2=A(4)
print("Passed value:")
print(obj1<obj2)

obj3=A(5)
obj4=A(5)
print(obj3==obj4)