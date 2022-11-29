import math


def calculateControlBits(size, str_sequence):
    print("The encoding has started")

    amount_control_bits = math.ceil(math.log2(size))
    list_sequence = [int(i) for i in str_sequence]
    i = 1


    # inserting 0 the indexes that equal powers of 2
    print("Inserting control bits")
    while (i< len(list_sequence)):
        list_sequence.insert(i - 1, 0)
        list_indexes = [j+1 for j in range(len(list_sequence))]
        i = i * 2

    print(list_indexes)
    print(list_sequence)
    print("Inserting has finished")
    print(" ")


    # creating a 2D array with matrixes
    list_matrices = [[] for i in range(amount_control_bits)]
    # list_indexes = [i + 1 for i in list_indexes]
    list_bits = [bin(i)[2::] for i in list_indexes]

    for i in range(len(list_bits)):
        if (len(list_bits[i]) < amount_control_bits):
            list_bits[i] = '0' * (amount_control_bits - len(list_bits[i])) + list_bits[i]
    list_bits = [l[::-1] for l in list_bits]
    # print(list_bits)

    print("Printing the matrix of bits")
    for i in list_bits:
        for j in range(len(i)):
            list_matrices[j].append(int(i[j]))
    for i in list_matrices:
        print(i)


    # calculating the values of control bits
    list_control_bit_values = []
    for i in range(amount_control_bits):
        value = 0
        for j in range(len(list_sequence) - 1):
            value += list_matrices[i][j] * list_sequence[j]
        value = value % 2
        list_control_bit_values.append(value)
    print(" ")
    print("The values of control bits: ", list_control_bit_values)


    # creating a 2D array with inserted control bits
    list_sequence_copy = list_sequence.copy()
    i = 1
    j1 = 0
    while (i < len(list_sequence_copy)):
        list_sequence_copy[i - 1] = list_control_bit_values[j1]
        j1 += 1
        i = i * 2

    print('Indexes: ', list_indexes)
    print('The initial sequence: ', list_sequence)
    print('The sequence with inserted control bits: ', list_sequence_copy)
    print("The encoding has ended")
    print(' ')
    return [list_sequence_copy, list_matrices, list_indexes, amount_control_bits]


def findError(data):
    print("The decoding has started")

    # adding an error
    sequence_copy = data[0]
    sequence_copy[9] = 1
    print('The sequence with an error: ', sequence_copy)


    # getting data from the data array
    matrices = data[1]
    indexes = data[2]
    number_control_bits = data[3]


    # calculating the values of control bits
    list_control_bit_values = []
    for i in range(number_control_bits):
        value = 0
        for j in range(len(sequence_copy) - 1):
            value += matrices[i][j] * sequence_copy[j]
        value = value % 2
        list_control_bit_values.append(value)
    print("The values of control bits: ", list_control_bit_values)
    print(" ")


    print("Printing the matrix of bits")
    for i in matrices:
        print(i)
    print(" ")


    # finding the error bit
    list_control_bit_values = list_control_bit_values[::-1]
    str_error_bit = ''
    for i in list_control_bit_values:
        str_error_bit += str(i)
    error = int(str_error_bit, 2)

    print('The position of the error bit: ', error)
    print("The decoding has ended")


if __name__ == "__main__":
    # print("Enter the size of the sequence: ")
    # N = int(input())
    N = 10
    sequence = '1111000010'

    list_data = calculateControlBits(N, sequence)
    findError(list_data)
