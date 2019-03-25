from sys import argv
if __name__ == '__main__':
    file_name=""
    to_do=[]
    if(len(argv)>1):
        file_name=argv[1]
        txt=open(file_name)
        to_do=txt.read().splitlines()
        txt.close()
    while True:
        print('1.insert a new task2.remove a task3.show all exsting tasks4.close the program/n')
        print('please insert the number index:')

        item = int(input())

        if item == 1:
            print('please insert a new task of string:')
            to_do.append(str(input()))

        elif item == 2:
            print('remove a task:')
            to_do.remove(str(input()))

        elif item == 3:
            print('show all existing tasks:')
            to_do = sorted(to_do)
            print(to_do)
            if len(to_do) < 1:
                print('empty')
            else:
                print(to_do)

        elif item == 4:
            print('close the program')
            break

        else:
            print('wrong number')
    if(filename!=""):
        txt=open(file_name,'w')
        for list in to_do:
            txt.write(list+"\n")
        txt.close()