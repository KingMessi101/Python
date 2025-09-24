file = open('Codingal.txt', 'r')
print(file.read())
file.close()

file = open('Codingal.txt', 'r')
print ("\n Read in Parts \n")
print(file.read(8))
file.close()

file = open('Codingal.txt', 'a')
file.write("Hi I am Penguin and I am 1 year old.")
file.close()