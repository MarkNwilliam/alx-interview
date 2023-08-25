#!/usr/bin/python3

def validUTF8(data):
    # Number of bytes in the current UTF-8 character
    n_bytes = 0

    # For each integer in the data array.
    for num in data:
        # Get the binary representation. We only need the least significant 8 bits
        # for any given number.
        bin_rep = format(num, '#010b')[-8:]

        # If this is the start of a new character.
        if n_bytes == 0:
            for bit in bin_rep:
                if bit == '0': break
                n_bytes += 1
            if n_bytes == 0:
                continue
            # 1 byte characters should start with 0xxxxxxx.
            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            # If it's one of the additional bytes in a character, it should start with 10xxxxxx.
            if not bin_rep.startswith('10'):
                return False
        n_bytes -= 1

    # This is for the case where we might left something incomplete.
    return n_bytes == 0

# You can now test the function with the given data sets.
