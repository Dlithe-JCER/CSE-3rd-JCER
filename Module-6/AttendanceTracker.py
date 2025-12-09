def createFile():
    fileName=input('Enter File Name')
    try:
        file=open(fileName,'x')
        if(file):
            print('File created ',fileName)
    except:
        print('File Already Exist')
def updateDetails():
    fileName=input('Enter File Name where you want to update the details')
    file=open(fileName,'a')
    n=int(input('Enter how many students details you want to update'))
    for i in range(n):
        name=input('Enter Student Name:')
        usn=input('Enter Student USN:')
        department=input('Enter Department Name: ')
        attendance=input('Enter Attendance Status: ')
        file.write(name+'\t'+usn+'\t'+department+'\t'+attendance+'\n')
    print('Content Updated ')
    file.close()

def readDetails():
    fileName=input('Enter File Name which you want to read')
    file=open(fileName,'r')
    content=file.read()
    print(content)
    file.close()
def main():
    while(True):
        print('1.createFile\n2.UpdateDetails\n3.ReadDeatils\n4.exit')
        ch=int(input('Enter Your Choice'))
        if(ch==1):
            createFile()
        elif(ch==2):
            updateDetails()
        elif(ch==3):
            readDetails()
        elif(ch==4):
            break 
        else:
            print('Invalid Choice')
main()