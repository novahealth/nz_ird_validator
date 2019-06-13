import re


# This method will take the passed IRD
# and remove all non-numeric characters
def clean_ird(ird):
    # Store the IRD value locally
    ird_to_clean = ird

    # Uses regex to remove all non-numeric characters
    ird_clean = re.sub('[^0-9]', '', ird_to_clean)

    # adds the preceding 0 if IRD has 8 digits
    if len(ird_clean) < 9:
        ird_clean = "0" + str(ird_clean)

    # Returns the "clean" version of the IRD
    return ird_clean


# This method calculates for the check digit (the trailing digit in the IRD number)
# It multiplies each of the first 7 digits of the IRD number to their corresponding
# weight factor, sums it up then gets the remainder when divided by 11.
# The remainder is then compared to the check digit.
def get_remainder(ird, weights_sum):
    if weights_sum == 1:
        weights = [3, 2, 7, 6, 5, 4, 3, 2]
    else:
        weights = [7, 4, 3, 2, 5, 2, 7, 6]

    ird_list = list(ird)    # converts the IRD number into a list
    ird_list = list(map(int, ird_list))     # converts the IRD list of strings, to a list of integers

    result = map(lambda x, y: x * y, ird_list, weights) # multiply each of the weight factor and their associated ird digits

    results_sum = sum(result)   # sum of the result from

    # sum of the weights divided by 11, the "%" sign gives the remainder when divided by 11
    remainder = results_sum % 11
    return remainder


# This method will take the passed IRD
# and use the official validation process
# to determine whether the IRD is valid or invalid
def is_valid(ird):
    # cleans up the IRD before going through the checks
    ird = clean_ird(ird)
    if len((str(ird)[:-1])) == 8:  # check to see if the IRD number has the correct length
        if 10000000 <= int(ird) <= 150000000:  # check to see if the IRD number is in the correct range
            check_digit = ird[8]
            remainder = get_remainder(ird, 1)
            # if remainder is 0 and check digit (last digit of the IRD number) is 0, then IRD number is valid
            if int(remainder) == 0 and int(check_digit) == int(remainder):
                return True
            # if remainder is != 0, subtract it from 11
            elif int(remainder) != 0:
                remainder = 11 - int(remainder)
                #  if result is between 0 and 9
            if 0 <= int(remainder) <= 9 and int(remainder) == int(check_digit):
                # if 11 - remainder = check digit, then IRD number is valid
                return True
            # if result is = 10, recalculate weights using the secondary weight factor
            elif int(remainder) == 10:
                # calc for each digit using the secondary weight factor
                remainder = get_remainder(ird, 2)
                # if remainder is 0 and check digit (last digit of the IRD number) is 0, then IRD number is valid
                if int(remainder) == 0 and int(check_digit) == 0:
                    return True
                # if remainder is != 0, subtract it from 11
                elif int(remainder) != 0:
                    remainder = 11 - int(remainder)
                    if int(remainder) == int(check_digit):
                        return True
    return False
