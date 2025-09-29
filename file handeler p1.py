with open('Codingal.txt', 'w') as file:
 file.write("Hi, i'm penguin and i'm 1 years old.")
file.close()

with open('Codingal.txt', 'r') as file:
 data = file.readlines()
print("words in file are.... ")
for line in data:
 word =line.split()
 print (word)
file.close()