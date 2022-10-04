"""
Program: validate_input_in_functions.py
Author: Alex Heinrichs
Last date modified: 10/04/2022

The test_name is a mandatory parameter and will not need validation.
The test_score is optional, with default value that is negative,
eg -1, and will be validated to be between 0-100
The invalid_message is optional, with default value 'Invalid test score!'
Return the string with test name and score if it passes validation;
otherwise return the test name with invalid_message
"""


def score_input(test_name, test_score=-1, invalid_message="Invalid test score!"):
    """
    :param test_name: Mandatory string of name of the test
    :param test_score: Int that must be between 0-100, defaults to -1
    :param invalid_message: String of the error message if test score is invalid, defaults to 'Invalid test score!'
    :return: String with test_name, and Score such as 'Test 1: 70'
             Or else string with test_name and error message is score is invalid
    """

    try:
        test_score = int(test_score)
        if 0 <= test_score <= 100:
            output = f"{test_name}: {str(test_score)}"
        else:
            raise IndexError
    except ValueError:
        output = f"{test_name}: ValueError encountered!"
    except IndexError:
        output = f"{test_name}: {invalid_message}"
    finally:
        return output

if __name__ == '__main__':
    display_string = score_input('Test 1', 70)
    print(display_string)
    display_string = score_input('Test 2', -40)
    print(display_string)
    display_string = score_input('Test 3', 150)
    print(display_string)
    display_string = score_input('Test 4', 'ValueError')
    print(display_string)
