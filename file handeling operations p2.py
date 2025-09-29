new_file = open('new_file.text', 'x')
new_file.close()

import os
print("checking if my_file exists or not.... ")
if os.path.exists("my_file.txtx"):
    os.remove("my_file.txt")
else:
    print("The file does not exist.")

    my_file = open("my_file.txt", "w")
    my_file.write("Hi i'm penguin and I'm 1 years old.")
    my_file.close()

    os.remove('Codingal.txt')