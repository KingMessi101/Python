class Parrot:
 species= "bird"
 def __init__(self, name, age):
   self.name= name 
   self.age= age
Blu= Parrot("Blu", 10)
Woo= Parrot("Woo", 15)
print("Blu is a {}".format(Blu.species))
print("Woo is also a {}".format(Woo.species))
print("{} is {} years old".format(Blu.name, Blu.age))
print("{} is {} years old".format(Woo.name, Woo.age))