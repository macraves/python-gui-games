"""Reading text and number entity"""


class InvalidRangeError(Exception):
    """Exception raised for invalid range"""

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


def read_text(prompt):
    """
    Display  a prompt and reads in string of text
    Keyboard Interrupts (Ctrl+C) are ignored
    returns string containing the string input by user
    """
    while True:
        try:
            result = input(prompt)
            if result.strip() == "":
                raise ValueError
            return result
        except KeyboardInterrupt:
            print("Please do not attempt to stop the program ")
        except ValueError:
            print("Do not leave empty please enter text")


def read_number(prompt, function):
    """
    Read a number with destinated function
    """
    while True:
        try:
            number_text = read_text(prompt)
            result = function(number_text)
            return result
        except ValueError:
            print("Please enter a number")


def read_int(prompt):
    """
    Display prompt and reads entry as integer
    Invalid Entries rejected
    Returns a integer containing value input by user"""
    return read_number(prompt, int)


def read_float(prompt):
    """
    Display prompt and reads in floating point number
    Invalid Entries are rejected
    Returns a float point number value input by user"""
    return read_number(prompt, float)


def read_number_ranged(prompt, func, min_val, max_val):
    """Arange number range as min and max value"""
    if min_val > max_val:
        raise InvalidRangeError("Minimum value greater than max value")
    while True:
        result = read_number(prompt, func)
        if result < min_val:
            print("Entered number is too low\nMinimum value is: ", min_val)
            continue
        if result > max_val:
            print("Entered number is too high\nMaximum value is: ", max_val)
            continue
        # If we get her loop is valid than break and send result
        return result


def read_int_ranged(prompt, minimum_value, maximum_value):
    """Display prompt read integer minimum and maximum value
    Raises InvalidRangeError if min and max value wrong way round"""
    return read_number_ranged(prompt, int, minimum_value, maximum_value)


def read_float_ranged(prompt, minimum_value, maximum_value):
    """Display prompt read float minimum and maximum value
    Raises InvalidRangeError if min and max value wrong way round"""
    return read_number_ranged(prompt, float, minimum_value, maximum_value)
