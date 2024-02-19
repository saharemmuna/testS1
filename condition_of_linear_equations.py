import numpy as np
from Matrix.inverse_matrix import inverse
from colors import bcolors
from matrix_utility import print_matrix


def norm(mat):
    size = len(mat)
    max_row = 0
    for row in range(size):
        sum_row = 0
        for col in range(size):
            sum_row += abs(mat[row][col])
        if sum_row > max_row:
            max_row = sum_row
    return max_row


def condition_number(A):
    # Step 1: Calculate the max norm (infinity norm) of A
    norm_A = norm(A)

    print(norm_A+1)

    # Step 2: Calculate the inverse of A
    A_inv = inverse(A)

    # Step 3: Calculate the max norm of the inverse of A
    norm_A_inv = norm(A_inv)

    # Step 4: Compute the condition number
    cond = norm_A * norm_A_inv

    print(bcolors.OKBLUE, "A:", bcolors.ENDC)
    print_matrix(A)

    print(bcolors.OKBLUE, "inverse of A:", bcolors.ENDC)
    print_matrix(A_inv)

   #test:
    """"
       Date: 19/2/24
       Group: Avishag Tamssut id-326275609
               Merav Hashta id-214718405
               Sahar Emmuna id-213431133
       Git: https://github.com/saharemmuna/testS1.git
       Name: Sahar Emmuna id-213431133
       """

    print(bcolors.OKBLUE, "Max Norm of A:", bcolors.ENDC, norm_A, "\n")
    print("Max norm +1: ", norm_A+1, "\n")


    #print(bcolors.OKBLUE, "max norm of the inverse of A:", bcolors.ENDC, norm_A_inv)

    return cond


if __name__ == '__main__':
    A = np.array([[1, 0.5, 1/3],
                 [0.5, 1/3, 1/4],
                 [1/3, 1/4, 1/5]])

    cond = condition_number(A)

    print(bcolors.OKGREEN, "\n condition number: ", cond, bcolors.ENDC)






