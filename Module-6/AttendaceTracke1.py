def createFile():
    fileName=input('Enter File Name You Want tO Create')
    try:
        file=open(fileName,'x')
        if(file):
            print('file created')
    except:
        print('file already exist')
def updateFile():
    fileName=input('Enter File Name where you want to update the details\n')
    file=open(fileName,'a')
    n=int(input('Enter Number Of Students Deatils You Want to update'))
    for i in range(n):
        name=input('Enter Student Name :')
        usn=input('Enter USN :')
        department=input('Enter Student Department Name :')
        attendance=input('Update attendace status')
        file.write(name+'\t'+usn+'\t'+department+'\t'+attendance)
    file.close()
def main():
    while(True):
        print('1.createFile\n2.updateFile\n3.readFile\n4.exit\n')
        ch=int(input('Enter Your Choice\n'))
        if(ch==1):
            createFile()
        elif(ch==2):
            updateFile()
        elif(ch==4):
            break
        else:
            print
            ('Invalid')
main()
