class myclass:
    x=5
ob=myclass()
print(ob.x)

class person:
    def __init__(self,nam,ag):
          #init-> fxn which is called automatically everytime class is used to create new objects
        self.name=nam
        self.age=ag
    def myfxn(myins):  
          #self,myins etc are my instances i can name them anything i want and they are used to refer my variables of the class.it is always1 parameter of fxn
        print('name is '+myins.name)
p1=person('sukhman',20)
print('name =',p1.name)
print('age =',p1.age)

p2=person('simran',18)
print('name =',p2.name)
print('age =',p2.age)

del p1.age   #deletes the property of age for object p1
# print('age =',p1.age)  #->printing this will give an error as it has been deleted

p1.myfxn()
p2.myfxn()