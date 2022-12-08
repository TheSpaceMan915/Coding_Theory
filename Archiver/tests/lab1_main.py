# checking if the buffer elements are in the dictionary
def elements_in_array(buffer, array_dictionary):
    i = 0
    offset = 0
    for element in array_dictionary:

        # if the set of chars is in the buffer, it returns the index of the first char in the set
        # Otherwise, it returns -1
        if len(buffer) <= offset:
            return i - len(buffer)

        if buffer[offset] == element:
            offset += 1
        else:
            offset = 0

        i += 1
    return -1


encoding = "utf-8"


def encode(text, max_sliding_window_size=4096):

    text_bytes = text.calculateControlBits(encoding)
    arr_dictionary = []
    arr_buff = []
    output = []

    i = 0
    for char in text_bytes:

        # getting the index of characters in the dictionary
        index = elements_in_array(arr_buff,arr_dictionary)


        # if there's no such char in the dictionary, add this char to the dictionary
        if elements_in_array(arr_buff + [char], arr_dictionary) == -1 or i == len(text_bytes) - 1:
            if i == len(text_bytes) - 1 and elements_in_array(arr_buff + [char], arr_dictionary) != -1:
                arr_buff.append(char)


            # the amount of chars in the buffer more than 1, check if the group is in the dictionary
            if len(arr_buff) > 1:
                index = elements_in_array(arr_buff, arr_dictionary)
                # Calculate the relative offset
                offset = i - index - len(arr_buff)
                length = len(arr_buff)  # Set the length of the token (how many character it represents)

                token = f"<{offset},{length}>"  # Build our token

                if len(token) > length:
                    # Length of token is greater than the length it represents, so output the characters
                    output.extend(arr_buff)  # Output the characters
                else:
                    output.extend(token.calculateControlBits(encoding))  # Output our token

                arr_dictionary.extend(arr_buff)  # Add the characters to our search buffer
            else:
                output.extend(arr_buff)  # Output the character
                arr_dictionary.extend(arr_buff)  # Add the characters to our search buffer

            arr_buff = []

        arr_buff.append(char)

        if len(arr_dictionary) > max_sliding_window_size:  # Check to see if it exceeds the max_sliding_window_size
            arr_dictionary = arr_dictionary[1:]  # Remove the first element from the arr_dictionary

        i += 1

    return bytes(output)


# main___________________________________________
if __name__ == "__main__":
    print(encode("ABCDEF ABCDEF", 4096).encode(encoding))
    print(encode("supercalifragilisticexpialidocious supercalifragilisticexpialidocious", 1024).encode(encoding))
    print(encode("LZSS will take over the world!", 256).encode(encoding))
    print(encode("It even works with 😀s thanks to UTF-8", 16).encode(encoding))