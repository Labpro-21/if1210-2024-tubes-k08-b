def is_valid_string(input_string):
    for char in input_string:
        ascii_value = ord(char)
        # Check if the character is a letter, number, hyphen, or underscore
        valid = (
            (65 <= ascii_value <= 90) or  # A-Z
            (97 <= ascii_value <= 122) or # a-z
            (48 <= ascii_value <= 57) or  # 0-9
            ascii_value == 45 or          # hyphen (-)
            ascii_value == 95             # underscore (_)
        )
        # If any character is not valid, return False
        if valid == False:
            return False
    return True

# Example usage:
print(is_valid_string("---___#")) 

