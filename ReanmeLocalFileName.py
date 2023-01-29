import os
# os.rename(old_name, new_name)
path = input("Enter the path: ")
path = path.replace( "\\", "/") + "/"  #In windows directory are sep by "/" and in python we use "\"

print(path)

print(os.listdir(path))

# function to rename random name to car1, car2, car3 ... from path dir
def renameCarNo.():
  i = 1
  for filename in os.listdir(path):
    new_name = path + "car" + str(i) + ".jpg"
    old_name = path + filename
    os.rename(old_name,new_name)
    i+=1

def deleteLast30char():
    for filename in os.listdir(path):
        extension = filename[-4:]
        # print(extension)
        new_name  = path+filename[:-34]+extension
        print(new_name)
        old_name = path + filename
        os.rename(old_name, new_name)
deleteLast30char()
