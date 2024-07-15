#Compile-time  method-over loading 
#Same class, same method names with different parameters

class A:
    def sum(self,a,b):
        return a+b
    def sum(self,a,b,c=0):  
        return a+b+c

obj =A()
print(obj.sum(10,20)) # If we don't give default value in line 7 then this will throw an error
print(obj.sum(10,20,30))



#Run-time  method-over Riding 
#different class, same method names with different parameters

class A:
    def sum(self,a,b):
        return a+b
class B(A):
    def sum(self,a,b):
        return a-b
    
obj =B()
print(obj.sum(10,20)) # Returns '-10' as it override the methods
        