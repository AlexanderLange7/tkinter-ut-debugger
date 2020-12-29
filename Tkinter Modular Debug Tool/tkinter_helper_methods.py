#Imports needed to test filenames
import os


def testFileNames():
    #Empty List
    testfilelist = []
    #Current Working Directory
    cwd = os.getcwd()
    print("Working in " + os.getcwd() + "\n")
    
    #Loop through each file in the directory
    #If it contains test in the filename
    #Add to a list and return
    for directory in os.walk(".", topdown = True):
        print("Directory: "+ str(directory[0]))
        #Directory is a tuple
        #dir[0] is the current dir
        #dir[1] is subdirs
        #dir[2] is files in the current dir
        for filename in directory[2]:
            print("File: " + str(filename))
            if "test" in filename:
                testfilelist.append(filename)
        #Linebreak when we move onto next dir        
        print ("\n")
    
    return testfilelist