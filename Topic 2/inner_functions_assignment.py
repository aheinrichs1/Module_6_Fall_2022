"""
Program: inner_functions_assignment.py
Author: Alex Heinrichs
Last date modified: 10/04/2022

Create a python file inner_functions_assignment.py.
In your inner_functions_assignment.py, write a function measurements
that accepts a list of measurements for a rectangle and
returns a string with perimeter and area
"""


def measurements(a_list):
    """
    :param a_list: list of numbers of a square or rectangle's dimensions
    :return: a string of result of the perimeter and area
    """

    def area(a_list1):
        """
        :param a_list1: a list of width of a square or width and height of a rectangle
        :return: a string of Area = area
        """

        if len(a_list1) == 1:
            width = float(a_list1.pop())
            area_result = width * width
        else:
            area_result = a_list1.pop() * a_list1.pop()
        str_result = f"Area = {str(area_result)} "
        return str_result

    def perimeter(a_list1):
        """
        :param a_list1: a list of width of a square or width and height of a rectangle
        :return: a string of Perimeter = perimeter
        """
        if len(a_list1) == 1:
            width = float(a_list1.pop())
            perimeter_result = width + width + width + width
        else:
            perimeter_result = (float(a_list1.pop()) * 2) + (float(a_list1.pop()) * 2)
        str_result = f"Perimeter = {str(perimeter_result)} "
        return str_result

    # copies list to use twice
    b_list = a_list.copy()
    final_result = perimeter(a_list) + area(b_list)
    return final_result

if __name__ == '__main__':
    rectangle = [2.1, 3.4]
    result = measurements(rectangle)
    print(result)
    square = [3.5]
    result = measurements(square)
    print(result)
