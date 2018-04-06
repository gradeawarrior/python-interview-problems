"""
Description
===========

Write a simple function that take a input string, add a space after every 3rd character, and
return the modified string
"""


def simple_function(input):
    """
    Adds a space every 3rd character of an input

    :param input: String - some string
    :returns: String - A string with a space between every 3rd character
    """
    output = ""
    for index in range(len(input)):
        if index%3==0 and index!=0:
            output += " "
        output += input[index]
    return output

def main():
    input = "jalsdflbvflnvfmdklsdfsdjkbd"
    output = simple_function(input)
    print("Input: '%s'" % input)
    print("Output: '%s'" % output)


if __name__ == "__main__":
    main()
