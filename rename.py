import os

def rename_fun():
    os.chdir("D:\prank")
    file_names = os.listdir('D:\prank')
    print (file_names)

    for names in file_names:
        os.rename(names,names.translate(str.maketrans('','','0123456789')))



rename_fun()

k = os.getcwd()
print (k)
