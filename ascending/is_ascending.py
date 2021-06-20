
def main():
    my_list = []
    count = 0
    number = 0
    while number != -1:
        number = int(input('>'))
        my_list.append(number)
        count += 1
    x = 0
    my_list.remove(-1)
    count -= 2
    if ascending(x,count,my_list):
        print("Is Ascending! :)")

    else:
        print("Not Ascending :(")

def ascending(x,count,my_list):
    x1 = my_list[x]
    x2 = my_list[count-1]

    if x1 < x2:
        for elem in my_list:
            print(elem)
        return True
    else:
        for elem in my_list:
            print(elem)
        return False

if __name__ == '__main__':
    main()
