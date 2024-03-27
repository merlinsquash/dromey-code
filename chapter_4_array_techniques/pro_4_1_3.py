def rotate_array(array, rotate_by):
    if rotate_by > 0 and rotate_by != len(array):
        if rotate_by > len(array):
            rotate_by = abs(len(array) - rotate_by)

        to_shift = array[:rotate_by]
        array = array[rotate_by:]
        array.extend(to_shift)

    return array


if __name__ == "__main__":
    print(rotate_array([1,6,7,8], 5))