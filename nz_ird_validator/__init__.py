import re


# This method will take the passed IRD
# and remove all non-numeric characters
def clean_ird(ird):
    # Store the IRD value locally
    ird_to_clean = ird

    # Uses regex to remove all non-numeric characters
    ird_clean = re.sub('[^0-9]', '', ird_to_clean)

    # Returns the "clean" version of the IRD
    return ird_clean


# This method will take the passed IRD
# and use the official validation process
# to determine whether the IRD is valid or invalid
def is_valid(ird):
    # Initialise the boolean variable that stores
    # whether the IRD tax number is valid or invalid
    is_ird_valid = False

    # For "safety" reasons use the clean method to make sure the IRD number
    # only contains numerical characters before validating
    ird_to_validate = clean_ird(ird)

    weights_first = [3, 2, 7, 6, 5, 4, 3, 2]
    weight_second = [7, 4, 3, 2, 5, 2, 7, 6]

    if len(ird_to_validate) == len(weights_first):  # check to see if the IRD number has the correct length
        if 10000000 <= ird_to_validate >= 150000000:    # check to see if the IRD number is in the correct range
            if len(ird_to_validate) < 8:
                ird_to_validate = "0" + str(ird_to_validate)    # if length of IRD number is < 8 then add a leading 0

                one = int(ird_to_validate[0]) * int(weights_first[0])

    else:
        print("IRD IS INVALID")


    return is_ird_valid
