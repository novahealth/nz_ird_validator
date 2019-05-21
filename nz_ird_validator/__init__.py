import re

name = "nz_ird_validator"


def is_valid(ird):
    ird_to_clean = ird

    ird_clean = re.sub('[^0-9]', '', ird_to_clean)
    
    return ird_clean
