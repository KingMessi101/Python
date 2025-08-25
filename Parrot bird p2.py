class Parrot:
 def __init__(self, name, age):
   self.name= name 
   self.age= age

   def sing(self, song):
     return"{} sings {}".format(self, name, song)
   def dance(self):
    return"{} is now dancing".format(self.name)
Blu= Parrot("Blu", 10)

print(Blu.sing("happy"))
print(Blu.dance())