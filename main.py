# create prime list to file
def set_prime(num):
    if num < 2:
        print('ERROR: you must set a number bigger than 2!')
        return
    file = open("num.txt","w")
    for i in range(2,num):
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            file.write(str(i))
            file.write('\n')

    file.close()

# read prime from file
def get_prime(list):
    try:
        file = open("num.txt", 'r')
    except IOError:
        print("Read file ERROR!")
        return False
    for i in file.readlines():
        list.append(int(i))
    file.close()

# main function
def goldbach(num):
    if num < 6:
        print('ERROR: you must set a number bigger than 6!')
        return
    list = []
    if get_prime(list)==False:
        return
    work(num,list)

# work results out
def work(num,list):
    for n in range(6,num):
        jump = 0
        list1 = [i for i in list if i < n]
        for n1 in list1:
            if jump!=0:
                break
            for n2 in list1:
                if jump!=0:
                    break
                for n3 in list1:
                    if jump!=0:
                        break
                    if n1+n2+n3==n:
                        jump = 1
                        print(n,"=",n1,"+",n2,"+",n3)
                        break
        if jump == 0:
            print("ERROR!: ",n)
            exit()


if __name__ == "__main__":
    num = 100
    set_prime(num)
    goldbach(num)