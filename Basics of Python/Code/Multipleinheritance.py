#Multiple inheritance means one child class can inherit from multiple parent classes.
class A:
    def method_A(self):
        print("method call from A")
class B:
    def method_B(self):
        print("method call from B")
class C(A,B):
    def method_C(self):
        print("method call from C") 
test_object = C()
test_object.method_A()  # Calling method from class A
test_object.method_B()  # Calling method from class B
test_object.method_C()  # Calling method from class C