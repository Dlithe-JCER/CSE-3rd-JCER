try:
    file=open('text.txt','w')
    file.write('Hello')
    print('content updated')
   
except:
    print('file is already exist')
finally:
    file.close()
    print('file closed')
