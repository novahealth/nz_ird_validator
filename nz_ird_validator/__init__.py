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

    return is_ird_valid

