# your code goes here

def reverse_array(array):
    temp = 0
    index = 0
    length = len(array)
    rev_index = length - index - 1

    if length > 1:
        while (index < rev_index):
            temp = array[index]
            array[index] = array[rev_index]
            array[rev_index] = temp
            index += 1
            rev_index -= 1

    return array

if __name__ == "__main__":
    print(reverse_array([1,3,2]))