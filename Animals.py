class Smart:
 species= "human"
 def __init__(self, name, age):
   self.name= name 
   self.age= age
Anish= Smart("Anish", 11)
Ali= Smart("Ali", 10)
print("Anish is a {}".format(Anish.species))
print("Ali is also a {}".format(Ali.species))
print("{} is {} years old".format(Anish.name, Anish.age))
print("{} is {} years old".format(Ali.name, Ali.age))