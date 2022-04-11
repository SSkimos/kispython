import matplotlib.pyplot as plt
from random import randint
import numpy as np


def array_mirror_left(given_array):
    if len(given_array) % 2 == 0:
        given_array[len(given_array) //
                    2:] = given_array[len(given_array) // 2 - 1::-1]
    else:
        given_array[len(given_array) //
                    2:] = given_array[len(given_array)//2::-1]
    return given_array


# a = [1, 2, 3, 4, 5]    -> [1, 2, 3, 2, 1]
# b = [1, 2, 3, 4, 5, 6] -> [1, 2, 3, 3, 2, 1]

def smile_generator():
    two_dim_arr = []
    for i in range(5):
        local_arr = [0, 0, 0, 0, 0]
        for j in range(5):
            local_arr[j] = randint(0, 1)
        array_mirror_left(local_arr)
        two_dim_arr.append(local_arr)
    return two_dim_arr


def smile_show(double_array):
    fig, ax = plt.subplots()

    ax.imshow(double_array)

    fig.set_figwidth(6)
    fig.set_figheight(6)

    plt.show()
    return 1


def main():
    my_smile = smile_generator()
    smile_show(my_smile)
        


if __name__ == "__main__":
    main()
