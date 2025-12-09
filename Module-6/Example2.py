try:
    file=open('cseB.txt','a')
    file.write('\nHello CSE A') 
    print('content updated')
except:
    print('file is already exist')
