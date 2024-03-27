# your code goes here

def array_switch(array):
    temp = 0
    index = 0
    length = len(array)

    if length > 1:
        while (index < length):
            if index % 2 == 0 and (length) % 2 != 0:
                temp = array[index]
                array[index] = array[length -1]
                array[length - 1] = temp
                index += 1
                length -= 1

    return array

if __name__ == "__main__":
    print(array_switch([1,2,3,4,5,6,7]))