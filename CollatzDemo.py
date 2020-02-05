def collatz(num):
    if num == 1:
        print(num)
        return num
    elif (num % 2) == 0:
        print("number%2:"+str(num))
        return collatz(num / 2)
    else:
        print("3*number+1:"+str(num))
        return collatz(3 * num + 1)


number = input("请输入一个数:")
collatz(int(number))